# -*- coding: utf-8 -*-
"""生成 clusterprofiler-skill 的事实文件：
  - references/api-signatures.md   全量函数真实签名（可 grep）
  - references/function-index.md   按模块分类的索引
  - tools/whitelist.json           供 cp_lint.py 做函数/参数存在性校验

数据来自 tools/etl/build_api.py 写出的 .build/raw/api_full.json。
"""
import io, os, json, re

_HERE = os.path.dirname(os.path.abspath(__file__))        # tools/etl
SKILL = os.path.dirname(os.path.dirname(_HERE))           # skill 根目录
RAW = os.path.abspath(os.environ.get(
    "CP_RAW", os.path.join(SKILL, ".build", "raw")))
os.makedirs(os.path.join(SKILL, "references"), exist_ok=True)
os.makedirs(os.path.join(SKILL, "tools"), exist_ok=True)

d = json.loads(io.open(os.path.join(RAW, "api_full.json"), encoding="utf-8").read())
fns = d["functions"]

# ---------------- 模块分类 ----------------
# 基于 clusterProfiler 的 R 源文件做映射；未命中的按定义文件兜底
TAG = {}


def tagmany(names, t):
    for n in names:
        TAG[n] = t


# ORA 核心
tagmany("""enrichGO enrichKEGG enrichWP enrichMKEGG enrichPC enrichDAVID
enricher compareCluster""".split(), "ora")
# GSEA
tagmany("""GSEA gseGO gseKEGG gseWP gseMKEGG gsePC
nseGO nseKEGG nseWP nseMKEGG mnseGO mnseKEGG mnseWP mnseMKEGG
bayes_enrich bayes_summary aggregate_enrichment aggregate_omics
select_features_for_ora""".split(), "gsea")
# ID 转换与位点
tagmany("""bitr bitr_kegg Gff2GeneTable read.blast2go read.gaf
harmonize_ids setReadable idType go2ont go2term ko2name
getTaxID getTaxInfo get_organism get_wp_organisms""".split(), "id")
# 数据库与 GSON
tagmany("""gson_GO gson_GO_local gson_KEGG gson_KEGG_mapper gson_KO gson_WP
read.gmt read.gmt.pc read.gmt.wp download_KEGG search_kegg_organism
append_kegg_category""".split(), "db")
# GO 工具
tagmany("""groupGO add_go_level gofilter dropGO buildGOmap""".split(), "go")
# 比较与合并
tagmany("""merge_result simplify""".split(), "manip")
# 可视化
tagmany("""dotplot cnetplot emapplot gseaplot goplot heatplot ridgeplot
browseKEGG plotGOgraph""".split(), "viz")
# 蛋白互作与外部数据
tagmany("""getPPI get_ppi get_ppi_network uniprot_get""".split(), "external")
# LLM 解读
tagmany("""interpret interpret_agent interpret_hierarchical""".split(), "llm")
# dplyr 风格的 dplyr verbs（enrichResult 等 S3 method）
tagmany("""arrange filter group_by mutate rename select slice summarise n""".split(),
        "dplyr")
# 文件兜底
FILE_TAG = {
    "enrichGO.R": "ora",
    "enrichKEGG.R": "ora",
    "enrichWP.R": "ora",
    "wikiPathways.R": "ora",
    "enrichMKEGG.R": "ora",
    "enrichPC.R": "ora",
    "pathwayCommons.R": "ora",
    "enrichDAVID.R": "ora",
    "enricher.R": "ora",
    "compareCluster.R": "ora",
    "gseAnalyzer.R": "gsea",
    "nseaAnalyzer.R": "gsea",
    "enrichit.R": "gsea",
    "bitr.R": "id",
    "GFFparser.R": "id",
    "gson.R": "db",
    "kegg-utilities.R": "db",
    "go-utilities.R": "go",
    "groupGO.R": "go",
    "gofilter.R": "go",
    "simplify.R": "manip",
    "merge_result.R": "manip",
    "enrichplot.R": "viz",
    "plotGOgraph.R": "viz",
    "plot_interpret.R": "viz",
    "interpret.R": "llm",
    "taxa.R": "external",
    "ppi.R": "external",
    "uniprot.R": "external",
    "accessor.R": "manip",
    "utilities.R": "util",
    "data.R": "data",
    "AllGenerics.R": "generic",
    "reexports.R": "reexport",
    "zzz.R": "init",
    "clusterProfiler-package.R": "init",
    "dplyr-arrange.R": "dplyr", "dplyr-filter.R": "dplyr",
    "dplyr-group_by.R": "dplyr", "dplyr-mutate.R": "dplyr",
    "dplyr-rename.R": "dplyr", "dplyr-select.R": "dplyr",
    "dplyr-slice.R": "dplyr", "dplyr-summarise.R": "dplyr",
}
for name, r in fns.items():
    # 1) re-exported 函数（来自第三方包的 importFrom）：强制归到 reexport 模块
    if r.get("kind") == "reexport":
        TAG[name] = "reexport"
        continue
    # 2) 显式表
    if name in TAG:
        continue
    # 3) 文件兜底
    f = r.get("file") or ""
    TAG[name] = FILE_TAG.get(f, "misc")

