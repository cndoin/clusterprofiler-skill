# -*- coding: utf-8 -*-
"""生成 clusterprofiler-skill 的事实文件（多包版本）。

数据源：<BUILD>/<pkg>/raw/api_full.json  （每个 Y 叔生态包一个）
产出：
  - references/api-signatures.md   按 ecosystem_pkg 分组
  - references/function-index.md   模块索引 + 跨包索引
  - references/ecosystem/<pkg>.md  每个包一份 mini 签名速查

数据流程：
  1. 读取所有 <BUILD>/<pkg>/raw/api_full.json
  2. 按 pkg_name 聚合
  3. 每个 pkg 一份 section
  4. 跨包索引（同名符号 / S3 methods）
"""
import io, os, json, sys
from collections import defaultdict

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import fetch_sources as _fs   # 权威包表（PACKAGES）+ 数据源标签
SKILL = os.path.dirname(os.path.dirname(_HERE))           # skill 根目录
BUILD_DIR = os.path.abspath(os.environ.get(
    "CP_BUILD_DIR", os.path.join(SKILL, ".build")))
RAW_DIR = os.path.join(BUILD_DIR, "raw")                  # 单包 raw（如有）
ECOSYSTEM_RAW_DIR = BUILD_DIR                            # <pkg>/raw/api_full.json
REFS_DIR = os.path.join(SKILL, "references")
ECOSYSTEM_DIR = os.path.join(REFS_DIR, "ecosystem")
WHITELIST_PATH = os.path.join(SKILL, "tools", "whitelist.json")

os.makedirs(REFS_DIR, exist_ok=True)
os.makedirs(ECOSYSTEM_DIR, exist_ok=True)


def load_pkgs():
    """加载所有 <pkg>/raw/api_full.json。

    包名一律取 JSON 里的 `package` 字段（规范大小写），**不能用构建目录名**：
    clusterProfiler 的目录在磁盘上是小写的 `.build/clusterprofiler`（v1.0 遗留），
    用目录名会把文档写成 `ecosystem/clusterprofiler.md`，与其余文档命名风格不一致。
    Windows 文件系统大小写不敏感，这个 bug 在本机看不出来，到 Linux 才炸。

    同时丢掉已从 PACKAGES 移除的陈旧目录（如 HDO），
    避免它们的空 stub 永远留在 references/ecosystem/ 里。
    """
    pkgs = {}
    if not os.path.isdir(BUILD_DIR):
        return pkgs
    known = set(_fs.PACKAGES)
    for entry in sorted(os.listdir(BUILD_DIR)):
        raw = os.path.join(BUILD_DIR, entry, "raw", "api_full.json")
        if not os.path.exists(raw):
            continue
        d = json.loads(io.open(raw, encoding="utf-8").read())
        name = d.get("package") or entry
        if name not in known:
            sys.stderr.write("WARN: 跳过 %s（package=%s 不在 PACKAGES 里）\n"
                             % (entry, name))
            continue
        pkgs[name] = d
    return pkgs


def fmt_args(args, maxlen=40):
    out = []
    for a in args or []:
        if isinstance(a, dict):
            n = a.get("name", "?")
            dv = a.get("default")
        else:
            n = a
            dv = None
        if dv is None:
            out.append(n)
        else:
            dv = " ".join(str(dv).split())
            if len(dv) > maxlen:
                dv = dv[:maxlen - 3] + "..."
            out.append("%s=%s" % (n, dv))
    return ", ".join(out)


def gen_pkg_signatures(pkg_data, pkg_name):
    """生成单个包的 api-signatures section"""
    version = pkg_data.get("version", "?")
    fns = pkg_data.get("functions", {})
    out = []
    out.append("## %s (%s) — %d symbols" % (pkg_name, version, len(fns)))
    out.append("")
    # 按 pkg / kind 分组
    by_kind = defaultdict(list)
    for name, r in fns.items():
        by_kind[r.get("kind", "function")].append((name, r))
    for kind in ["function", "generic", "s4method", "reexport"]:
        items = sorted(by_kind.get(kind, []), key=lambda x: x[0].lower())
        if not items:
            continue
        out.append("### %s (%d)" % (kind.capitalize(), len(items)))
        for name, r in items:
            sig = fmt_args(r.get("args", []))
            out.append("- `%s(%s)` — pkg=%s" % (name, sig or "?", r.get("pkg", "?")))
        out.append("")
    return "\n".join(out)


