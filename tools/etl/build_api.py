# -*- coding: utf-8 -*-
"""从 YuLab-SMU 生态包的源码生成 skill 的事实底座。

支持的包（详见 fetch_sources.py 的 PACKAGES 字典）：clusterProfiler / DOSE /
ReactomePA / meshes / GOSemSim / ChIPseeker / MicrobiomeProfiler / HDO / aPEAR /
enrichit / enrichplot / gson / aisdk / ggtree / treeio / ggtreeExtra / tidytree /
MicrobiotaProcess / SVP / sclet / scMSGNN / ggsc / createKEGGdb / CNEr /
yulab.utils / aplot / ggimage / ggtangle / ggbreak / ggmsa / ivolcano / tigeR /
wikiprofiler / epiSeeker / scholar / seqmagick / TCNMDATA ...

数据源：<BUILD>/<pkg>/{NAMESPACE, DESCRIPTION, R/*.R}

产出（按 env 合并，可由 build_all.py 一次生成）：
  <BUILD>/<pkg>/raw/api_full.json   ← 单包事实
  <SKILL_DIR>/tools/whitelist.json  ← 合并后的总白名单

支持参数：
  python3 build_api.py                       默认只构建 clusterProfiler
  python3 build_api.py --pkg NAME           单包
  python3 build_api.py --pkg NAME --pkg NAME 多个
  python3 build_api.py --all                全部 PACKAGES
  python3 build_api.py --merge              合并所有 pkg 输出到 whitelist.json

特别处理：
  1. R 文件里 `name <- function(...)`、`name = function(...)`、`setMethod(...)` 三种定义。
  2. `name <- alias` / `name = alias` 是别名赋值，复用 alias 的 formals。
  3. importFrom 的第三方包函数：进 whitelist（保证 cp_lint 不报幻觉）。
"""
import io, os, re, json, sys

# ---- 路径 ----
_HERE = os.path.dirname(os.path.abspath(__file__))        # tools/etl
SKILL_DIR = os.path.dirname(os.path.dirname(_HERE))       # skill 根目录
BUILD_DIR = os.path.abspath(os.environ.get(
    "CP_BUILD_DIR", os.path.join(SKILL_DIR, ".build")))
WHITELIST_PATH = os.path.join(SKILL_DIR, "tools", "whitelist.json")
os.makedirs(BUILD_DIR, exist_ok=True)


# ================ 通用 R 解析 ================

def strip_comments(s):
    out, inq = [], None
    i, n = 0, len(s)
    while i < n:
        ch = s[i]
        if inq:
            out.append(ch)
            if ch == inq:
                inq = None
            i += 1
            continue
        if ch in "\"'":
            inq = ch; out.append(ch); i += 1; continue
        if ch == "#":
            while i < n and s[i] != "\n":
                i += 1
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def split_args(argstr):
    argstr = strip_comments(argstr)
    args_out, depth, cur, inq = [], 0, [], None
    for ch in argstr:
        if inq:
            cur.append(ch)
            if ch == inq:
                inq = None
            continue
        if ch in "\"'":
            inq = ch; cur.append(ch); continue
        if ch == "`":
            inq = "`"; cur.append(ch); continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == "," and depth == 0:
            args_out.append("".join(cur)); cur = []; continue
        cur.append(ch)
    if "".join(cur).strip():
        args_out.append("".join(cur))
    out = []
    for a in args_out:
        a = a.strip()
        if not a:
            continue
        if "=" in a:
            n, d = a.split("=", 1)
            out.append((n.strip(), d.strip()))
        else:
            out.append((a, None))
    return out


FN_RE = re.compile(r"(?P<name>[\w.]+)\s*(?:<-|=)\s*function\s*\(", re.M)
ALIAS_RE = re.compile(
    r"(?P<name>[\w.]+)\s*(?:<-|=)\s*(?P<alias>[A-Za-z][A-Za-z0-9._]*)\s*$",
    re.M,
)
S4_RE = re.compile(
    r"setMethod\s*\(\s*\"(?P<gen>[\w.<>-]+)\"\s*,\s*"
    r"(?P<sig>[^,]+),\s*function\s*\(\s*(?P<args>[^)]*)\)",
    re.S,
)


