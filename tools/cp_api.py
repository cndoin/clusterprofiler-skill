#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cp_api.py —— 离线查 clusterProfiler 函数真实签名（数据来自源码解析，不联网）

用法：
  python cp_api.py enrichGO                查单个函数
  python cp_api.py enrichGO --json         机器可读
  python cp_api.py --search kegg           模糊搜索函数名
  python cp_api.py --module gsea           列出某模块全部函数
  python cp_api.py --list-modules          列出模块
"""
import io, os, re, sys, json, argparse, difflib

HERE = os.path.dirname(os.path.abspath(__file__))
WL = os.path.join(HERE, "whitelist.json")
SIG = os.path.join(os.path.dirname(HERE), "references", "api-signatures.md")


def load():
    wl = json.loads(io.open(WL, encoding="utf-8").read())
    sigs = {}
    if os.path.exists(SIG):
        cur = None
        for line in io.open(SIG, encoding="utf-8"):
            line = line.rstrip("\n")
            if line.startswith("### "):
                cur = line[4:].strip()
            elif cur and line.startswith("`") and line.endswith("`"):
                sigs[cur] = line.strip("`")
                cur = None
    return wl, sigs


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("name", nargs="?", help="函数名")
    ap.add_argument("--search", "-s", help="模糊搜索")
    ap.add_argument("--module", "-m",
                    help="按模块列出（ora/gsea/id/db/go/manip/viz/llm/dplyr/reexport）")
    ap.add_argument("--list-modules", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    wl, sigs = load()
    syms = wl["symbols"]
    dep = wl.get("deprecated_args", {})

    if a.list_modules:
        mods = {}
        for n, r in syms.items():
            mods.setdefault(r["module"], []).append(n)
        for m in sorted(mods):
            print("%-10s %d" % (m, len(mods[m])))
        return 0

    if a.module:
        names = sorted(n for n, r in syms.items() if r["module"] == a.module)
        if not names:
            sys.stderr.write("no such module: %s (try --list-modules)\n" % a.module)
            return 2
        print("module `%s` (%d):" % (a.module, len(names)))
        print("  " + ", ".join(names))
        return 0

    if a.search:
        q = a.search.lower()
        hit = [n for n in syms if q in n.lower()]
        hit += [n for n in difflib.get_close_matches(a.search, list(syms), n=8, cutoff=0.5)
                if n not in hit]
        if not hit:
            print("no match for `%s`" % a.search)
            return 0
        print("search `%s` -> %d hits" % (a.search, len(hit)))
        for n in sorted(hit)[:40]:
            print("  %-28s [%s / %s]" % (n, syms[n]["module"], syms[n]["pkg"]))
        return 0

    if not a.name:
        ap.print_help()
        return 2

    n = a.name
    if n not in syms:
        sys.stderr.write("`%s` 不在 clusterProfiler 导出 / re-export 清单里 —— 可能是幻觉函数名\n" % n)
        lower = {k.lower(): k for k in syms}
        if n.lower() in lower:
            sys.stderr.write("  大小写错误，应为 `%s`\n" % lower[n.lower()])
        close = difflib.get_close_matches(n, list(syms), n=5, cutoff=0.6)
        if close:
            sys.stderr.write("  相近：%s\n" % ", ".join(close))
        return 1

    r = syms[n]
    # 若用户传的是 pkg::sym，把 name 字段切成短名 + 全名（不破坏 pkg 前缀语义）
    if "::" in n:
        short = n.split("::", 1)[1]
        r = dict(r); r["name"] = short; r["qualified_name"] = n
        n = short
    sig = sigs.get(n) or "%s(%s)" % (n, ", ".join(r["args"]))
    if a.json:
        print(json.dumps({"name": n, "module": r["module"], "pkg": r["pkg"],
                          "impl": r["def"], "signature": sig, "args": r["args"],
                          "kind": r["kind"],
                          "deprecated_args": dep.get(n, {})},
                         ensure_ascii=False, indent=2))
        return 0
    print("%s   [%s / %s]" % (sig, r["module"], r["pkg"]))
    if r["def"]:
        print("  实现: %s" % r["def"])
    if dep.get(n):
        print("  弃用参数: %s" % ", ".join("%s(%s)" % (k, v) for k, v in dep[n].items()))
    print("  参数(%d): %s" % (len(r["args"]), ", ".join(r["args"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())