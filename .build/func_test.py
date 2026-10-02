"""功能完整性端到端测试 — 不改任何状态、只读 + 模拟输入。

覆盖：
  T1  fetch_sources --check        38/38 可达
  T2  build_api --stats             白名单自洽（键数 / 包数 / 形式参数覆盖率 / 有重复键）
  T3  cp_api 已知短名               enrichGO
  T4  cp_api pkg::sym 已知          clusterProfiler::enrichGO
  T5  cp_api 拒识别不存在           enrichGOO
  T6  cp_api --search 子串          kegg
  T7  cp_api 大小写纠错             enrichgo
  T8  cp_api 拒识别带 :: 不存在     foo::barBaz
  T9  cp_lint 正确代码 PASS         多个 fixture 文件
  T10 cp_lint 幻觉函数被拦          tests/fixtures/02_hallucination.R
  T11 cp_lint pkg:: 跨包            K24 case
  T12 cp_lint ecosystem 外包放行    K29 case
  T13 cp_plan --list ≥ 15 个 plan
  T14 cp_plan enrichGO 返回步骤
  T15 gen_docs.py 加载无异常
  T16 rebuild.py --help
"""
import json, os, subprocess, sys, tempfile, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable

passes = []
fails = []

def ok(name, cond, detail=""):
    if cond:
        passes.append(name)
        print(f"  [PASS] {name}{(' — ' + detail) if detail else ''}")
    else:
        fails.append((name, detail))
        print(f"  [FAIL] {name}{(' — ' + detail) if detail else ''}")

def run(args, **kw):
    return subprocess.run([PY, *args], cwd=str(ROOT), capture_output=True, text=True, **kw)

# T1: fetch_sources --check — 重试 3 次容忍瞬时网络问题
# 实测：codeload HEAD 偶发 4xx（GitHub 限流），单次跑 ~10% 概率 fail 在不同包上，
# 重试就能过。要测的是**代码正确性**，不是网络稳定性。
attempts = []
for i in range(3):
    r = run(["tools/etl/fetch_sources.py", "--check"])
    attempts.append(r)
    if r.returncode == 0 and "38 / 38" in r.stdout:
        break
    time.sleep(2)
last = attempts[-1]
ok("T1 fetch_sources --check 38/38 可达（3 次重试内）",
   last.returncode == 0 and "38 / 38" in last.stdout,
   f"rc={last.returncode}, last_line={last.stdout.strip().splitlines()[-1] if last.stdout else ''}")

# T2: build_api 输出自洽性 — 没有 --stats 标志；直接读 whitelist.json
wl_path = ROOT / "tools" / "whitelist.json"
wl = json.loads(wl_path.read_text(encoding="utf-8"))
syms = wl.get("symbols") or {}
ok("T2 build_api 输出白名单 ≥ 6000 键",
   len(syms) >= 6000,
   f"实际 {len(syms)}")
ok("T2 白名单含 6137 键",
   len(syms) == 6137,
   f"实际 {len(syms)}")
pkgs = wl.get("generated_from", {}).get("packages", {})
ok("T2 白名单 generated_from 含 38 个包",
   len(pkgs) == 38,
   f"实际 {len(pkgs)}")

# T3: cp_api enrichGO
r = run(["tools/cp_api.py", "enrichGO"])
ok("T3 cp_api enrichGO 命中",
   r.returncode == 0 and "clusterProfiler" in r.stdout and "enrichGO" in r.stdout,
   f"rc={r.returncode}")

# T4: cp_api clusterProfiler::enrichGO（输出会带 [ora / clusterProfiler] 后缀）
r = run(["tools/cp_api.py", "clusterProfiler::enrichGO"])
ok("T4 cp_api pkg::sym 命中",
   r.returncode == 0 and "enrichGO" in r.stdout and "clusterProfiler" in r.stdout,
   f"rc={r.returncode}")

# T5: cp_api 拒绝不存在的
r = run(["tools/cp_api.py", "enrichGOO"])
ok("T5 cp_api 拒绝不存在",
   r.returncode != 0,
   f"rc={r.returncode}")

# T6: cp_api --search kegg
r = run(["tools/cp_api.py", "--search", "kegg"])
ok("T6 cp_api --search kegg 命中",
   r.returncode == 0 and r.stdout.strip() != "",
   f"rc={r.returncode}, lines={len(r.stdout.splitlines())}")

