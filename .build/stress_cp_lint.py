"""cp_lint 压测 — 喂 30 个边缘 R 代码样本，期望每个都按预期表现。

分类：
  ✓ 应该 PASS（rc=0）：
    - 干净调用
    - 注释 + 字符串含函数名
    - 多行 ident（连续点调用）
    - 嵌套括号
    - 函数定义里有 hallucination 名（不是 call，不该拦）
    - 第三方包
    - ecosystem 包（enrichit:: 等）
    - 字符串里含 hallucination 名（不是 call，不该拦）

  ✗ 应该 FAIL（rc=1）：
    - 幻觉函数
    - 幻觉参数
    - 幻觉 pkg::
    - 没匹配 export 的 S3 generic
"""
import subprocess, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable
FIX_DIR = ROOT / ".build" / "stress_fixtures"
FIX_DIR.mkdir(parents=True, exist_ok=True)

# (filename, content, expected_rc, label)
cases = [
    # === 应该 PASS ===
    ("p01_basic.R",            "enrichGO(gene)\n", 0, "基础调用"),
    ("p02_pkg_qual.R",         "clusterProfiler::enrichGO(gene)\n", 0, "pkg:: 限定"),
    ("p03_comment.R",          "# 注释里写 enrichGooo 不算幻觉调用\nenrichGO(gene)\n", 0, "注释里含幻觉名"),
    ("p04_string.R",           'msg <- "use enrichGooo if you want"\nenrichGO(gene)\n', 0, "字符串里含幻觉名"),
    ("p05_multiline.R",        "res <- enrichGO(\n  gene = gene,\n  OrgDb = org.Hs.eg.db\n)\n", 0, "多行参数"),
    ("p06_nested_ok.R",        "enrichGO(enricher(gene, ...), OrgDb = org.Hs.eg.db)\n", 0, "嵌套已知函数"),
    ("p07_third.R",            "dplyr::filter(df, x > 1)\n", 0, "第三方 dplyr"),
    ("p08_eco_pkg.R",          "enrichit::bayes_enrich(x)\n", 0, "ecosystem 包"),
    ("p09_chipseeker.R",       "ChIPseeker::annotatePeak(peak)\n", 0, "ChIPseeker::"),
    ("p10_dot_chain.R",        "x %>% enrichGO() %>% as.data.frame()\n", 0, "%>% 链式"),
    ("p11_func_def.R",         "enrichGooo <- function(x) x  # 定义一个幻觉名\nenrichGO(gene)\n", 0, "函数定义含幻觉名"),
    ("p12_undefined.R",        "x <- 1\nenrichGO(gene)\n", 0, "未导出变量"),
    ("p13_tibble.R",           "df %>% dplyr::filter(x > 1) %>% head()\n", 0, "tibble 链"),
    ("p14_base_R.R",           "aggregate(x, by = list(g = cyl), FUN = mean)\n", 0, "base R aggregate"),
    ("p15_complex_eq.R",       "enrichGO(gene, pvalueCutoff = (x == y))\n", 0, "= 与 == 混合"),
    ("p16_unicode.R",          "# 中文注释\nenrichGO(gene)\n", 0, "中文注释"),
    ("p17_no_formal.R",        "diversity(x, index = 'shannon')\n", 0, "无 formals 时不误报"),
    ("p18_nested_pkg.R",       "x <- enrichplot::dotplot(res); y <- enrichplot::cnetplot(res)\n", 0, "同一 pkg 多次调用"),
    ("p19_trailing_comma.R",   "enrichGO(\n  gene,\n  OrgDb,\n)\n", 0, "尾随逗号"),
    ("p20_numeric.R",          "x <- 1.5e-10; enrichGO(gene)\n", 0, "科学计数法"),

    # === 应该 FAIL ===
    ("f01_hallu_func.R",       "enrichGooo(gene)\n", 1, "幻觉函数"),
    ("f02_hallu_pkg_func.R",   "foo::enrichGO(gene)\n", 0, "pkg:: 信任用户（K29 放行）"),
    ("f03_hallu_arg.R",        "enrichGO(gene, badArg = 1)\n", 1, "幻觉参数"),
    ("f04_hallu_cross.R",      "enrichit::badFn(x)\n", 1, "幻觉跨包函数"),
    ("f05_unclosed.R",         "enrichGO(\n", 1, "未闭合括号"),
    ("f06_two_calls.R",        "enrichGooo(x)\nenrichGOOther(y)\n", 1, "两个幻觉函数"),
    ("f07_mixed.R",            "enrichGO(gene)\nenrichGooo(x)\n", 1, "一真一幻"),
    ("f08_unknown_op.R",       "enrichGO(gene, ont = 'XYZ_NOT_REAL')\n", 0, "字符串值不查（只查参数名）"),  # 字符串值不查
    ("f09_bad_formal.R",       "annotatePeak(peak, badArg = 1)\n", 1, "ChIPseeker 幻觉参数"),
    ("f10_hallu_eco.R",        "CBNplot::badFn(x)\n", 1, "ecosystem 包幻觉函数"),
]

passed = []
failed = []
for name, content, expected_rc, label in cases:
    p = FIX_DIR / name
    p.write_text(content, encoding="utf-8")
    r = subprocess.run([PY, "tools/cp_lint.py", str(p)], cwd=str(ROOT),
                       capture_output=True, text=True)
    got_rc = r.returncode
    ok = got_rc == expected_rc
    line = f"  [{'PASS' if ok else 'FAIL'}] {name}  rc={got_rc} (期望 {expected_rc})  — {label}"
    print(line)
    if ok:
        passed.append(name)
    else:
        failed.append((name, got_rc, expected_rc, r.stderr[-200:]))

print()
print(f"===== cp_lint 压测: {len(passed)}/{len(cases)} 通过 =====")
if failed:
    print("\n失败详情:")
    for n, g, e, stderr in failed:
        print(f"  {n}: got {g} expected {e}")
        print(f"    stderr: {stderr[-200:]}")
    sys.exit(1)
sys.exit(0)
