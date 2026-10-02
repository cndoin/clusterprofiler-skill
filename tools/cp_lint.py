#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cp_lint.py —— clusterProfiler R 脚本静态校验器（防幻觉）

做的事：
  1. 扫描 R 脚本里所有函数调用
  2. 函数名必须在 whitelist.json（38 个包解析出的 6137 个键，含 `pkg::sym` 限定名与第三方 re-export）
     —— 不存在 = ERROR，并给出「大小写改错 / 拼写相近」的正确写法建议
  3. 命名参数必须是该函数真实拥有的参数名 —— 不存在 = ERROR
  4. 结构性检查：中文全角括号、library() 缺失

退出码：0 = 无 error；1 = 有 error；2 = 用法或文件错误
stdout 只放 JSON（--json）或纯文本报告；人类提示走 stderr

数据来源：tools/whitelist.json，由 tools/etl/build_api.py 从上游源码事实生成。
"""
import io, os, re, sys, json, argparse, difflib

HERE = os.path.dirname(os.path.abspath(__file__))

# 反面案例标记：含此注释的代码块在文档示例中用，cp_lint 整体跳过
SKIP_MARKER = "# cp_lint_skip"
WL_PATH = os.path.join(HERE, "whitelist.json")

# ---------------------------------------------------------------- 基础放行表
# base R / utils / stats / graphics / methods 常用函数
BASE_R = set("""
c list data.frame as.data.frame matrix as.matrix vector numeric character logical integer
factor levels nlevels droplevels cut table prop.table xtabs aggregate by
sum mean median sd var mad quantile range min max sum pmax pmin abs sqrt exp log log2 log10
round ceiling floor signif trunc
seq seq_along seq_len rep rev sort order rank unique duplicated any all which which.max which.min
length dim nrow ncol NROW NCOL dimnames rownames colnames row.names names
head tail sample set.seed runif rnorm rbinom sample.int
paste paste0 sprintf format formatC nchar substr substring grep grepl gsub sub regexpr
tolower toupper trimws strsplit unlist split unsplit rbind cbind do.call
apply sapply lapply vapply mapply tapply Reduce Filter Map
is.null is.na is.numeric is.character is.logical is.factor is.matrix is.data.frame is.list
isTRUE identical all.equal inherits class as.character as.numeric as.integer as.logical
ls rm gc memory.size memory.limit browser debug trace untrace
ifelse switch match
commandArgs args
sink source file close quit
withCallingHandlers tryCatch conditionMessage conditionCall invokeRestart
muffleWarning simpleWarning simpleError
packageVersion packageDescription update.packages
unlink file.remove file.rename file.copy file.info
read.dcf write.dcf
getwd setwd dir create.dir
Sys.which Sys.sleep Sys.setlocale
print cat message warning stop try tryCatch suppressWarnings suppressMessages
stdout stderr stdin sink.number connections showConnections
summary str glimpse View head.data.frame
library require requireNamespace loadNamespace installed.packages install.packages
Sys.getenv Sys.setenv Sys.getpid Sys.info R.version R.version.string sessionInfo
options getOption setOption new.env environment assign exists
read.csv read.table write.csv write.table readLines writeLines readRDS saveRDS load save
file.path file.exists dir.exists dir.create list.files list.dirs
Sys.time Sys.Date date as.Date as.POSIXct difftime system.time
par plot points lines abline text legend title axis box grid mtext
pdf png jpeg svg dev.off dev.new ggsave
setwd getwd
invisible return quote eval parse deparse substitute missing on.exit
seq.int rev.default stopifnot with within transform merge.data.frame
nchar utils::head tibble as_tibble
rownames<- colnames<- names<- levels<- class<- dimnames<-
for if else while repeat function break next TRUE FALSE NULL NA NaN Inf
data.table as.data.table setDT setDF melt dcast
data barplot pie hist curve abline mtext axis grid boxpanel layout
""".split())

# 第三方包常见函数（不校验，仅记录）
KNOWN_3RD = set("""
ggplot aes geom_point geom_line geom_tile geom_boxplot geom_violin geom_density
theme_bw theme_classic theme_minimal theme element_text element_rect element_blank
facet_wrap facet_grid labs xlab ylab xlim ylim coord_equal coord_fixed register MulticoreParam SnowParam bplapply bpmapply bpiterate bpvec SerialParam
future plan multisession multicore sequential multisessionWorkers
scale_fill_gradient scale_color_gradient scale_fill_brewer scale_color_manual
ggsave unit grid.arrange
""".split())

R_KEYWORDS = {"if", "for", "while", "repeat", "function", "else", "return", "break", "next"}


# ---------------------------------------------------------------- 词法扫描
def strip_code(src):
    """去掉注释与字符串字面量，保留长度以便算行号；字符串替换为 \" \" """
    out, inq, i, n = [], None, 0, len(src)
    while i < n:
        ch = src[i]
        if inq:
            if ch == "\\":
                out.append("  "); i += 2; continue
            if ch == inq:
                inq = None
            out.append(" " if ch != "\n" else "\n"); i += 1; continue
        if ch == "#":
            while i < n and src[i] != "\n":
                out.append(" "); i += 1
            continue
        if ch in "\"'":
            inq = ch; out.append(" "); i += 1; continue
        if ch == "`":
            j = src.find(")", i + 1)   # 反引号闭合（python str.find 用 ')'，R 用 '`'）
            j = src.find("`", i + 1)
            if j == -1:
                j = n - 1
            out.append(src[i:j + 1]); i = j + 1; continue
        out.append(ch); i += 1
    return "".join(out)