def parse_r(path, rel):
    try:
        src = io.open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return {}
    res = {}
    for m in FN_RE.finditer(src):
        name = m.group("name")
        if name in res:
            continue
        start = m.end() - 1
        depth, i, n, inq = 0, start, len(src), None
        while i < n:
            ch = src[i]
            if inq:
                if ch == inq:
                    inq = None
                i += 1; continue
            if ch in "\"'":
                inq = ch; i += 1; continue
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        if i >= n:
            continue
        argstr = src[start + 1:i]
        try:
            args = split_args(argstr)
        except Exception:
            args = []
        line_no = src[:m.start()].count("\n") + 1
        res[name] = {
            "file": rel, "line": line_no,
            "args": [{"name": a, "default": b} for a, b in args],
        }
    for m in S4_RE.finditer(src):
        gen = m.group("gen")
        sig = m.group("sig")
        cls = re.findall(r'"([^"]+)"', sig) or re.findall(r"'([^']+)'", sig)
        cls_name = cls[0] if cls else ""
        key = "%s.%s" % (gen, cls_name) if cls_name else gen
        if key in res:
            continue
        argstr = m.group("args")
        try:
            args = split_args(argstr)
        except Exception:
            args = []
        line_no = src[:m.start()].count("\n") + 1
        res[key] = {
            "file": rel, "line": line_no,
            "args": [{"name": a, "default": b} for a, b in args],
            "s4method": True, "generic": gen, "class": cls_name,
        }
    for am in ALIAS_RE.finditer(src):
        a_name = am.group("name")
        a_alias = am.group("alias")
        if a_name in res:
            continue
        if a_alias in res:
            d = res[a_alias]
            res[a_name] = {
                "file": d["file"], "line": d["line"],
                "args": [dict(a) for a in d["args"]],
                "alias_of": a_alias,
            }
    return res


# ================ 第三方包函数的已知 formals（手工核对） ================
# 生态包互 re-export（如 clusterProfiler 通过 importFrom 把 enrichplot 的函数
# re-export 出来）。本技能不去抓那些被 re-export 包的源码，但用已核对过的
# formals 填进 args，保证 cp_lint 不误报 unknown-arg。
THIRD_PARTY_PARAMS = {
    # enrichplot
    "dotplot": ["object", "x", "color", "showCategory", "size", "split",
                 "font.size", "title", "label_format", "orderBy",
                 "decreasing", "xlim", "ylim"],
    "cnetplot": ["x", "layout", "showCategory", "color_category",
                  "size_category", "color_item", "size_item", "color_edge",
                  "size_edge", "categorySizeBy", "node_label", "node_label_size",
                  "foldChange", "fc_threshold", "hilight", "hilight_alpha",
                  # 兼容别名（被 normalize_legacy_* 翻译）
                  "categorySize", "colorEdge", "circular", "pie", "split",
                  "includeAll"],
    "emapplot": ["x", "showCategory", "color", "layout", "cex_category",
                  "cex_line", "min_edge", "group_category"],
    "gseaplot": ["x", "geneSetID", "by", "type", "color", "title"],
    "goplot": ["x", "showCategory", "color", "size"],
    "heatplot": ["x", "showCategory", "foldChange"],
    "ridgeplot": ["x", "showCategory", "label_format"],
    # magrittr
    "%>%": ["lhs", "rhs"],
    "%<>%": ["lhs", "rhs"],
    # rlang
    "%||%": ["lhs", "rhs"],
    # aisdk
    "Agent": ["description", "name", "model"],
    "ChatSession": ["agent"],
    "generate_object": ["session", "schema"],
    "z_string": [], "z_enum": ["values"], "z_array": ["items"], "z_object": ["fields"],
    # yulab.utils
    "download_yulab_file": ["url", "destfile"],
    "get_cache": ["dir"], "get_cache_item": ["key"],
    "get_fun_from_pkg": ["pkg", "fun"], "is.installed": ["pkg"],
    "load_OrgDb": ["OrgDb"], "user_dir": ["appname"],
    "yread": ["file"], "yread_tsv": ["file"],
    # AnnotationDbi
    "Ontology": ["object"], "keys": ["x"], "keytypes": ["x"],
    "toTable": ["x"], "mappedkeys": ["x"], "mget": ["x"],
    # GOSemSim
    "buildGOmap": ["gostats"], "get_organism": ["db"],
    "godata": ["ont", "organism"], "mgoSim": ["GO1", "GO2"],
    "read.blast2go": ["file"], "read.gaf": ["file"],
    # gson
    "gson": ["gsid2gene", "gsid2name"],
    "read.gmt": ["gmtfile"], "read.gmt.wp": ["gmtfile"],
    # utils
    "head": ["x"], "tail": ["x"],
    # ggplot2 (limited)
    "ggplot": ["data", "mapping"],
    "aes": ["x", "y"],
    "scale_color_manual": ["values"],
    # msigdbr
    "msigdbr": ["species", "category", "subcategory"],
    # simplify (enrichplot::simplify.enrichResult 的 S3 dispatch 入口)
    "simplify": ["object", "cutoff", "by", "select_fun", "measure", "semData"],
    # enrichit 网络构建函数
    "build_kegg_graph": ["organism"],
    "build_string_graph": ["taxID"],
    "build_go_graph": ["ont", "organism"],
    "prepare_network": ["graph"],
    "prepare_multilayer_network": ["graphs"],
    # igraph
    "layout_with_kk": [],
    "layout_nicely": [],
    "layout_in_circle": [],
}


