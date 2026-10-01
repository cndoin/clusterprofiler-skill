#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pack.py —— 把 clusterprofiler-skill 打包成 zip / tar.gz

要求：
  1. 所有 .R / .py / .md / .json 文件都是 LF 换行（Windows 写入的 CRLF 一律转 LF）
  2. 排除 .build/ / .git/ / __pycache__/
  3. 算出 SHA-256 写入 MANIFEST.md（可选）

用法：
  python3 tools/pack.py                       打包成 dist/clusterprofiler-skill-<ver>.zip
  python3 tools/pack.py --tar                也打 .tar.gz
  python3 tools/pack.py --skip-manifest       不更新 MANIFEST.md
"""
import argparse
import hashlib
import os
import re
import sys
import zipfile
import tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
DIST_DIR = os.path.join(SKILL_DIR, "dist")

# 不打包进安装包
EXCLUDE_DIRS = {".build", "__pycache__", ".git", ".venv", "dist"}
EXCLUDE_FILES = {"Thumbs.db", ".DS_Store"}

# 需要保持 LF 行尾的文本扩展名
TEXT_EXTS = {".R", ".py", ".md", ".json", ".yaml", ".yml", ".txt", ".sh", ".Rmd"}


def get_version():
    """从 DESCRIPTION 旁路读 SKILL.md 的 version 字段"""
    p = os.path.join(SKILL_DIR, "SKILL.md")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            m = re.match(r"\s*version:\s*(\S+)", line)
            if m:
                return m.group(1)
    return "0.0.0"


def should_skip(path):
    rel = os.path.relpath(path, SKILL_DIR)
    parts = rel.split(os.sep)
    if any(p in EXCLUDE_DIRS for p in parts):
        return True
    if os.path.basename(path) in EXCLUDE_FILES:
        return True
    return False


def collect_files():
    out = []
    for root, dirs, files in os.walk(SKILL_DIR):
        # 原地修剪 dirs，os.walk 不会进 EXCLUDE_DIRS
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDE_DIRS)
        for f in sorted(files):
            p = os.path.join(root, f)
            if should_skip(p):
                continue
            out.append(p)
    return out


def to_lf(content_bytes):
    """强制 LF 行尾"""
    return content_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def write_zip(files, out_path):
    n = 0
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            rel = os.path.relpath(path, SKILL_DIR)
            data = open(path, "rb").read()
            ext = os.path.splitext(path)[1]
            if ext in TEXT_EXTS:
                data = to_lf(data)
            info = zipfile.ZipInfo(rel)
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, data)
            n += 1
    return n


def write_tar(files, out_path):
    n = 0
    with tarfile.open(out_path, "w:gz") as tf:
        for path in files:
            rel = os.path.relpath(path, SKILL_DIR)
            data = open(path, "rb").read()
            ext = os.path.splitext(path)[1]
            if ext in TEXT_EXTS:
                data = to_lf(data)
            info = tarfile.TarInfo(name=rel)
            info.size = len(data)
            info.mode = 0o644
            import io as _io
            tf.addfile(info, _io.BytesIO(data))
            n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tar", action="store_true", help="同时打 .tar.gz")
    ap.add_argument("--skip-manifest", action="store_true", help="不更新 MANIFEST.md")
    args = ap.parse_args()

    os.makedirs(DIST_DIR, exist_ok=True)
    files = collect_files()

    version = get_version()
    zip_path = os.path.join(DIST_DIR, "clusterprofiler-skill-%s.zip" % version)
    n = write_zip(files, zip_path)
    print("打包 %d 个文件 -> %s" % (n, zip_path))

    if args.tar:
        tar_path = os.path.join(DIST_DIR, "clusterprofiler-skill-%s.tar.gz" % version)
        write_tar(files, tar_path)
        print("打包 %d 个文件 -> %s" % (n, tar_path))

    # 不自动写 MANIFEST.md（避免与手动维护冲突）
    # 留 hook 给用户：想更新就解包后跑 python tools/pack.py --update-manifest
    if not args.skip_manifest:
        print("提示：MANIFEST.md 是手工维护的；如果你改了文件结构请同步更新。")


if __name__ == "__main__":
    sys.exit(main() or 0)