MODULES = [
    ("ora", "过表示分析 ORA（GO / KEGG / WikiPathways / Module / PathwayCommons / DAVID / 通用 enricher）"),
    ("gsea", "GSEA / NSEA / 拓扑感知 / 贝叶斯"),
    ("id", "基因 ID 转换与位点注释"),
    ("db", "数据库 / GSON / KEGG 下载"),
    ("go", "GO 工具（groupGO / gofilter / dropGO / buildGOmap）"),
    ("manip", "结果操作（merge_result / simplify）"),
    ("viz", "可视化（dotplot/cnetplot/emapplot/gseaplot/heatmap/ridgeplot/goplot）"),
    ("external", "外部数据（PPI / Uniprot / Taxa）"),
    ("llm", "LLM 解读（interpret / interpret_agent / interpret_hierarchical）"),
    ("dplyr", "dplyr 风格 S3 method（arrange/filter/group_by/mutate/...）"),
    ("reexport", "第三方包 re-export（enrichplot/dplyr/magrittr/...）"),
    ("generic", "S3 / S4 generic"),
    ("data", "内嵌数据"),
    ("util", "通用工具"),
    ("init", "包初始化 / 文档"),
    ("misc", "其他"),
]


def fmt_args(args, maxlen=40):
    out = []
    for a in args:
        n = a["name"]
        dv = a["default"]
        if dv is None:
            out.append(n)
        else:
            dv = " ".join(dv.split())
            if len(dv) > maxlen:
                dv = dv[:maxlen - 3] + "..."
            out.append("%s=%s" % (n, dv))
    return ", ".join(out)


# ---------------- 生成 api-signatures.md ----------------
lines = []
lines.append("# clusterProfiler 全量函数签名库（自源码提取，非文档转述）")
lines.append("")
lines.append("> 数据源：github.com/YuLab-SMU/clusterProfiler `devel`（clusterProfiler %s）。"
            % d["clusterprofiler_version"])
lines.append("> 每条签名由 `R/` 源码的真实 `formals` 解析得到；")
lines.append("> 第三方包 re-export（enrichplot/dplyr/magrittr/...）的参数表为手工核对（标注 pkg）。")
lines.append("> S3 generic 取其全部 method 参数的并集。")
lines.append("")
lines.append("> 用法：`grep -n \"^### <函数名>\" references/api-signatures.md` 精确查，不要整篇读。")
lines.append("")
lines.append("共 %d 个已知符号，其中 %d 个解析到真实参数表。"
            % (len(fns), sum(1 for r in fns.values() if r["args"])))
lines.append("")

bymod = {}
for name, r in fns.items():
    bymod.setdefault(TAG[name], []).append(name)

for mod, title in MODULES:
    names = sorted(bymod.get(mod, []), key=lambda x: x.lower())
    if not names:
        continue
    lines.append("")
    lines.append("## MODULE: %s — %s（%d）" % (mod, title, len(names)))
    lines.append("")
    for name in names:
        r = fns[name]
        sig = fmt_args(r["args"])
        src = r.get("file") or "—"
        pkg = r.get("pkg", "?")
        defn = r.get("def") or "—"
        lines.append("### %s" % name)
        lines.append("`%s(%s)`" % (name, sig if sig else "?"))
        lines.append("")
        lines.append("- 来源：`%s` · 包：%s · 实现：%s" % (src, pkg, defn))
        if r.get("variants"):
            lines.append("- 方法变体：%s" % ", ".join("`*%s*`" % v for v in r["variants"][:12]))
        lines.append("")