# ================ 1. 解析 R source ================

def parse_pkg(pkg):
    """解析单个包。返回 (functions_dict, version_str, raw_data_dict)。"""
    src_dir = os.path.join(BUILD_DIR, pkg)
    rdir = os.path.join(src_dir, "R")
    ns = os.path.join(src_dir, "NAMESPACE")
    desc = os.path.join(src_dir, "DESCRIPTION")
    if not os.path.isfile(ns):
        raise FileNotFoundError("NAMESPACE 不存在: %s (请先跑 fetch_sources.py)" % ns)
    ns_text = io.open(ns, encoding="utf-8").read()

    # R sources
    fns = {}
    if os.path.isdir(rdir):
        for fn in sorted(os.listdir(rdir)):
            if fn.endswith(".R"):
                fns.update(parse_r(os.path.join(rdir, fn), fn))

    # NAMESPACE: export / S3method / exportClasses / exportMethods / importFrom
    def parse_export(text):
        out = []
        for m in re.finditer(r"^export\(\s*([^)]*)\)", text, re.M):
            inner = m.group(1)
            if inner.startswith('"'):
                out.append(inner.strip('"'))
            else:
                out += [x.strip() for x in inner.split(",") if x.strip()]
        return sorted(set(out))

    pkg_exports = [x.strip('"') for x in parse_export(ns_text)]

    s3 = []
    for m in re.finditer(r'^S3method\(\s*"?([\w.<\-]+)"?\s*,\s*"?([\w.]+)"?', ns_text, re.M):
        s3.append({"generic": m.group(1), "class": m.group(2)})

    s4cls = []
    for m in re.finditer(r"^exportClasses\(([^)]*)\)", ns_text, re.M):
        s4cls += [x.strip().strip('"') for x in m.group(1).split(",") if x.strip()]

    exported_methods = []
    for m in re.finditer(r"^exportMethods\(\s*([^)]+?)\s*\)", ns_text, re.M):
        for tok in m.group(1).split(","):
            tok = tok.strip().strip('"')
            if tok:
                exported_methods.append(tok)

    imports = {}
    for m in re.finditer(r"^importFrom\(([^,]+),\s*([\s\S]*?)\)\s*$", ns_text, re.M):
        p = m.group(1).strip().strip('"')
        fns_in = [x.strip() for x in m.group(2).split(",") if x.strip()]
        imports.setdefault(p, []).extend(fns_in)

    # find_def
    def find_def(name, table):
        if name in table:
            d = table[name]
            if d.get("alias_of") and d["alias_of"] in table:
                return d["alias_of"], table[d["alias_of"]]
            return name, d
        if name.endswith("<-"):
            base = name[:-2]
            for suf in (".enrichResult", ".compareClusterResult", ".gseaResult",
                        ".data.frame", ".default", ".list"):
                cand = base + suf
                if cand in table:
                    return cand, table[cand]
        for suf in (".default", ".enrichResult", ".compareClusterResult",
                    ".gseaResult", ".groupGOResult", ".interpretation"):
            cand = name + suf
            if cand in table:
                return cand, table[cand]
        return None, None

    # 组装 exports
    records = {}
    for name in pkg_exports:
        key, d = find_def(name, fns)
        rec = {"name": name, "pkg": pkg, "kind": "function", "def": key}
        if d:
            rec["file"] = d["file"]; rec["line"] = d["line"]
            rec["args"] = d["args"]
        else:
            rec["file"] = None; rec["line"] = None; rec["args"] = []
        records[name] = rec

    # S3 method -> generic
    for item in s3:
        g, c = item["generic"], item["class"]
        cand = "%s.%s" % (g, c)
        if cand in fns:
            if g in records and not records[g]["args"]:
                records[g]["args"] = fns[cand]["args"]
                records[g]["def"] = cand
                records[g]["file"] = fns[cand]["file"]

    # S3 method dispatch 参数并入 generic
    def merge_args(lists):
        idx, out = {}, []
        for al in lists:
            for a in al:
                n = a["name"]
                if n == "...":
                    continue
                if n not in idx:
                    idx[n] = dict(a); out.append(n)
                elif idx[n].get("default") is None and a.get("default") is not None:
                    idx[n] = dict(a)
        if any(any(a["name"] == "..." for a in al) for al in lists):
            idx["..."] = {"name": "...", "default": None}
            out.append("...")
        return [idx[n] for n in out]

    def collect_generic_args(table):
        g = {}
        for fname, d in table.items():
            if "." not in fname:
                continue
            gen, cls = fname.rsplit(".", 1)
            if not gen or not cls:
                continue
            g.setdefault(gen, {})[cls] = d["args"]
        return g

    gen_from = collect_generic_args(fns)
    s3_generics = sorted({x["generic"] for x in s3})

    for gen, variants in gen_from.items():
        if gen not in records:
            if gen not in s3_generics:
                continue
            records[gen] = {"name": gen, "pkg": pkg, "kind": "generic",
                            "def": None, "file": None, "line": None, "args": []}
        chosen = None
        for pref in ("default", "enrichResult", "compareClusterResult",
                     "gseaResult", "groupGOResult"):
            if pref in variants and variants[pref]:
                chosen = variants[pref]; break
        if chosen is None:
            chosen = merge_args(list(variants.values()))
        merged = merge_args([chosen] + list(variants.values()))
        if merged:
            r = records[gen]
            if len(merged) > len(r["args"]):
                r["args"] = merged
                r["variants"] = sorted(variants.keys())

    # 4d. exportMethods(...) 暴露的 S4 method（用户写 simplify(x) 合法）
    for mname in exported_methods:
        if mname in records:
            continue
        records[mname] = {
            "name": mname, "pkg": pkg, "kind": "s4method",
            "def": None, "file": None, "line": None, "args": [],
        }

    # 4e. importFrom 的所有函数（re-export）
    # 用 THIRD_PARTY_PARAMS（手工核对过的 formals）填充 args。
    # 跨包 re-export（如 clusterProfiler::dotplot 来自 enrichplot::dotplot）的关键。
    for p, fns_in in imports.items():
        for fn in fns_in:
            name = fn.strip().strip('"')
            if not name:
                continue
            params = THIRD_PARTY_PARAMS.get(name)
            arg_records = (
                [{"name": a, "default": None} for a in params if a != "..."]
                if params else []
            )
            if name in records:
                r = records[name]
                if not r.get("args") and arg_records:
                    r["args"] = arg_records
                r["pkg"] = p
                r["kind"] = "reexport"
            else:
                records[name] = {
                    "name": name, "pkg": p, "kind": "reexport",
                    "def": None, "file": None, "line": None,
                    "args": arg_records,
                }

    # version
    def read_ver(p):
        if not os.path.exists(p):
            return "?"
        d = io.open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r"^Version:\s*(\S+)", d, re.M)
        return m.group(1) if m else "?"

    ver = read_ver(desc)

    s4methods = [{"generic": d["generic"], "class": d["class"], "key": fname}
                 for fname, d in fns.items() if d.get("s4method")]

    return records, ver, {
        "s3methods": s3, "s4classes": s4cls, "s4methods": s4methods,
        "imports": {k: sorted(set(v)) for k, v in imports.items()},
        "internal_functions": sorted(fns.keys()),
    }


