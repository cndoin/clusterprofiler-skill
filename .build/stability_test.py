"""稳定性压测 — 并发 + 大输入 + 极端边界。

T1 并发读取：cp_lint 同进程跑 5 次 vs 子进程并发 5 个，验证没有竞态
T2 大文件：生成 1000 行 R 代码（95% 是注释 + 5% 是 enrichGO 调用），看 linter 性能
T3 极长 ident：构造 200 字符的变量名，看 token 化没崩
T4 空 / 单字符文件
T5 CRLF 文件（Windows 风格）
T6 大字符串字面量（10KB 单行）
T7 大括号嵌套 (()()()() * 50 层)
"""
import subprocess, sys, time, os, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable
FIX_DIR = ROOT / ".build" / "stability_fixtures"
FIX_DIR.mkdir(parents=True, exist_ok=True)
passes = []
fails = []
def ok(n, cond, detail=""):
    if cond: passes.append(n); print(f"  [PASS] {n}{' — '+detail if detail else ''}")
    else:    fails.append((n, detail)); print(f"  [FAIL] {n}{' — '+detail if detail else ''}")

# T1: 并发 5 个 cp_lint 进程
import concurrent.futures as cf
fixture = FIX_DIR / "concurrent.R"
fixture.write_text("enrichGO(gene)\n", encoding="utf-8")
start = time.time()
with cf.ThreadPoolExecutor(max_workers=5) as ex:
    futs = [ex.submit(subprocess.run, [PY, "tools/cp_lint.py", str(fixture)],
                      cwd=str(ROOT), capture_output=True, text=True) for _ in range(5)]
    rcs = [f.result().returncode for f in futs]
elapsed = time.time() - start
ok("T1 5 个 cp_lint 并发全部 rc=0", all(rc == 0 for rc in rcs),
   f"rcs={rcs}, 用时 {elapsed:.2f}s")

# T2: 大文件（1000 行，5% enrichGO 调用）
big = FIX_DIR / "big.R"
big_content = "\n".join([
    "# 注释行 %d" % i if i % 20 else "enrichGO(gene%d)" % i
    for i in range(1000)
])
big.write_text(big_content, encoding="utf-8")
start = time.time()
r = subprocess.run([PY, "tools/cp_lint.py", str(big)], cwd=str(ROOT),
                   capture_output=True, text=True)
elapsed = time.time() - start
ok("T2 1000 行大文件 cp_lint 不超时",
   r.returncode == 0 and elapsed < 30,
   f"rc={r.returncode}, 用时 {elapsed:.2f}s")

# T3: 200 字符变量名
long_ident = "a" * 200
content = f"{long_ident} <- 1\nenrichGO({long_ident})\n"
longf = FIX_DIR / "long_ident.R"
longf.write_text(content, encoding="utf-8")
r = subprocess.run([PY, "tools/cp_lint.py", str(longf)], cwd=str(ROOT),
                   capture_output=True, text=True)
ok("T3 200 字符变量名不崩", r.returncode == 0,
   f"rc={r.returncode}")

# T4: 空 / 单字符
for fn, content in [("empty.R", ""), ("onechar.R", "x\n")]:
    p = FIX_DIR / fn
    p.write_text(content, encoding="utf-8")
    r = subprocess.run([PY, "tools/cp_lint.py", str(p)], cwd=str(ROOT),
                       capture_output=True, text=True)
    ok(f"T4.{fn} cp_lint 不崩", r.returncode in (0, 1),
       f"rc={r.returncode}")

# T5: CRLF 文件（Windows 风格行尾）
crlf = FIX_DIR / "crlf.R"
crlf.write_bytes(b"enrichGO(gene)\r\n", encoding=None) if False else crlf.write_bytes(b"enrichGO(gene)\r\n")
r = subprocess.run([PY, "tools/cp_lint.py", str(crlf)], cwd=str(ROOT),
                   capture_output=True, text=True)
ok("T5 CRLF 文件 cp_lint 不崩",
   r.returncode in (0, 1),
   f"rc={r.returncode}")

# T6: 10KB 单行字符串字面量
big_str = "'" + ("x" * 10_000) + "'"
content = f"msg <- {big_str}\nenrichGO(gene)\n"
bigsf = FIX_DIR / "big_str.R"
bigsf.write_text(content, encoding="utf-8")
r = subprocess.run([PY, "tools/cp_lint.py", str(bigsf)], cwd=str(ROOT),
                   capture_output=True, text=True)
ok("T6 10KB 字符串字面量不崩", r.returncode == 0,
   f"rc={r.returncode}")

# T7: 50 层括号嵌套
content = "enrichGO(" + "(" * 50 + "gene" + ")" * 50 + ")\n"
deepf = FIX_DIR / "deep.R"
deepf.write_text(content, encoding="utf-8")
r = subprocess.run([PY, "tools/cp_lint.py", str(deepf)], cwd=str(ROOT),
                   capture_output=True, text=True)
ok("T7 50 层嵌套括号不崩", r.returncode in (0, 1),
   f"rc={r.returncode}")

# T8: cp_lint 在不存在的文件上
r = subprocess.run([PY, "tools/cp_lint.py", str(FIX_DIR / "DOES_NOT_EXIST.R")],
                   cwd=str(ROOT), capture_output=True, text=True)
ok("T8 不存在文件 → 退出 2（不是 1）",
   r.returncode == 2,
   f"rc={r.returncode}")

# T9: cp_lint --json 输出是合法 JSON
r = subprocess.run([PY, "tools/cp_lint.py", str(fixture), "--json"],
                   cwd=str(ROOT), capture_output=True, text=True)
import json
try:
    j = json.loads(r.stdout)
    ok("T9 --json 输出合法 JSON 且有 errors 字段",
       isinstance(j, dict) and "errors" in j,
       f"keys={list(j.keys())}")
except Exception as e:
    ok("T9 --json 输出合法 JSON", False, str(e))

# T10: cp_lint 大调用量（500 个 enrichGO 调用）
big2 = FIX_DIR / "many_calls.R"
big2.write_text("\n".join(f"enrichGO(g{i})" for i in range(500)) + "\n",
                encoding="utf-8")
start = time.time()
r = subprocess.run([PY, "tools/cp_lint.py", str(big2)], cwd=str(ROOT),
                   capture_output=True, text=True)
elapsed = time.time() - start
ok("T10 500 个调用不超时",
   r.returncode == 0 and elapsed < 30,
   f"rc={r.returncode}, 用时 {elapsed:.2f}s")

print()
print(f"===== 稳定性压测: {len(passes)}/{len(passes)+len(fails)} 通过 =====")
if fails:
    print("FAILED:")
    for n, d in fails:
        print(f"  - {n}: {d}")
    sys.exit(1)
sys.exit(0)