def gen_full_api_md(pkgs):
    out = []
    out.append("# clusterprofiler-skill · 全量函数签名（按生态包分组）")
    out.append("")
    out.append("> 数据源：各包上游仓库源码（逐包见下文各节的数据源行）")
    out.append("> 每条签名由 `R/` 源码的真实 `formals` 解析得到；第三方包 re-export 函数用 THIRD_PARTY_PARAMS 手工核对。")
    out.append("> 用法：`grep -n \"^### <函数名>\"` 精确查，不要整篇读。")
    out.append("")
    n_total = sum(len(d.get("functions", {})) for d in pkgs.values())
    n_with_formals = sum(
        sum(1 for r in d.get("functions", {}).values() if r.get("args"))
        for d in pkgs.values()
    )
    out.append("涵盖 %d 个 Y 叔生态包，%d 个已知符号（其中 %d 个解析到真实参数表）。"
               % (len(pkgs), n_total, n_with_formals))
    out.append("")
    for pkg_name, d in sorted(pkgs.items()):
        out.append(gen_pkg_signatures(d, pkg_name))
    return "\n".join(out)


def gen_function_index_md(pkgs):
    """按 module 分组的索引 + 跨包同名函数"""
    out = []
    out.append("# clusterprofiler-skill · 函数分类索引")
    out.append("")
    out.append("涵盖 %d 个生态包，%d 个函数。" %
               (len(pkgs), sum(len(d.get("functions", {})) for d in pkgs.values())))
    out.append("")

    # 按 ecosystem_pkg + module 分组
    by_pkg = sorted(pkgs.keys())
    for pkg in by_pkg:
        d = pkgs[pkg]
        fns = d.get("functions", {})
        out.append("## %s (%d) — v%s" % (pkg, len(fns), d.get("version", "?")))
        out.append("")
        items = sorted(fns.items(), key=lambda x: x[0].lower())
        out.append(", ".join("`%s`" % n for n, _ in items))
        out.append("")

    # 跨包同名函数（同符号被多个包 re-export）
    out.append("## 跨包同名函数")
    out.append("")
    sym2pkgs = defaultdict(list)
    for pkg, d in pkgs.items():
        for sym in d.get("functions", {}):
            sym2pkgs[sym].append(pkg)
    cross = {s: ps for s, ps in sym2pkgs.items() if len(ps) > 1}
    if cross:
        for sym in sorted(cross, key=lambda x: x.lower()):
            out.append("- `%s` 被 %d 个包定义：%s" %
                       (sym, len(cross[sym]), ", ".join(sorted(set(cross[sym])))))
    else:
        out.append("_（无）_")
    out.append("")

    # S3 / S4 methods 跨包汇总
    s3_total = sum(len(d.get("s3methods", [])) for d in pkgs.values())
    s4_total = sum(len(d.get("s4methods", [])) for d in pkgs.values())
    out.append("## S3 / S4 methods 汇总")
    out.append("")
    out.append("- S3 method: %d 条" % s3_total)
    out.append("- S4 method: %d 条" % s4_total)
    out.append("")

    return "\n".join(out)