def build_one(pkg, write_pkg_raw=True):
    """解析单个包，输出 raw/<pkg>/api_full.json"""
    print("=== [%s] ===" % pkg)
    try:
        recs, ver, raw = parse_pkg(pkg)
    except Exception as e:
        print("  !! 解析失败：%s" % str(e)[:120])
        return None

    pkg_raw = os.path.join(BUILD_DIR, pkg, "raw")
    os.makedirs(pkg_raw, exist_ok=True)
    if write_pkg_raw:
        data = {
            "package": pkg, "version": ver,
            "functions": recs,
            "s3methods": raw["s3methods"],
            "s4classes": raw["s4classes"],
            "s4methods": raw["s4methods"],
            "imports": raw["imports"],
            "internal_functions": raw["internal_functions"],
        }
        with io.open(os.path.join(pkg_raw, "api_full.json"), "wb") as f:
            f.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    # 统计
    n_sig = sum(1 for r in recs.values() if r["args"])
    n_pkg = {}
    for r in recs.values():
        n_pkg[r.get("pkg", "?")] = n_pkg.get(r.get("pkg", "?"), 0) + 1
    print("  version: %s, total symbols: %d, with formals: %d" % (ver, len(recs), n_sig))
    for k, v in sorted(n_pkg.items(), key=lambda x: -x[1]):
        print("    %-25s %d" % (k, v))
    return recs, ver, raw


