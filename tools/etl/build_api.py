# -*- coding: utf-8 -*-
"""从 clusterProfiler 源码生成 skill 的事实底座。

产出：<BUILD>/raw/api_full.json
  - functions: dict[name] = {pkg, name, def, file, line, args}
  - s3methods, s4classes, s4methods
  - imports: 按 pkg 聚合的 importFrom 函数
  - internal_functions: 全部解析到的函数名（含 S4 / alias / 私有名）

数据源：<BUILD>/clusterprofiler/{NAMESPACE, DESCRIPTION, R/*.R}

特别处理：
  1. R 文件里有 `name <- function(...)`、`name = function(...)`、`setMethod(...)` 三种函数定义语法。
  3. `name <- alias` / `name = alias` 是别名赋值，复用 alias 的 formals。
  4. importFrom 的第三方包函数（enrichplot::dotplot / dplyr::filter / magrittr::%>% / ...）
     通过 NAMESPACE 间接 re-export，本技能不去抓它们源码，但把已核对的 formals
     用 THIRD_PARTY_PARAMS 注入白名单（保证 cp_lint.py 不报幻觉）。
"""
import io, os, re, json

# ---- 路径 ----
_HERE = os.path.dirname(os.path.abspath(__file__))        # tools/etl
SKILL_DIR = os.path.dirname(os.path.dirname(_HERE))       # skill 根目录
BUILD_DIR = os.path.abspath(os.environ.get(
    "CP_BUILD_DIR", os.path.join(SKILL_DIR, ".build")))
CP = os.path.abspath(os.environ.get(
    "CP_SRC", os.path.join(BUILD_DIR, "clusterprofiler")))
RAW = os.path.abspath(os.environ.get(
    "CP_RAW", os.path.join(BUILD_DIR, "raw")))
os.makedirs(RAW, exist_ok=True)


# ================ 通用 R 解析 ================

def strip_comments(s):
    """去掉 # 之后的注释，忽略字符串内的 #"""
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


# 支持 <- 和 = 两种赋值风格
FN_RE = re.compile(r"(?P<name>[\w.]+)\s*(?:<-|=)\s*function\s*\(", re.M)

# 别名赋值：name <- alias / name = alias（alias 是已存在的另一个函数名）
ALIAS_RE = re.compile(
    r"(?P<name>[\w.]+)\s*(?:<-|=)\s*(?P<alias>[A-Za-z][A-Za-z0-9._]*)\s*$",
    re.M,
)

# setMethod("gen", signature(...), function(args) {...})
S4_RE = re.compile(
    r"setMethod\s*\(\s*\"(?P<gen>[\w.<>-]+)\"\s*,\s*"
    r"(?P<sig>[^,]+),\s*function\s*\(\s*(?P<args>[^)]*)\)",
    re.S,
)


def parse_r(path, rel):
    """解析一个 R 文件，返回 {name: {file, line, args, [alias_of], [s4method]}}"""
    try:
        src = io.open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return {}
    res = {}
    # 1) name <- function(...) 或 name = function(...)
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
    # 2) setMethod("gen", signature, function(args))
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
    # 3) name <- alias / name = alias 别名
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


# ================ 1. 解析 clusterProfiler 源码 ================
rdir = os.path.join(CP, "R")
cp_fns = {}
for fn in sorted(os.listdir(rdir)):
    if fn.endswith(".R"):
        cp_fns.update(parse_r(os.path.join(rdir, fn), fn))


# ================ 2. 解析 NAMESPACE ================
ns = io.open(os.path.join(CP, "NAMESPACE"), encoding="utf-8").read()


def parse_export(text):
    out = []
    for m in re.finditer(r"^export\(\s*([^)]*)\)", text, re.M):
        inner = m.group(1)
        if inner.startswith('"'):
            out.append(inner.strip('"'))
        else:
            out += [x.strip() for x in inner.split(",") if x.strip()]
    return sorted(set(out))


cp_exports = [x.strip('"') for x in parse_export(ns)]