# ---------------- 生成 function-index.md ----------------
idx = []
idx.append("# clusterProfiler 函数分类索引")
idx.append("")
idx.append("版本：clusterProfiler %s。用于快速定位「该用哪个函数」；签名查 `api-signatures.md`。"
           % d["clusterprofiler_version"])
idx.append("")
idx.append("| 模块 | 函数 |")
idx.append("| --- | --- |")
for mod, title in MODULES:
    names = sorted(bymod.get(mod, []), key=lambda x: x.lower())
    if not names:
        continue
    idx.append("| **%s** %s | %s |" %
               (mod, title, ", ".join("`%s`" % n for n in names)))
idx.append("")
idx.append("## S3 method 覆盖（%d 条）" % len(d["s3methods"]))
idx.append("")
idx.append("形如 `generic.class`；调用时写 `generic(obj, ...)` 由 R 自动分派。")
idx.append("")
gens = {}
for x in d["s3methods"]:
    gens.setdefault(x["generic"], []).append(x["class"])
idx.append("| generic | 支持的方法类 |")
idx.append("| --- | --- |")
for g in sorted(gens, key=lambda x: x.lower()):
    idx.append("| `%s` | %s |" % (g, ", ".join("`%s`" % c for c in sorted(gens[g]))))
idx.append("")
idx.append("## S4 method 覆盖（%d 条）" % len(d["s4methods"]))
idx.append("")
idx.append("形如 `setMethod(\"generic\", signature(class=\"...\"), function(...) {})`，"
           "用户脚本里通常不直接写它，但 S3 dispatch 实际会命中这些实现。")
idx.append("")
s4_gens = {}
for x in d["s4methods"]:
    s4_gens.setdefault(x["generic"], []).append(x["class"])
idx.append("| generic | 支持的方法类 |")
idx.append("| --- | --- |")
for g in sorted(s4_gens, key=lambda x: x.lower()):
    idx.append("| `%s` | %s |" % (g, ", ".join("`%s`" % c for c in sorted(s4_gens[g]))))
idx.append("")
idx.append("## S4 类（%d）" % len(d["s4classes"]))
idx.append("")
idx.append(", ".join("`%s`" % c for c in sorted(set(d["s4classes"]))))
idx.append("")
idx.append("## 第三方包 re-export（按包汇总，%d 包 / %d 函数）" %
           (len(d["imports"]), sum(len(v) for v in d["imports"].values())))
idx.append("")
for pkg in sorted(d["imports"]):
    idx.append("- **%s**（%d）：%s" % (pkg, len(d["imports"][pkg]),
                                       ", ".join("`%s`" % fn for fn in d["imports"][pkg][:25])))
idx.append("")


def w(path, text):
    with io.open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    print("written", path, len(text), "chars")


w(os.path.join(SKILL, "references", "api-signatures.md"), "\n".join(lines))
w(os.path.join(SKILL, "references", "function-index.md"), "\n".join(idx))

# ---------------- whitelist.json ----------------
DEPRE_TIPS = {
    # 未来 clusterProfiler 可能弃用的参数名；当前版本暂无系统级 deprecated()
}
deprecated = {}
# 直接复用 build_api.py 收集的弃用参数；这里简化，只保留 warnings 类
# 由于 clusterProfiler 还没有大量 deprecated() 标记，先留空
# 等真出现弃用参数时，build_api.py 自动填充并在此处透传

wl = {
    "generated_from": {
        "clusterprofiler": d["clusterprofiler_version"],
        "source": "github.com/YuLab-SMU/clusterProfiler@devel",
        "generated_at": __import__("datetime").datetime.now().isoformat(),
    },
    "symbols": {
        n: {
            "pkg": r.get("pkg"),
            "module": TAG[n],
            "args": [a["name"] for a in r["args"]],
            "def": r.get("def"),
            "kind": r.get("kind", "function"),
        }
        for n, r in fns.items()
    },
    "deprecated_args": deprecated,
    "s3_generics": sorted({x["generic"] for x in d["s3methods"]}),
    "s4_generics": sorted({x["generic"] for x in d["s4methods"]}),
}
with io.open(os.path.join(SKILL, "tools", "whitelist.json"), "wb") as f:
    f.write(json.dumps(wl, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
print("written whitelist.json", len(wl["symbols"]), "symbols")

# 统计
print()
for mod, title in MODULES:
    print("  %-10s %d" % (mod, len(bymod.get(mod, []))))