def _inject_third_party(all_symbols):
    """把 THIRD_PARTY_PARAMS 里所有函数注入 all_symbols。

    一些函数（如 msigdbr / build_kegg_graph / ggplot2::geom_point）虽然不在
    clusterProfiler 的 importFrom 里，但用户脚本里照样会调用。手动归好类。
    """
    added = 0
    for name, params in THIRD_PARTY_PARAMS.items():
        # 已有更完整的版本就不覆盖
        if name in all_symbols and len(all_symbols[name].get("args", [])) >= len(params):
            continue
        if name.startswith("msigdbr"):
            ecosystem_pkg, module = "msigdbr", "util"
        elif name in ("layout_with_kk", "layout_nicely", "layout_in_circle"):
            ecosystem_pkg, module = "igraph", "viz"
        elif name.startswith("build_") or name.startswith("prepare_"):
            ecosystem_pkg, module = "enrichit", "gsea"
        elif name in ("Agent", "ChatSession", "generate_object", "z_string",
                     "z_enum", "z_array", "z_object"):
            ecosystem_pkg, module = "aisdk", "llm"
        elif name in ("%>%", "%<>%"):
            ecosystem_pkg, module = "magrittr", "dplyr"
        elif name == "%||%":
            ecosystem_pkg, module = "rlang", "dplyr"
        elif name in ("ggplot", "aes", "geom_point", "geom_label", "scale_color_manual",
                     "theme", "theme_void") or name.startswith("scale_"):
            ecosystem_pkg, module = "ggplot2", "viz"
        elif name in ("head", "tail", "read.table", "read.csv", "write.table",
                     "installed.packages", "browseURL", "citation", "packageDescription"):
            ecosystem_pkg, module = "utils", "util"
        elif name in ("Ontology", "keys", "keytypes", "toTable", "mappedkeys", "mget"):
            ecosystem_pkg, module = "AnnotationDbi", "id"
        elif name in ("godata", "mgoSim", "buildGOmap", "get_organism", "read.blast2go",
                     "read.gaf"):
            ecosystem_pkg, module = "GOSemSim", "semantic"
        elif name in ("gson", "read.gmt", "read.gmt.wp"):
            ecosystem_pkg, module = "gson", "db"
        elif name in ("yread", "yread_tsv", "get_cache", "get_cache_item",
                     "download_yulab_file", "get_fun_from_pkg", "is.installed",
                     "load_OrgDb", "user_dir"):
            ecosystem_pkg, module = "yulab.utils", "util"
        elif name.startswith("dotplot") or name in ("cnetplot", "emapplot",
                                                    "gseaplot", "goplot",
                                                    "heatplot", "ridgeplot"):
            ecosystem_pkg, module = "enrichplot", "viz"
        else:
            ecosystem_pkg, module = "third_party", "reexport"
        arg_names = [a for a in params if a != "..."] if params else []
        rec = {
            "name": name, "pkg": ecosystem_pkg, "kind": "reexport",
            "def": None, "file": None, "line": None,
            "args": arg_names,
            "ecosystem_pkg": ecosystem_pkg,
            "ecosystem_module": module,
            "module": module,
        }
        all_symbols[name] = rec
        full_name = "%s::%s" % (ecosystem_pkg, name)
        if full_name not in all_symbols:
            all_symbols[full_name] = dict(rec)
        added += 1
    return added