s3 = []
for m in re.finditer(r'^S3method\(\s*"?([\w.<\-]+)"?\s*,\s*"?([\w.]+)"?', ns, re.M):
    s3.append({"generic": m.group(1), "class": m.group(2)})

s4cls = []
for m in re.finditer(r"^exportClasses\(([^)]*)\)", ns, re.M):
    s4cls += [x.strip().strip('"') for x in m.group(1).split(",") if x.strip()]

# exportMethods(...)：clusterProfiler 把 simplify 等 S4 method 作为公开方法暴露。
# 用户脚本里写 simplify(ek) 是合法的（S4 dispatch），cp_lint 必须放行。
exported_methods = []
for m in re.finditer(r"^exportMethods\(\s*([^)]+?)\s*\)", ns, re.M):
    inner = m.group(1)
    for tok in inner.split(","):
        tok = tok.strip().strip('"')
        if tok:
            exported_methods.append(tok)

imports = {}
for m in re.finditer(r"^importFrom\(([^,]+),\s*([\s\S]*?)\)\s*$", ns, re.M):
    pkg = m.group(1).strip().strip('"')
    rest = m.group(2)
    fns = [x.strip() for x in rest.split(",") if x.strip()]
    imports.setdefault(pkg, []).extend(fns)


# ================ 3. 第三方包函数的已知参数表 ================
# clusterProfiler 通过 importFrom re-export 但不在 export() 里的函数，
# 本技能不去抓那些包源码，但记录已手工核对过的 formals，保证 cp_lint.py
# 不报幻觉。

