#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rebuild.py —— 一键重建 clusterprofiler-skill 的事实底座。

链路： 抓源码 -> 解析 NAMESPACE/formals -> 生成 references + whitelist.json

用法：
  python3 rebuild.py                  全量重建（抓全部 38 个包的源码 → 解析 → 生成文档）
  python3 rebuild.py --no-fetch       用 .build/ 里已有的源码重建（离线）
  python3 rebuild.py --dry-run        只打印将要执行的步骤

注意：fetch_sources 现在**自动**逐包探测 ref（devel → master → main → HEAD），
不存在即回退，所以 rebuild 不再需要 --ref 选项。
早期版本传的 `--ref devel` 会被新版 fetch_sources 拒收并 exit 2。

产物（都在 skill 目录内）：
  references/api-signatures.md    全量函数真实签名
  references/function-index.md    按模块分类索引
  tools/whitelist.json            cp_lint.py 用的导出符号 + 参数名 + 弃用参数

改任何一个上游版本后，请重跑本脚本 + `python3 tools/selftest.py`，
保证 references/ 与 whitelist.json 与源码一致。
"""
import argparse
import io
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
PY = sys.executable or "python3"


def run(script, extra=None):
    cmd = [PY, os.path.join(HERE, script)] + (extra or [])
    print("\n$ %s" % " ".join(cmd))
    r = subprocess.run(cmd, cwd=HERE)
    if r.returncode != 0:
        print("!! %s failed (exit=%d)" % (script, r.returncode))
        sys.exit(r.returncode)


def snapshot(path):
    if not os.path.exists(path):
        return None
    return json.loads(io.open(path, encoding="utf-8").read())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-fetch", action="store_true", help="跳过抓源码")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    wl = os.path.join(SKILL_DIR, "tools", "whitelist.json")
    before = snapshot(wl)

    # 必须 --all / --merge：原版调 `fetch_sources.py --ref devel` 只抓 clusterProfiler
    # 一个包，`build_api.py` 无参数也只解析 clusterProfiler，于是"一键重建"产出的
    # whitelist 只有 1 个包 —— 和发布版（38 包）完全对不上，是会骗人的重建脚本。
    steps = []
    if not args.no_fetch:
        # v2.1.0：fetch_sources 自动探测 ref（不存在的 ref 自动回退），
        # 不再需要给它传 --ref。
        steps.append(("fetch_sources.py", ["--all"]))
    steps.append(("build_api.py", ["--all", "--merge"]))
    steps.append(("gen_docs.py", []))

    if args.dry_run:
        for s, e in steps:
            print("would run: %s %s" % (s, " ".join(e)))
        return 0

    for s, e in steps:
        run(s, e)

    after = snapshot(wl)
    print("\n===== 结果 =====")
    if before and after:
        b = set(before.get("symbols", {}))
        a = set(after.get("symbols", {}))
        print("符号数: %d -> %d  (新增 %d, 移除 %d)" % (
            len(b), len(a), len(a - b), len(b - a)))
        if a - b:
            print("  新增:", ", ".join(sorted(a - b)[:20]))
        if b - a:
            print("  移除:", ", ".join(sorted(b - a)[:20]))
        if before.get("generated_from") != after.get("generated_from"):
            print("  上游版本: %s -> %s" % (
                before.get("generated_from"), after.get("generated_from")))
    else:
        print("whitelist.json:", len(after.get("symbols", {})) if after else "缺失")

    print("\n下一步：跑 `python3 tools/selftest.py` 确认全部用例仍然通过。")
    return 0


if __name__ == "__main__":
    sys.exit(main())