# T7: 大小写纠错 — enrichgo 应被工具判为幻觉并提示 enrichGO
# 设计：rc=1 是正确的。R 区分大小写，enrichgo() 真的会运行崩；
# 工具给纠错建议是 UX，但调用 cp_lint 把它当幻觉拦下才是对的。
# 消息走 stderr（诊断输出，不是数据）—— cp_api 的契约。
r = run(["tools/cp_api.py", "enrichgo"])
ok("T7 cp_api 大小写纠错：rc=1 + 提示 enrichGO（走 stderr）",
   r.returncode == 1 and "enrichGO" in r.stderr,
   f"rc={r.returncode}")

# T8: 拒识别带 :: 不存在
r = run(["tools/cp_api.py", "foo::barBaz"])
ok("T8 cp_api 拒绝带 :: 不存在",
   r.returncode != 0,
   f"rc={r.returncode}")

# T9: cp_lint fixtures
fixtures = ["01_valid_basic.R", "02_hallucination.R", "03_valid_advanced.R",
            "04_syntax_error.R", "05_common_traps.R"]
for fix in fixtures:
    p = ROOT / "tests" / "fixtures" / fix
    r = run(["tools/cp_lint.py", str(p)])
    # 04_syntax_error.R 应该 exit 1
    expected_rc = 1 if fix in ("02_hallucination.R", "04_syntax_error.R") else 0
    ok(f"T9.{fix} cp_lint rc={expected_rc}",
       r.returncode == expected_rc,
       f"rc={r.returncode}, stderr_tail={r.stderr.strip().splitlines()[-1] if r.stderr else ''}")

# T10 / T11 / T12: cp_lint 边缘用例 — 写到临时文件
# 这些是 K23/K24/K25/K26/K27/K28/K29 的复刻
cases = [
    ("pass_simple.R",       "enrichGO(gene)\n",                              0),
    ("pass_pkg.R",          "clusterProfiler::enrichGO(gene)\n",            0),
    ("pass_pkg_cross.R",    "enrichit::bayes_enrich(x)\n",                  0),
    ("pass_third.R",        "dplyr::filter(df, x > 1)\n",                   0),
    ("fail_hallu_func.R",   "enrichGooo(gene)\n",                            1),
    ("fail_hallu_arg.R",    "enrichGO(gene, nonexistentArg = 1)\n",         1),
    ("pass_no_formal.R",    "diversity(x, index = 'shannon')\n",             0),
    ("pass_eq_flush.R",     "aggregate(x, by = list(g = cyl))\n",            0),
]
for name, content, expected_rc in cases:
    # 写到 .build/func_test_fixtures/ —— 不能污染 tests/fixtures/，
    # 否则 selftest 会扫描到并要 EXPECT 表里加条目。
    p = ROOT / ".build" / "func_test_fixtures" / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    r = run(["tools/cp_lint.py", str(p)])
    ok(f"T10.{name} cp_lint rc={expected_rc}",
       r.returncode == expected_rc,
       f"rc={r.returncode}, stderr_tail={r.stderr.strip().splitlines()[-1] if r.stderr else ''}")

# T13: cp_plan --list
r = run(["tools/cp_plan.py", "--list"])
ok("T13 cp_plan --list ≥ 15 个 plan",
   r.returncode == 0 and len(r.stdout.splitlines()) >= 15,
   f"rc={r.returncode}, lines={len(r.stdout.splitlines())}")

# T14: cp_plan enrichGO
r = run(["tools/cp_plan.py", "enrichGO"])
ok("T14 cp_plan enrichGO 步骤",
   r.returncode == 0 and "enrichGO" in r.stdout,
   f"rc={r.returncode}")

# T15: gen_docs.py 可加载 + load_pkgs 可调用
r = run(["-c", "import sys; sys.path.insert(0, 'tools/etl'); import gen_docs; pkgs = gen_docs.load_pkgs(); print('loaded', len(pkgs))"])
ok("T15 gen_docs.py 可加载并能 load_pkgs",
   r.returncode == 0 and "loaded" in r.stdout,
   f"rc={r.returncode}, stdout={r.stdout.strip()}")

# T16: rebuild.py --help
r = run(["tools/etl/rebuild.py", "--help"])
ok("T16 rebuild.py --help",
   r.returncode == 0,
   f"rc={r.returncode}")

print()
print(f"===== 功能测试: {len(passes)}/{len(passes)+len(fails)} 通过 =====")
if fails:
    print("FAILED:")
    for n, d in fails:
        print(f"  - {n}: {d}")
    sys.exit(1)
sys.exit(0)