THIRD_PARTY_PARAMS = {
    # enrichplot
    "dotplot": ["object", "x", "showCategory", "size", "title", "font.size",
                "label_format", "color", "orderBy", "decreasing", "xlim", "ylim"],
    "cnetplot": ["x", "showCategory", "foldChange", "layout", "colorEdge",
                 "nodeLabel", "cex_category", "cex_gene", "cex_label_category",
                 "cex_label_gene", "categorySize", "shadowtext", "color_category"],
    "emapplot": ["x", "showCategory", "color", "layout", "cex_category",
                 "cex_line", "min_edge", "group_category", "group_legend",
                 "node_label", "label_format"],
    "gseaplot": ["x", "geneSetID", "by", "type", "color", "title", "pvalue_table"],
    "goplot": ["x", "showCategory", "color", "size", "geom", "hi",
                "lo", "font.size"],
    "heatplot": ["x", "showCategory", "foldChange", "color", "label"],
    "ridgeplot": ["x", "showCategory", "label_format", "fill", "orderBy",
                  "decreasing", "scale_bar"],
    # magrittr
    "%>%": ["lhs", "rhs"],
    "%<>%": ["lhs", "rhs"],
    # rlang
    "%||%": ["lhs", "rhs"],
    # enrichit (clusterProfiler 的底层引擎；用户脚本里通过 enrichit::xxx 调用)
    "aggregate_enrichment": ["res_list", "method"],
    "aggregate_omics": ["x", "method", "input", "feature_type", "conflict_policy"],
    "bayes_enrich": ["x", "candidate", "n_terms", "by", "prior", "false_positive",
                       "false_negative", "n_iter", "burnin", "thin",
                       "posterior_cutoff", "seed", "verbose"],
    "bayes_summary": ["x", "active", "n"],
    "gsfilter": ["x", "by", "min", "max"],
    "harmonize_ids": ["x", "mapping", "from", "to", "collapse"],
    "select_features_for_ora": ["x", "cutoff", "by"],
    "setReadable": ["x", "OrgDb", "keyType", "toType"],
    "build_kegg_graph": ["organism"],
    "build_go_graph": ["ont", "organism"],
    "build_string_graph": ["taxID"],
    "prepare_network": ["graph", "organism"],
    "prepare_multilayer_network": ["graphs"],
    "propagate_multilayer": ["multilayer_graph"],
    "collapse_multilayer_scores": ["scores"],
    "ora": ["gene", "pathway"],
    "gsea": ["gene_list", "pathway"],
    "gseaScores": ["geneList"],
    "get_omics_contribution": ["x"],
    "classify_omics_pattern": ["x"],
    "get_mnsea_contribution": ["x"],
    "extract_mnsea_subnetwork": ["x"],
    "as_enrichResult": ["x"],
    "as_gseaResult": ["x"],
    # aisdk (LLM 解释)
    "Agent": ["description", "name", "model"],
    "ChatSession": ["agent", "user_message"],
    "generate_object": ["session", "schema", "prompt"],
    "z_string": [],
    "z_enum": ["values"],
    "z_array": ["items"],
    "z_object": ["fields"],
    # yulab.utils
    "download_yulab_file": ["url", "destfile", "method", "extra"],
    "get_cache": ["dir", "create"],
    "get_cache_item": ["key", "cache_dir"],
    "get_fun_from_pkg": ["pkg", "fun"],
    "is.installed": ["pkg"],
    "load_OrgDb": ["orgdb"],
    "user_dir": [".appname"],
    "yread": ["file"],
    "yread_tsv": ["file"],
    # AnnotationDbi
    "Ontology": ["object"],
    "keys": ["x", "k"],
    "keytypes": ["x"],
    "toTable": ["x"],
    "mappedkeys": ["x"],
    "mget": ["x", "envir", "mode", "ifnotfound"],
    # GO.db (纯数据对象，无 formals)
    # GOSemSim
    "buildGOmap": ["gostats", "db", "ont", "genome"],
    "get_organism": ["db"],
    "godata": ["ont", "organism", "db", "keytype"],
    "mgoSim": ["GO1", "GO2", "semData", "measure", "combine"],
    "read.blast2go": ["file", "format"],
    "read.gaf": ["file"],
    # gson
    "gson": ["gsid2gene", "gsid2name", "species", "gsname", "version",
             "keytype", "accessed_date", "file", "obo"],
    "read.gmt": ["gmtfile", "sep"],
    "read.gmt.wp": ["gmtfile"],
    # tidyr
    "gather": ["data", "key", "value"],
    "separate": ["data", "col", "into", "sep", "remove", "convert"],
    # stats
    "formula": [],
    "setNames": ["object", "nm"],
    # utils
    "browseURL": ["url"],
    "citation": ["package"],
    "head": ["x", "n"],
    "installed.packages": ["pkgs", "lib"],
    "modifyList": ["x", "val"],
    "packageDescription": ["pkg", "lib"],
    "read.table": ["file", "header", "sep", "quote", "dec"],
    "stack": ["x"],
    "str": ["object"],
    "tail": ["x", "n"],
    # plyr
    "dlply": [".data", ".variables", ".fun"],
    "ldply": [".data", ".fun"],
    "llply": [".data", ".fun"],
    # ggplot2
    "aes": ["x", "y"],
    "geom_label": ["mapping", "data"],
    "geom_point": ["mapping", "data"],
    "ggplot": ["data", "mapping"],
    "ggtitle": ["label"],
    "scale_color_manual": ["values"],
    "theme_void": [],
    # methods
    "is": ["object", "class2"],
    "new": ["Class"],
}


# ================ 4. 组装导出记录 ================
def find_def(name, table):
    if name in table:
        d = table[name]
        if d.get("alias_of") and d["alias_of"] in table:
            return d["alias_of"], table[d["alias_of"]]
        return name, d
    # 替换函数：name<-
    if name.endswith("<-"):
        base = name[:-2]
        for suf in (".enrichResult", ".compareClusterResult", ".gseaResult",
                    ".data.frame", ".default", ".list"):
            cand = base + suf
            if cand in table:
                return cand, table[cand]
    # 算子类：name.default
    for suf in (".default", ".enrichResult", ".compareClusterResult",
                ".gseaResult", ".groupGOResult", ".interpretation"):
        cand = name + suf
        if cand in table:
            return cand, table[cand]
    return None, None