def merge_all_whitelist():
    """合并所有 pkg 的 raw/<pkg>/api_full.json 到 tools/whitelist.json"""
    # 复用 fetch_sources.py 的 PACKAGES 字典
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import fetch_sources as fs

    all_symbols = {}
    pkg_versions = {}
    all_s3, all_s4classes, all_s4methods = [], [], []

    # 把 THIRD_PARTY_PARAMS 里所有函数注入 all_symbols
    third_party_added = _inject_third_party(all_symbols)
    for pkg in fs.PACKAGES:
        p = os.path.join(BUILD_DIR, pkg, "raw", "api_full.json")
        if not os.path.exists(p):
            print("  skip %s (no raw)" % pkg)
            continue
        d = json.loads(io.open(p, encoding="utf-8").read())
        pkg_versions[pkg] = d.get("version", "?")
        for sym, rec in d.get("functions", {}).items():
            # 用包名 + sym 作为唯一键（不同包可能有同名函数）
            full_name = "%s::%s" % (pkg, sym)
            r = dict(rec)
            r["ecosystem_pkg"] = pkg
            r["ecosystem_module"] = guess_module(pkg, sym, rec)
            r["module"] = r["ecosystem_module"]   # 兼容旧字段
            # args 统一为 list of str（cp_lint 期望）
            if isinstance(r.get("args"), list) and r["args"] and isinstance(r["args"][0], dict):
                r["args"] = [a.get("name") for a in r["args"]]
            # 也保留原 list of dict 用于 references/docs 生成
            r["args_full"] = d["functions"][sym].get("args", [])
            all_symbols[full_name] = r
            # 短名：优先选 args 最多的版本（避免某包只有空 args 占位）
            n_args = len(r["args"])
            if sym not in all_symbols:
                all_symbols[sym] = dict(r)
            elif len(all_symbols[sym].get("args", [])) < n_args:
                # 现存短名 args 更少，用这个更完整的替换
                # 注意：保留原 short_name 其它字段，args 用新的
                all_symbols[sym]["args"] = r["args"]
                all_symbols[sym]["ecosystem_pkg"] = pkg
                all_symbols[sym]["ecosystem_module"] = r["ecosystem_module"]
        all_s3 += d.get("s3methods", [])
        all_s4classes += d.get("s4classes", [])
        all_s4methods += d.get("s4methods", [])

    wl = {
        "generated_from": {
            "format_version": "ecosystem-1.0",
            "generated_at": __import__("datetime").datetime.now().isoformat(),
            "source": "github.com/YuLab-SMU/<多个包>@devel",
            "packages": pkg_versions,
        },
        "symbols": all_symbols,
        "deprecated_args": {},
        "s3_generics": sorted({x["generic"] for x in all_s3}),
        "s4_generics": sorted({x["generic"] for x in all_s4methods}),
        "s3methods": all_s3,
        "s4methods": all_s4methods,
        "s4classes": list(set(all_s4classes)),
    }
    with io.open(WHITELIST_PATH, "wb") as f:
        f.write(json.dumps(wl, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    print("\n合并 whitelist.json: %d 符号 (含包前缀: %d, 单名: %d)" %
          (len(all_symbols), sum(1 for k in all_symbols if "::" in k),
           sum(1 for k in all_symbols if "::" not in k)))
    print("  写入 %s" % WHITELIST_PATH)


# 把生态包映射到 module（用于 gen_docs.py 输出分组）
ECOSYSTEM_MODULE = {
    "clusterProfiler":    "ora",
    "enrichit":           "gsea",
    "enrichplot":         "viz",
    "gson":               "db",
    "DOSE":               "disease",
    "ReactomePA":         "reactome",
    "meshes":             "mesh",
    "GOSemSim":           "semantic",
    "ChIPseeker":         "chippeak",
    "MicrobiomeProfiler": "microbiome",
    "HDO":                "disease",
    "aPEAR":              "viz",
    "aisdk":              "llm",
    "yulab.utils":        "util",
    "ggtree":             "phylo",
    "treeio":             "phylo",
    "ggtreeExtra":        "phylo",
    "tidytree":           "phylo",
    "MicrobiotaProcess":  "microbiome",
    "SVP":                "spatial",
    "sclet":              "singlecell",
    "scMSGNN":            "singlecell",
    "ggsc":               "spatial",
    "createKEGGdb":      "db",
    "CNEr":                "chippeak",
    "aplot":              "viz",
    "ggimage":            "viz",
    "ggtangle":           "viz",
    "ggbreak":            "viz",
    "ggmsa":              "viz",
    "ivolcano":           "viz",
    "tigeR":              "disease",
    "wikiprofiler":       "wiki",
    "epiSeeker":          "epigenomic",
    "scholar":            "util",
    "seqmagick":          "util",
    "TCMDATA":            "tcm",
}


def guess_module(pkg, sym, rec):
    """Guess a module tag."""
    return ECOSYSTEM_MODULE.get(pkg, "misc")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--pkg", action="append", default=[],
                    help="要解析的包名（可多次）。缺省: clusterProfiler")
    ap.add_argument("--all", action="store_true", help="全部 PACKAGES")
    ap.add_argument("--merge", action="store_true",
                    help="把 raw/<pkg>/api_full.json 合并到 tools/whitelist.json")
    ap.add_argument("--list", action="store_true", help="列出 PACKAGES")
    a = ap.parse_args()

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import fetch_sources as fs

    if a.list:
        for k, v in fs.PACKAGES.items():
            print("%-22s %s" % (k, v))
        return 0

    targets = []
    if a.all:
        targets = list(fs.PACKAGES)
    elif a.pkg:
        for k in a.pkg:
            if k in fs.PACKAGES:
                targets.append(k)
            else:
                print("WARN: 未知包 `%s`" % k)
    else:
        targets = ["clusterProfiler"]

    n_ok = 0
    for pkg in targets:
        if build_one(pkg) is not None:
            n_ok += 1

    print("\n===== 解析 %d/%d 包成功 =====" % (n_ok, len(targets)))

    if a.merge or a.all:
        merge_all_whitelist()


if __name__ == "__main__":
    sys.exit(main())