IDENT_START = re.compile(r"[A-Za-z._]")
IDENT_BODY = re.compile(r"[A-Za-z0-9._]")


def scan_calls(code):
    """返回 [(name, line, [argnames], pkg)]"""
    calls = []
    stack = []
    i, n = 0, len(code)
    cur = ""
    last_ns = None
    cur_line = 1

    def flush_ident():
        nonlocal cur
        v = cur
        cur = ""
        return v

    while i < n:
        ch = code[i]
        if ch == "\n":
            cur_line += 1
            # 换行处要 flush 当前 ident，否则下一行的 ident 会被串进上一行
            # 例：'deg\$log2fc\nnames' → 'log2fcnames' 误识别
            cur = ""
            i += 1
            continue
        if IDENT_START.match(ch) and (not cur or True):
            if not cur:
                j = i
                while j < n and IDENT_BODY.match(code[j]):
                    j += 1
                cur = code[i:j]
                i = j
                continue
            else:
                j = i
                while j < n and IDENT_BODY.match(code[j]):
                    j += 1
                cur += code[i:j]
                i = j
                continue
        if ch == "(":
            name = flush_ident()
            if name in R_KEYWORDS or name == "":
                stack.append({"kind": "paren", "name": "", "line": cur_line,
                              "args": [], "pkg": None, "seg": i + 1})
            else:
                stack.append({"kind": "call", "name": name, "line": cur_line,
                              "args": [], "pkg": last_ns, "seg": i + 1})
            last_ns = None
            i += 1
            continue
        if ch == "[" or ch == "{":
            flush_ident()
            stack.append({"kind": "idx", "name": "", "line": cur_line,
                          "args": [], "pkg": None, "seg": i + 1})
            i += 1
            continue
        if ch == ")" or ch == "]" or ch == "}":
            if stack:
                fr = stack.pop()
                if fr["kind"] == "call":
                    calls.append((fr["name"], fr["line"], fr["args"], fr["pkg"]))
            flush_ident()
            i += 1
            continue
        if ch == "," and stack:
            fr = stack[-1]
            fr["seg"] = i + 1
            i += 1
            continue
        if ch == "=" and stack:
            fr = stack[-1]
            nxt = code[i + 1] if i + 1 < n else ""
            prev = code[i - 1] if i > 0 else ""
            if nxt != "=" and prev not in "=<>!+-*/&|^":
                # 必须先 flush：否则左值名会与右值的标识符粘连。
                # 例：`aggregate(x, by = list(cyl), FUN = mean)` 里的 `by=list`
                # 会被读成一个名为 `bylist` 的函数调用，
                # 既丢了真实的 `list()` 调用，又多报一个 unknown-function。
                flush_ident()
                seg = code[fr["seg"]:i]
                m = re.match(r"^\s*([A-Za-z._][A-Za-z0-9._]*)\s*$", seg)
                if m and fr["kind"] == "call":
                    j = i + 1
                    while j < n and code[j] in " \t":
                        j += 1
                    vm = re.match(r"([A-Za-z._][A-Za-z0-9._]*)", code[j:])
                    val = vm.group(1) if vm else None
                    fr["args"].append([m.group(1), cur_line, val])
            i += 1
            continue
        if ch == ":" and i + 1 < n and code[i + 1] == ":":
            last_ns = flush_ident()
            i += 2
            continue
        if ch in "$@%":
            flush_ident()
            i += 1
            continue
        if not IDENT_BODY.match(ch):
            flush_ident()
        i += 1

    for fr in stack:
        if fr["kind"] == "call":
            calls.append((fr["name"], fr["line"], fr["args"], fr["pkg"]))
    return calls