records = {}
for name in cp_exports:
    key, d = find_def(name, cp_fns)
    rec = {"name": name, "pkg": "clusterProfiler", "kind": "function", "def": key}
    if d:
        rec["file"] = d["file"]
        rec["line"] = d["line"]
        rec["args"] = d["args"]
    else:
        rec["file"] = None; rec["line"] = None; rec["args"] = []
    records[name] = rec

# 把 exportMethods(...) 暴露的方法也加入（如果尚未存在）。
# 这类 S4 method 真实签名在 setMethod("simplify", ...) 处定义的 generic.class；
# 但用户写 simplify(ek) 会由 R 自动 dispatch，cp_lint 只要知道名字合法即可。
for mname in exported_methods:
    if mname in records:
        continue
    records[mname] = {
        "name": mname, "pkg": "clusterProfiler", "kind": "s4method",
        "def": None, "file": None, "line": None, "args": [],
    }

# S3 method 变体的参数并入对应 generic
for item in s3:
    g, c = item["generic"], item["class"]
    cand = "%s.%s" % (g, c)
    if cand in cp_fns:
        if g in records and not records[g]["args"]:
            records[g]["args"] = cp_fns[cand]["args"]
            records[g]["def"] = cand
            records[g]["file"] = cp_fns[cand]["file"]


# ================ 4b. generic 的真实参数 = S3 method 参数的并集 ================
def merge_args(list_of_arglists):
    idx, out = {}, []
    for al in list_of_arglists:
        for a in al:
            n = a["name"]
            if n == "...":
                continue
            if n not in idx:
                idx[n] = dict(a)
                out.append(n)
            else:
                if idx[n].get("default") is None and a.get("default") is not None:
                    idx[n] = dict(a)
    if any(any(a["name"] == "..." for a in al) for al in list_of_arglists):
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


gen_from_cp = collect_generic_args(cp_fns)
s3_generics = sorted({x["generic"] for x in s3})

for gen, variants in gen_from_cp.items():
    if gen not in records:
        if gen not in s3_generics:
            continue
        records[gen] = {"name": gen, "pkg": "clusterProfiler", "kind": "generic",
                        "def": None, "file": None, "line": None, "args": []}
    chosen = None
    for pref in ("default", "enrichResult", "compareClusterResult",
                 "gseaResult", "groupGOResult"):
        if pref in variants and variants[pref]:
            chosen = variants[pref]
            break
    if chosen is None:
        chosen = merge_args(list(variants.values()))
    merged = merge_args([chosen] + list(variants.values()))
    if merged:
        r = records[gen]
        if len(merged) > len(r["args"]):
            r["args"] = merged
            r["variants"] = sorted(variants.keys())
            pref_cls = None
            for pref in ("default", "enrichResult", "compareClusterResult",
                         "gseaResult", "groupGOResult"):
                if pref in variants and variants[pref]:
                    pref_cls = pref
                    break
            if pref_cls is None and variants:
                pref_cls = sorted(variants.keys())[0]
            cand = "%s.%s" % (gen, pref_cls)
            if cand in cp_fns:
                r["def"] = cand
                r["file"] = cp_fns[cand]["file"]
                r["line"] = cp_fns[cand]["line"]


# ================ 4c. importFrom 的所有函数 ================
# 对已在 export() 里的 re-exported 函数（典型场景：R/<pkg>.R 里的
# `enrichplot::dotplot` 形式），如果没解析到 args，用 THIRD_PARTY_PARAMS 补齐。
for pkg, fns in imports.items():
    for fn in fns:
        name = fn.strip().strip('"')
        if not name:
            continue
        params = THIRD_PARTY_PARAMS.get(name)
        if params is None:
            continue
        arg_records = [{"name": a, "default": None} for a in params
                       if a != "..."]
        if name in records:
            r = records[name]
            if not r["args"]:
                r["args"] = arg_records
            r["pkg"] = pkg
            r["kind"] = "reexport"
        else:
            records[name] = {
                "name": name, "pkg": pkg, "kind": "reexport",
                "def": None, "file": None, "line": None, "args": arg_records,
            }


