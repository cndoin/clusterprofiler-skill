#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fetch_sources.py —— 抓取 YuLab-SMU 生态包的源码，为重建事实底座做准备。

只用标准库（urllib / json），不依赖 git 二进制、不依赖第三方包。

抓取：
  - YuLab-SMU/<pkg> -> <BUILD>/<pkg>
    包含 DESCRIPTION / NAMESPACE / R/*.R 全部文件。
    走 GitHub API 逐个文件拉（tarball.gz 在国内网络偶有失败，API 更稳）。

用法：
  python3 fetch_sources.py --pkg clusterProfiler          抓单个包
  python3 fetch_sources.py --pkg DOSE --pkg ChIPseeker     抓多个包
  python3 fetch_sources.py --all                          抓所有 PACKAGES 列出的包
  python3 fetch_sources.py --ref devel                    指定 git ref（默认 devel）

环境变量：
  CP_BUILD_DIR  覆盖输出根目录
  CP_INSECURE_TLS=1  跳过证书校验（企业代理）

已存在的目标文件会被"补齐"而不是重下：只对缺失文件发起请求。
"""
import io
import json
import os
import ssl
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
BUILD_DIR = os.path.abspath(os.environ.get(
    "CP_BUILD_DIR", os.path.join(SKILL_DIR, ".build")))

UA = {"User-Agent": "clusterprofiler-skill/1.0 (+https://github.com/YuLab-SMU)"}


def _ctx():
    if os.environ.get("CP_INSECURE_TLS") == "1":
        c = ssl.create_default_context()
        c.check_hostname = False
        c.verify_mode = ssl.CERT_NONE
        return c
    return ssl.create_context() if False else ssl.create_default_context()


def get(url, binary=False, timeout=120):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=_ctx()) as r:
        b = r.read()
    return b if binary else b.decode("utf-8", "replace")


def fetch_repo(pkg, ref, dest):
    """下载 DESCRIPTION / NAMESPACE / R/*.R 到 dest。"""
    os.makedirs(dest, exist_ok=True)
    repo = "YuLab-SMU/%s" % pkg
    base = "https://raw.githubusercontent.com/%s/%s" % (repo, ref)

    for f in ("DESCRIPTION", "NAMESPACE", "NEWS.md"):
        url = "%s/%s" % (base, f)
        p = os.path.join(dest, f)
        if os.path.exists(p) and os.path.getsize(p) > 0:
            print("  skip %s (exists)" % f)
            continue
        print("  downloading %s" % f)
        try:
            with io.open(p, "wb") as fh:
                fh.write(get(url, binary=True))
        except Exception as e:
            print("  WARN: %s 下载失败（%s）" % (f, str(e)[:80]))

    api = "https://api.github.com/repos/%s/contents/R?ref=%s" % (repo, ref)
    print("  listing R/ via GitHub API ...")
    try:
        items = json.loads(get(api))
    except Exception as e:
        print("  WARN: R/ listing failed: %s" % str(e)[:80])
        return
    rdir = os.path.join(dest, "R")
    os.makedirs(rdir, exist_ok=True)
    n_new = 0
    for it in items:
        if it.get("type") != "file" or not it["name"].endswith(".R"):
            continue
        p = os.path.join(rdir, it["name"])
        if os.path.exists(p) and os.path.getsize(p) > 0:
            continue
        try:
            with io.open(p, "wb") as fh:
                fh.write(get(it["download_url"], binary=True))
            n_new += 1
        except Exception as e:
            print("    WARN: %s 下载失败: %s" % (it["name"], str(e)[:60]))
    n_total = len([f for f in os.listdir(rdir) if f.endswith(".R")])
    print("  -> %s (%d new files, total %d R files)" %
          (dest, n_new, n_total))


# ==============================================================================
# Y 叔生态包完整列表（生物医学知识挖掘的"全栈"）
# ==============================================================================
# 每个包用 pkg_name -> github_repo 形式列出；默认 ref 全是 devel。
PACKAGES = {
    # ----- P0: 富集分析核心栈 -----
    "clusterProfiler":      "YuLab-SMU/clusterProfiler",
    "enrichit":             "YuLab-SMU/enrichit",
    "enrichplot":           "YuLab-SMU/enrichplot",
    "gson":                 "YuLab-SMU/gson",
    "DOSE":                 "YuLab-SMU/DOSE",
    "ReactomePA":           "YuLab-SMU/ReactomePA",
    "meshes":               "YuLab-SMU/meshes",
    "GOSemSim":             "YuLab-SMU/GOSemSim",
    "ChIPseeker":           "YuLab-SMU/ChIPseeker",
    "MicrobiomeProfiler":   "YuLab-SMU/MicrobiomeProfiler",
    "HDO":                  "YuLab-SMU/HDO",
    "aPEAR":                "YuLab-SMU/aPEAR",
    "aisdk":                "YuLab-SMU/aisdk",
    # ----- P1: 进化 / 系统发育 -----
    "ggtree":               "YuLab-SMU/ggtree",
    "treeio":               "YuLab-SMU/treeio",
    "ggtreeExtra":          "YuLab-SMU/ggtreeExtra",
    "tidytree":             "YuLab-SMU/tidytree",
    # ----- P1: 微生物组 / 空间 / 单细胞 -----
    "MicrobiotaProcess":    "YuLab-SMU/MicrobiotaProcess",
    "SVP":                  "YuLab-SMU/SVP",
    "sclet":                "YuLab-SMU/sclet",
    "scMSGNN":              "YuLab-SMU/scMSGNN",
    "ggsc":                 "YuLab-SMU/ggsc",
    # ----- P1: 数据库 / 工具 -----
    "createKEGGdb":         "YuLab-SMU/createKEGGdb",
    "CNEr":                 "YuLab-SMU/CNEr",
    "yulab.utils":          "YuLab-SMU/yulab.utils",
    # ----- P2: 辅助 -----
    "aplot":                "YuLab-SMU/aplot",
    "ggimage":              "YuLab-SMU/ggimage",
    "ggtangle":             "YuLab-SMU/ggtangle",
    "ggbreak":              "YuLab-SMU/ggbreak",
    "ggmsa":                "YuLab-SMU/ggmsa",
    "ivolcano":             "YuLab-SMU/ivolcano",
    "tigeR":                "YuLab-SMU/tigeR",
    "wikiprofiler":         "YuLab-SMU/wikiprofiler",
    "epiSeeker":            "YuLab-SMU/epiSeeker",
    "scholar":              "YuLab-SMU/scholar",
    "seqmagick":            "YuLab-SMU/seqmagick",
}


def main():
    import argparse
    ap = argparse.ArgumentParser(description="抓取 YuLab-SMU 生态包源码")
    ap.add_argument("--pkg", action="append", default=[],
                    help="要抓的包名（可多次传）。缺省: clusterProfiler")
    ap.add_argument("--all", action="store_true", help="抓所有 PACKAGES 列出的包")
    ap.add_argument("--ref", default="devel", help="git ref（branch/tag/sha）")
    ap.add_argument("--list", action="store_true", help="列出所有支持的包")
    args = ap.parse_args()

    if args.list:
        for k, v in PACKAGES.items():
            print("%-22s %s" % (k, v))
        return 0

    if args.all:
        targets = PACKAGES
    elif args.pkg:
        targets = {k: PACKAGES[k] for k in args.pkg if k in PACKAGES}
        for unknown in set(args.pkg) - set(PACKAGES):
            print("WARN: 未知包名 `%s`（用 --list 查看全部）" % unknown)
    else:
        # 默认：只抓 clusterProfiler
        targets = {"clusterProfiler": PACKAGES["clusterProfiler"]}

    os.makedirs(BUILD_DIR, exist_ok=True)
    n_ok = n_fail = 0
    failed_pkgs = []
    for pkg, repo in targets.items():
        dest = os.path.join(BUILD_DIR, pkg)
        # PACKAGES 中可以是 (repo, default_ref) tuple 或仅 repo（用 args.ref）
        if isinstance(repo, tuple):
            repo_path, pkg_default_ref = repo
            ref = pkg_default_ref
        else:
            repo_path = repo
            ref = args.ref
        print("[%s] %s @ %s" % (pkg, repo_path, ref))
        try:
            fetch_repo(pkg, ref, dest)
            n_ok += 1
        except Exception as e:
            n_fail += 1
            failed_pkgs.append(pkg)
            print("  !! FAILED: %s" % str(e)[:120])
    print("\n===== 抓取完成：%d 个成功 / %d 个失败 =====" % (n_ok, n_fail))
    if failed_pkgs:
        print("失败的包: %s" % ", ".join(failed_pkgs))
    print("BUILD_DIR =", BUILD_DIR)
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())