# ---------------------------------------------------------------- 主逻辑
def load_wl():
    if not os.path.exists(WL_PATH):
        sys.stderr.write("ERROR: whitelist.json not found at %s\n" % WL_PATH)
        sys.stderr.write("Run `python3 tools/etl/rebuild.py` to regenerate it.\n")
        sys.exit(2)
    return json.loads(io.open(WL_PATH, encoding="utf-8").read())


def suggest(name, symbols):
    lower = {k.lower(): k for k in symbols}
    if name.lower() in lower and lower[name.lower()] != name:
        return "大小写错误，应为 `%s`" % lower[name.lower()]
    close = difflib.get_close_matches(name, list(symbols), n=3, cutoff=0.72)
    if close:
        return "是否想写：%s" % ", ".join("`%s`" % c for c in close)
    close2 = difflib.get_close_matches(name.lower(), [k.lower() for k in symbols], n=3, cutoff=0.72)
    if close2:
        real = [lower.get(c, c) for c in close2]
        return "是否想写：%s" % ", ".join("`%s`" % c for c in real)
    return None


def lint(path, wl, allow_unknown=False):
    symbols = wl["symbols"]
    deprecated = wl.get("deprecated_args", {})
    try:
        raw = io.open(path, encoding="utf-8", errors="replace").read()
    except Exception as e:
        return {"ok": False, "fatal": "cannot read file: %r" % e,
                "errors": [], "warnings": []}

    # 文档反面案例：含 \code cp_lint_skip 注释则整个文件跳过校验
    if SKIP_MARKER in raw:
        return {
            "ok": True, "file": os.path.abspath(path),
            "whitelist": wl.get("generated_from", {}),
            "errors": [], "warnings": [],
            "stats": {"calls_found": 0, "cp_calls_checked": 0,
                       "errors": 0, "warnings": 0,
                       "skipped": True, "reason": "contains cp_lint_skip marker"},
        }

    errors, warnings = [], []

    # R 语法健全性：括号 / 引号配对
    clean = strip_code(raw)
    pairs = {")": "(", "]": "[", "}": "{"}
    opens = {"(": 0, "[": 0, "{": 0}
    stk, ln = [], 1
    for ch in clean:
        if ch == "\n":
            ln += 1
            continue
        if ch in "([{":
            stk.append((ch, ln)); opens[ch] += 1
        elif ch in ")]}":
            if not stk or stk[-1][0] != pairs[ch]:
                errors.append({"line": ln, "code": "syntax",
                               "msg": "括号不匹配：多出的 `%s`" % ch})
                break
            stk.pop()
    if stk:
        errors.append({"line": stk[-1][1], "code": "syntax",
                       "msg": "括号未闭合：`%s`（第 %d 行开始）" % (stk[-1][0], stk[-1][1])})
    for o, c in (("(", ")"), ("[", "]"), ("{", "}")):
        if clean.count(o) != clean.count(c):
            errors.append({"line": 0, "code": "syntax",
                           "msg": "`%s` 与 `%s` 数量不等（%d vs %d），可能有未闭合括号"
                                  % (o, c, clean.count(o), clean.count(c))})
    if clean.count('"') % 2 == 1 or clean.count("'") % 2 == 1:
        errors.append({"line": 0, "code": "syntax",
                       "msg": "引号数量为奇数，可能有未闭合字符串"})

    # 结构性检查
    for ln, line in enumerate(clean.split("\n"), 1):
        for bad in ("（", "）", "，", "；", "＝", "“", "”", "＋", "－", "："):
            if bad in line:
                errors.append({"line": ln, "code": "fullwidth",
                               "msg": "代码中出现中文全角符号 `%s`，R 无法解析（注释/字符串里无妨）" % bad})
                break

    used_cp = any(n in symbols for n, _l, _a, _p in scan_calls(strip_code(raw)))
    if used_cp and not re.search(r"^\s*(library|require)\s*\(\s*['\"]?clusterProfiler['\"]?\s*\)", raw, re.M):
        warnings.append({"line": 0, "code": "no-library",
                         "msg": "脚本用了 clusterProfiler 系列函数但没有 library(clusterProfiler)，确认是否已加载"})

    code = strip_code(raw)
    calls = scan_calls(code)

    # 用户自定义函数
    user_defs = set(re.findall(r"([A-Za-z._][A-Za-z0-9._]*)\s*<-\s*function", code))
    user_defs |= set(re.findall(r"([A-Za-z._][A-Za-z0-9._]*)\s*=\s*function", code))

    # 生态包集合。只有这些包的 `pkg::fn` 调用才在射程内；
    # `dplyr::filter` / `ggplot2::aes` 这类生态外调用直接放行（不报错也不校验）。
    # 关键：白名单里出现过 `pkg::sym` 限定名的包必须在集合里，
    # 否则会把一个已经有事实数据的包当成生态外而静默跳过。
    eco_pkgs = {k.split("::", 1)[0] for k in symbols if "::" in k}
    eco_pkgs.add("clusterProfiler")
    eco_pkgs |= set((wl.get("generated_from", {}) or {}).get("packages", {}) or {})

    checked = 0
    noformals = 0          # 只有导出名、无法校验参数的调用数（诚实暴露校验覆盖率）
    seen_unknown = set()
    for name, line, args, pkg in calls:
        if not name:
            continue
        if name in user_defs:
            continue
        if pkg is not None:
            # `pkg::fn` 限定调用：先按限定名查，再回退到短名
            if pkg not in eco_pkgs:
                continue
            label = pkg + "::" + name
            sym = symbols.get(label) or symbols.get(name)
        else:
            if name in BASE_R or name in KNOWN_3RD:
                continue
            label = name
            sym = symbols.get(name)

        if sym is None:
            if label in seen_unknown:
                continue
            seen_unknown.add(label)
            tip = suggest(name, symbols.keys())
            item = {"line": line, "code": "unknown-function", "name": name,
                    "msg": "`%s()` 不在 clusterProfiler 生态的导出 / re-export 清单里"
                          % label}
            if tip:
                item["msg"] += "；" + tip
            else:
                item["msg"] += "；若来自其他包请先 library() 并用 `pkg::fn()` 调用"
            if allow_unknown:
                warnings.append(item)
            else:
                errors.append(item)
            continue

        checked += 1
        valid = set(sym["args"])
        if not valid:
            # 空 args = 我们只拿到了导出名、没解析到 formals。
            # 此时“没有这个参数”是**没有证据**，不是证据表明不存在。
            # 若照常报 unknown-arg，会把 `diversity(index=)`、
            # `plotCov(col=, lwd=)` 这类正确代码全部误杀。
            noformals += 1
            continue
        has_dots = "..." in valid

        for an, aln, av in args:
            if an in valid:
                continue
            tip = suggest(an, valid)
            item = {"line": aln, "code": "unknown-arg", "name": name,
                    "msg": "`%s()` 没有参数 `%s`" % (name, an)}
            if tip:
                item["msg"] += "；" + tip
            if has_dots:
                # 函数带 ...（透传场景），降级为 warning 而不是 error
                item["msg"] += "（该函数有 `...`，若确系透传给下游请人工确认）"
                item["severity"] = "warning"
                warnings.append(item)
            else:
                errors.append(item)
        dep = deprecated.get(name, {})
        for an, aln, av in args:
            if an in dep:
                warnings.append({"line": aln, "code": "deprecated-arg", "name": name,
                                 "msg": "`%s(%s=)` 已弃用：%s" % (name, an, dep[an])})

    return {
        "ok": len(errors) == 0,
        "file": os.path.abspath(path),
        "whitelist": wl.get("generated_from", {}),
        "errors": errors,
        "warnings": warnings,
        "stats": {"calls_found": len(calls),
                  "cp_calls_checked": checked,
                  "args_unverified": noformals,
                  "errors": len(errors), "warnings": len(warnings)},
    }