# ================ 4d. enrichit 关键函数补充 ================
# enrichit 是 clusterProfiler 的依赖引擎（cp 的 importFrom 列表里没有它），
# 但用户脚本里常通过 enrichit::xxx 直接调用。
# THIRD_PARTY_PARAMS 里已列出这些函数的形参，这里把它们加进 records。
EXTRA_ENRICHIT = {
    "aggregate_enrichment", "aggregate_omics", "bayes_enrich", "bayes_summary",
    "gsfilter", "harmonize_ids", "select_features_for_ora", "setReadable",
    "build_kegg_graph", "build_go_graph", "build_string_graph",
    "prepare_network", "prepare_multilayer_network",
    "propagate_multilayer", "collapse_multilayer_scores",
    "ora", "gsea", "gseaScores",
    "get_omics_contribution", "classify_omics_pattern",
    "get_mnsea_contribution", "extract_mnsea_subnetwork",
    "as_enrichResult", "as_gseaResult",
    "EXTID2NAME",    "msigdbr",
}
for name in EXTRA_ENRICHIT:
    if name in records:
        continue
    params = THIRD_PARTY_PARAMS.get(name)
    if not params:
        continue
    records[name] = {
        "name": name, "pkg": "enrichit", "kind": "reexport",
        "def": None, "file": None, "line": None,
        "args": [{"name": a, "default": None} for a in params if a != "..."],
    }


# ================ 5. S4 method ================
s4methods = []
for fname, d in cp_fns.items():
    if d.get("s4method"):
        s4methods.append({
            "generic": d["generic"],
            "class": d["class"],
            "key": fname,
        })


# ================ 6. 弃用参数扫描 ================
DEPRE_RE = re.compile(r"deprecated\s*\(\s*[\"']([^\"']+)[\"']\s*\)")
deprecated = {}
for n, d in cp_fns.items():
    try:
        src = io.open(os.path.join(rdir, d["file"]), encoding="utf-8",
                      errors="replace").read()
    except Exception:
        continue
    hits = {}
    for a in d["args"]:
        arg_name = a["name"]
        # 在该函数定义附近找 deprecated() 标记
        for m in DEPRE_RE.finditer(src):
            if m.group(1) == arg_name:
                hits[arg_name] = "该参数已弃用"
    if hits:
        deprecated[n] = hits


# ================ 7. 版本 ================
def read_ver(p):
    d = io.open(p, encoding="utf-8", errors="replace").read()
    m = re.search(r"^Version:\s*(\S+)", d, re.M)
    return m.group(1) if m else "?"


ver = read_ver(os.path.join(CP, "DESCRIPTION"))

data = {
    "clusterprofiler_version": ver,
    "functions": records,
    "s3methods": s3,
    "s4classes": s4cls,
    "s4methods": s4methods,
    "imports": {k: sorted(set(v)) for k, v in imports.items()},
    "internal_functions": sorted(cp_fns.keys()),
}

with io.open(os.path.join(RAW, "api_full.json"), "wb") as f:
    f.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))


# ================ 8. 统计 ================
n_sig = sum(1 for r in records.values() if r["args"])
n_pkg = {}
for r in records.values():
    n_pkg[r.get("pkg", "?")] = n_pkg.get(r.get("pkg", "?"), 0) + 1
print("clusterProfiler version:", ver)
print("total known symbols:", len(records))
print("  with real formals:   ", n_sig)
print("  S3 method entries:   ", len(s3))
print("  S4 method entries:   ", len(s4methods))
print("  S4 classes:          ", len(s4cls))
print("  internal fns parsed: ", len(cp_fns))
print("  by package:")
for k, v in sorted(n_pkg.items(), key=lambda x: -x[1]):
    print("    %-20s %d" % (k, v))
no_sig = sorted(n for n, r in records.items() if not r["args"])
print("  no formals (%d): %s" % (len(no_sig), ", ".join(no_sig[:60])))
print("  deprecated params in", len(deprecated), "fns")