def gen_pkg_mini(pkg_data, pkg_name):
    """生成单个包的 mini 速查 → references/ecosystem/<pkg>.md"""
    fns = pkg_data.get("functions", {})
    out = []
    out.append("# %s — %s" % (pkg_name, pkg_data.get("version", "?")))
    out.append("")
    out.append("> 数据源：%s" % _spec_label(pkg_name))
    out.append("> %d 个已知符号" % len(fns))
    out.append("")
    # 按 kind 分
    by_kind = defaultdict(list)
    for name, r in fns.items():
        by_kind[r.get("kind", "function")].append((name, r))
    for kind in ["function", "generic", "s4method", "reexport"]:
        items = sorted(by_kind.get(kind, []), key=lambda x: x[0].lower())
        if not items:
            continue
        out.append("## %s (%d)" % (kind.capitalize(), len(items)))
        out.append("")
        for name, r in items[:80]:    # 限 80 个，避免文件过大
            sig = fmt_args(r.get("args", []))
            out.append("- `%s(%s)`" % (name, sig or "?"))
        out.append("")
    return "\n".join(out)


def _spec_label(pkg_name):
    """该包的数据源描述。优先用 fetch_sources 落下的 source.json（真实 ref）。"""
    import json as _json
    sp = os.path.join(BUILD_DIR, pkg_name, "source.json")
    if os.path.exists(sp):
        try:
            info = _json.loads(io.open(sp, encoding="utf-8").read())
            if info.get("repo"):
                return "%s @ %s" % (info["repo"], info.get("ref", "?"))
        except Exception:
            pass
    spec = _fs.PACKAGES.get(pkg_name)
    if spec is None:
        return "上游源码（详见 tools/whitelist.json）"
    if isinstance(spec, tuple):
        return "%s @ %s" % (spec[0], spec[1])
    if isinstance(spec, str) and spec.startswith("bioc:"):
        return "Bioconductor bioc/%s::%s" % (_fs.BIOC_REL, spec.split(":", 1)[1])
    return "%s @ 默认分支" % spec


def prune_ecosystem(pkgs):
    """删掉 references/ecosystem/ 里对应包已不存在的 .md（如 v1.0 残留的 TCMDATA/HDO）。"""
    removed = []
    for f in sorted(os.listdir(ECOSYSTEM_DIR)):
        if not f.endswith(".md"):
            continue
        if f[:-3] not in pkgs:
            os.remove(os.path.join(ECOSYSTEM_DIR, f))
            removed.append(f)
    return removed


def main():
    pkgs = load_pkgs()
    if not pkgs:
        print("ERROR: 找不到任何 <pkg>/raw/api_full.json")
        print("请先跑: python3 fetch_sources.py --all && python3 build_api.py --all")
        return 1

    print("加载 %d 个生态包" % len(pkgs))

    # api-signatures.md（合并所有包）
    md = gen_full_api_md(pkgs)
    p = os.path.join(REFS_DIR, "api-signatures.md")
    io.open(p, "wb").write(md.encode("utf-8"))
    print("written %s (%d chars)" % (p, len(md)))

    # function-index.md
    md = gen_function_index_md(pkgs)
    p = os.path.join(REFS_DIR, "function-index.md")
    io.open(p, "wb").write(md.encode("utf-8"))
    print("written %s (%d chars)" % (p, len(md)))

    # ecosystem/<pkg>.md
    for pkg, d in pkgs.items():
        md = gen_pkg_mini(d, pkg)
        p = os.path.join(ECOSYSTEM_DIR, pkg + ".md")
        io.open(p, "wb").write(md.encode("utf-8"))
    removed = prune_ecosystem(pkgs)
    print("written %d 个 ecosystem/<pkg>.md" % len(pkgs))
    if removed:
        print("清理陈旧 ecosystem 文档: %s" % ", ".join(removed))

    # 重新生成 whitelist.json（不再覆盖；从 build_api.py --merge 写）
    print("\nwhitelist.json 应由 build_api.py --merge 生成（包含 short + full name）")

    # 统计
    n_total = sum(len(d.get("functions", {})) for d in pkgs.values())
    n_with_formals = sum(
        sum(1 for r in d.get("functions", {}).values() if r.get("args"))
        for d in pkgs.values()
    )
    print("\n涵盖 %d 个包 / %d 个符号 / %d 个带 formals" %
          (len(pkgs), n_total, n_with_formals))
    return 0


if __name__ == "__main__":
    sys.exit(main())