def render(res):
    out = []
    out.append("cp_lint · clusterProfiler 脚本校验")
    out.append("  file: %s" % res["file"])
    g = res.get("whitelist", {})
    if g:
        out.append("  底座: clusterProfiler %s" % g.get("clusterprofiler", "?"))
    s = res["stats"]
    out.append("  调用 %d 处，clusterProfiler 系列函数校验 %d 个" %
               (s["calls_found"], s["cp_calls_checked"]))
    if s.get("args_unverified"):
        out.append("  其中 %d 处只有导出名、无 formals，未作参数校验"
                   % s["args_unverified"])
    out.append("")
    if res["errors"]:
        out.append("ERROR (%d)" % len(res["errors"]))
        for e in res["errors"]:
            out.append("  L%-5s [%s] %s" % (e["line"], e["code"], e["msg"]))
        out.append("")
    if res["warnings"]:
        out.append("WARNING (%d)" % len(res["warnings"]))
        for w in res["warnings"]:
            out.append("  L%-5s [%s] %s" % (w["line"], w["code"], w["msg"]))
        out.append("")
    out.append("RESULT: %s" % ("PASS" if res["ok"] else "FAIL"))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="校验 R 脚本里的 clusterProfiler 函数与参数是否真实存在")
    ap.add_argument("files", nargs="+", help="要校验的 .R 文件")
    ap.add_argument("--json", action="store_true", help="stdout 只输出 JSON")
    ap.add_argument("--allow-unknown", action="store_true",
                    help="把未识别函数从 error 降为 warning（用了很多第三方包时）")
    ap.add_argument("--quiet", action="store_true", help="只输出结论行")
    a = ap.parse_args()

    wl = load_wl()
    results = []
    for f in a.files:
        if not os.path.isfile(f):
            sys.stderr.write("ERROR: no such file: %s\n" % f)
            sys.exit(2)
        results.append(lint(f, wl, allow_unknown=a.allow_unknown))

    ok = all(r["ok"] for r in results)
    if a.json:
        payload = results[0] if len(results) == 1 else {"results": results, "ok": ok}
        sys.stdout.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    elif a.quiet:
        for r, f in zip(results, a.files):
            print("%s  %s  (E%d/W%d)" % ("PASS" if r["ok"] else "FAIL", f,
                                         len(r["errors"]), len(r["warnings"])))
    else:
        for r in results:
            print(render(r))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()