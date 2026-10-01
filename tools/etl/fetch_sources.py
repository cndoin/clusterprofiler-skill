#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fetch_sources.py —— 抓取 clusterProfiler 源码，为重建事实底座做准备。

只用标准库（urllib / json），不依赖 git 二进制、不依赖第三方包。

默认抓取：
  - YuLab-SMU/clusterProfiler  -> <BUILD>/clusterprofiler
    包含 DESCRIPTION / NAMESPACE / R/*.R 全部文件。
    走 GitHub API 逐个文件拉（tarball.gz 在国内网络偶有失败，API 更稳）。

用法：
  python3 fetch_sources.py                 抓仓库
  python3 fetch_sources.py --ref devel     指定 git ref（branch/tag/sha，默认 devel）

输出目录可用环境变量 CP_BUILD_DIR 覆盖。
若网络环境需要跳过 TLS 校验（企业代理常见），设 CP_INSECURE_TLS=1。
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

REPO = "YuLab-SMU/clusterProfiler"
DEFAULT_REF = "devel"

UA = {"User-Agent": "clusterprofiler-skill/1.0 (+https://github.com/YuLab-SMU/clusterProfiler)"}


def _ctx():
    if os.environ.get("CP_INSECURE_TLS") == "1":
        c = ssl.create_default_context()
        c.check_hostname = False
        c.verify_mode = ssl.CERT_NONE
        return c
    return ssl.create_default_context()


def get(url, binary=False, timeout=120):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=_ctx()) as r:
        b = r.read()
    return b if binary else b.decode("utf-8", "replace")


def fetch_repo(ref, dest):
    """下载 DESCRIPTION / NAMESPACE / R/*.R 到 dest。"""
    os.makedirs(dest, exist_ok=True)
    base = "https://raw.githubusercontent.com/%s/%s" % (REPO, ref)

    for f in ("DESCRIPTION", "NAMESPACE", "NEWS.md"):
        url = "%s/%s" % (base, f)
        p = os.path.join(dest, f)
        if os.path.exists(p) and os.path.getsize(p) > 0:
            print("  skip %s (exists)" % f)
            continue
        print("  downloading %s" % f)
        with io.open(p, "wb") as fh:
            fh.write(get(url, binary=True))

    api = "https://api.github.com/repos/%s/contents/R?ref=%s" % (REPO, ref)
    print("  listing R/ via GitHub API ...")
    items = json.loads(get(api))
    rdir = os.path.join(dest, "R")
    os.makedirs(rdir, exist_ok=True)
    n = 0
    for it in items:
        if it.get("type") != "file" or not it["name"].endswith(".R"):
            continue
        p = os.path.join(rdir, it["name"])
        if os.path.exists(p) and os.path.getsize(p) > 0:
            continue
        with io.open(p, "wb") as fh:
            fh.write(get(it["download_url"], binary=True))
        n += 1
    print("  -> %s (%d new files, total %d R files)" %
          (dest, n, len([f for f in os.listdir(rdir) if f.endswith(".R")])))


def main():
    import argparse
    ap = argparse.ArgumentParser(description="抓取 clusterProfiler 源码")
    ap.add_argument("--ref", default=DEFAULT_REF,
                    help="clusterProfiler 的 git ref，默认 devel；可传 tag/sha")
    args = ap.parse_args()

    os.makedirs(BUILD_DIR, exist_ok=True)
    fetch_repo(args.ref, os.path.join(BUILD_DIR, "clusterprofiler"))
    print("BUILD_DIR =", BUILD_DIR)
    return 0


if __name__ == "__main__":
    sys.exit(main())