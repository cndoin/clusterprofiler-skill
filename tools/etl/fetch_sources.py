#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fetch_sources.py —— 抓取 YuLab-SMU 生态包的源码，为重建事实底座做准备。

只用标准库（urllib / json / tarfile），不依赖 git 二进制、不依赖第三方包。

抓取策略（按顺序尝试，第一个成功即止）：
  1. GitHub tarball  https://codeload.github.com/<owner>/<repo>/tar.gz/<ref>
     —— 1 个请求拿全部文件，且不受 api.github.com 的 60 次/小时限制
  2. GitHub API 列目录 + 逐文件下载 raw.githubusercontent.com
     —— tarball 失败时的兜底（受 API 限流，包大时可能很慢）
  3. Bioconductor 源码 tarball（仅 spec 写成 "bioc:<Pkg>" 的包，如 CNEr）

ref 自动回退：spec 里指定的 ref → devel → master → main → HEAD。
YuLab-SMU 组织里有一半包只有 master，一半只有 devel，硬编码单一 ref 必然漏抓。

**失败一定响亮**：某个包如果拿不到 NAMESPACE 或 0 个 R 文件，会被记入 failed
并以退出码 1 结束。绝不静默产出空包 —— 空包会让下游 whitelist 少掉一个包的
全部符号，表现为「用户写对了却被 linter 报 unknown-function」，极难排查。

用法：
  python3 fetch_sources.py --list                     列出所有包与数据源
  python3 fetch_sources.py --check                    只探测可达性，不下载（CI 用）
  python3 fetch_sources.py --all                      抓所有 PACKAGES 列出的包
  python3 fetch_sources.py --pkg CNEr --pkg aplot      抓指定包（可多次）
  python3 fetch_sources.py --all --force              忽略已有文件，强制重抓

环境变量：
  CP_BUILD_DIR      覆盖输出根目录（默认 <skill>/.build）
  CP_INSECURE_TLS=1 跳过证书校验（企业代理）

退出码：0 = 全部成功；1 = 有包失败；2 = 用法错误
"""
import io
import json
import os
import re
import ssl
import sys
import tarfile
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(HERE))
BUILD_DIR = os.path.abspath(os.environ.get(
    "CP_BUILD_DIR", os.path.join(SKILL_DIR, ".build")))

UA = {"User-Agent": "clusterprofiler-skill/2.0 (+https://github.com/YuLab-SMU)"}
RETRIES = 3
BIOC_REL = os.environ.get("CP_BIOC_RELEASE", "devel")

# ---------------------------------------------------------------------------
# 包清单
# ---------------------------------------------------------------------------
# 值的三种形态：
#   "owner/repo"            → 默认 ref 走自动回退（devel → master → main → HEAD）
#   ("owner/repo", "ref")   → 锁定 ref（仅当该包只有一个可用分支时才用）
#   "bioc:<Pkg>"            → Bioconductor 源码 tarball（GitHub 无公开仓库）
#
# 每条 spec 都经过 `--check` 实测可达。改这个表之后请务必重跑 --check。
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
    # aPEAR 的上游不在 YuLab-SMU 组织下，是独立作者仓库（CRAN 同源）
    "aPEAR":                "ievaKer/aPEAR",
    "CBNplot":              "YuLab-SMU/CBNplot",
    "clusterProfiler.dplyr": "YuLab-SMU/clusterProfiler.dplyr",
    "aisdk":                "YuLab-SMU/aisdk",
    "TCMDATA":              "YuLab-SMU/TCMDATA",
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
    # CNEr 从未上 GitHub，唯一权威源码是 Bioconductor
    "CNEr":                 "bioc:CNEr",
    "yulab.utils":          "YuLab-SMU/yulab.utils",
    # ----- P2: 绘图辅助 -----
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

# 已知无法覆盖的包 —— 显式记录，避免下次有人"以为抓到了"
# key = 包名, value = 不可达的原因
KNOWN_UNAVAILABLE = {
    "HDO": "GitHub 与 Bioconductor 均无公开源码仓库（已从事实底座移除，"
           "调用 HDO 函数时 cp_lint 会报 unknown-function，属预期行为）",
}

REF_CANDIDATES = ("devel", "master", "main", "HEAD")


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------
def _ctx():
    if os.environ.get("CP_INSECURE_TLS") == "1":
        c = ssl.create_default_context()
        c.check_hostname = False
        c.verify_mode = ssl.CERT_NONE
        return c
    return ssl.create_default_context()


def get(url, binary=False, timeout=120):
    """带重试的 GET。全部重试失败抛最后一个异常。"""
    last = None
    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout, context=_ctx()) as r:
                b = r.read()
            return b if binary else b.decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            # 404 是确定性结果，重试没有意义
            if e.code == 404:
                raise
            last = e
        except Exception as e:  # noqa: BLE001 - 网络层异常种类多，统一重试
            last = e
        if attempt < RETRIES - 1:
            time.sleep(1.5 * (attempt + 1))
    raise last


# ---------------------------------------------------------------------------
# ref 解析
# ---------------------------------------------------------------------------
def _codeload_ok(repo, ref, timeout=30):
    """用 HTTP HEAD 向 codeload 探测 ref 是否真实存在（响应体为 0 字节，很便宜）。

    **不能用 raw.githubusercontent.com 探测**：实测发现对不存在的 ref，
    raw 会静默回退到默认分支并返回 200，例如只有 `main` 分支的 gson，
    `raw/.../master/DESCRIPTION` 也是 200。而 codeload 会老实报 404。
    这个差异会导致抓到「有 NAMESPACE、零个 R 文件」的残包。
    """
    url = "https://codeload.github.com/%s/tar.gz/%s" % (repo, ref)
    try:
        req = urllib.request.Request(url, headers=UA, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout, context=_ctx()) as r:
            return r.status == 200
    except Exception:  # noqa: BLE001
        return False


def resolve_ref(repo, preferred=None):
    """返回该 repo 第一个真实存在的 ref；都不行返回 None。

    顺序：用户指定的 ref → devel → master → main → HEAD。
    YuLab-SMU 组织里一半包只有 devel、另一半只有 master/main，
    所以硬编码单一 ref 必然漏抓；而固定用 HEAD 又会让
    clusterProfiler 这类有独立开发分支的包拿到错的版本。
    """
    cands = []
    if preferred:
        cands.append(preferred)
    for r in REF_CANDIDATES:
        if r not in cands:
            cands.append(r)
    for ref in cands:
        if _codeload_ok(repo, ref):
            return ref
    return None


# ---------------------------------------------------------------------------
# 策略 1：GitHub tarball（首选，1 个请求）
# ---------------------------------------------------------------------------
def _safe_members(tf, top):
    """只保留 top 目录下的常规文件，拒绝路径穿越。"""
    for m in tf.getmembers():
        if not m.isfile():
            continue
        name = m.name.replace("\\", "/")
        if ".." in name.split("/"):
            continue
        if not name.startswith(top + "/"):
            continue
        yield m, name[len(top) + 1:]


def fetch_tarball(repo, ref, dest, want_r=True):
    """下载并解包 repo@ref 的 tarball。返回写入的文件数。"""
    url = "https://codeload.github.com/%s/tar.gz/%s" % (repo, ref)
    raw = get(url, binary=True, timeout=180)
    written = 0
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as tf:
        members = list(tf.getmembers())
        if not members:
            raise IOError("tarball 为空: %s" % url)
        top = members[0].name.replace("\\", "/").split("/")[0]
        for m, rel in _safe_members(tf, top):
            if rel in ("DESCRIPTION", "NAMESPACE", "NEWS.md"):
                target = os.path.join(dest, rel)
            elif want_r and rel.startswith("R/") and rel.endswith(".R") and rel.count("/") == 1:
                target = os.path.join(dest, "R", os.path.basename(rel))
            else:
                continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            fh = tf.extractfile(m)
            if fh is None:
                continue
            with io.open(target, "wb") as out:
                out.write(fh.read())
            written += 1
    return written


# ---------------------------------------------------------------------------
# 策略 2：GitHub API 逐文件（兜底）
# ---------------------------------------------------------------------------
def fetch_via_api(repo, ref, dest):
    written = 0
    for f in ("DESCRIPTION", "NAMESPACE", "NEWS.md"):
        p = os.path.join(dest, f)
        if os.path.exists(p) and os.path.getsize(p) > 0:
            continue
        try:
            with io.open(p, "wb") as fh:
                fh.write(get("https://raw.githubusercontent.com/%s/%s/%s" % (repo, ref, f),
                             binary=True))
            written += 1
        except Exception as e:  # noqa: BLE001
            sys.stderr.write("    WARN: %s 下载失败（%s）\n" % (f, str(e)[:80]))

    api = "https://api.github.com/repos/%s/contents/R?ref=%s" % (repo, ref)
    try:
        items = json.loads(get(api))
    except Exception as e:  # noqa: BLE001
        sys.stderr.write("    WARN: R/ 列目录失败（%s）\n" % str(e)[:80])
        return written
    if not isinstance(items, list):
        return written
    rdir = os.path.join(dest, "R")
    os.makedirs(rdir, exist_ok=True)
    for it in items:
        if it.get("type") != "file" or not it.get("name", "").endswith(".R"):
            continue
        p = os.path.join(rdir, it["name"])
        if os.path.exists(p) and os.path.getsize(p) > 0:
            continue
        try:
            with io.open(p, "wb") as fh:
                fh.write(get(it["download_url"], binary=True))
            written += 1
        except Exception as e:  # noqa: BLE001
            sys.stderr.write("    WARN: %s 下载失败（%s）\n" % (it["name"], str(e)[:60]))
    return written


# ---------------------------------------------------------------------------
# 策略 3：Bioconductor 源码 tarball
# ---------------------------------------------------------------------------
_bioc_index_cache = {}


def bioc_version(pkg, rel=BIOC_REL):
    """从 Bioconductor 的 PACKAGES 索引里取该包版本号；不存在返回 None。"""
    if rel not in _bioc_index_cache:
        idx = get("https://bioconductor.org/packages/%s/bioc/src/contrib/PACKAGES" % rel,
                  timeout=180)
        _bioc_index_cache[rel] = idx
    m = re.search(r"^Package: %s\nVersion: (\S+)" % re.escape(pkg),
                  _bioc_index_cache[rel], re.M)
    return m.group(1) if m else None


def fetch_bioc(pkg, dest, rel=BIOC_REL):
    """返回 (版本号, 写入文件数)。包不在该 release 里则抛异常。"""
    ver = bioc_version(pkg, rel)
    if not ver:
        raise IOError("%s 不在 Bioconductor/%s 的 bioc 仓库里" % (pkg, rel))
    url = "https://bioconductor.org/packages/%s/bioc/src/contrib/%s_%s.tar.gz" % (
        rel, pkg, ver)
    raw = get(url, binary=True, timeout=240)
    written = 0
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as tf:
        members = list(tf.getmembers())
        if not members:
            raise IOError("tarball 为空: %s" % url)
        top = members[0].name.replace("\\", "/").split("/")[0]
        for m, relpath in _safe_members(tf, top):
            if relpath in ("DESCRIPTION", "NAMESPACE", "NEWS.md"):
                target = os.path.join(dest, relpath)
            elif relpath.startswith("R/") and relpath.endswith(".R") and relpath.count("/") == 1:
                target = os.path.join(dest, "R", os.path.basename(relpath))
            else:
                continue
            os.makedirs(os.path.dirname(target), exist_ok=True)
            fh = tf.extractfile(m)
            if fh is None:
                continue
            with io.open(target, "wb") as out:
                out.write(fh.read())
            written += 1
    return ver, written


# ---------------------------------------------------------------------------
# 单包抓取
# ---------------------------------------------------------------------------
def _have(pkg, dest):
    """判断本地是否已有一份可用源码：NAMESPACE 非空 且 至少 1 个非空 R 文件。"""
    ns = os.path.join(dest, "NAMESPACE")
    if not (os.path.exists(ns) and os.path.getsize(ns) > 0):
        return False
    rdir = os.path.join(dest, "R")
    if not os.path.isdir(rdir):
        return False
    return any(f.endswith(".R") and os.path.getsize(os.path.join(rdir, f)) > 0
               for f in os.listdir(rdir))


def fetch_one(pkg, spec, force=False):
    """抓一个包。返回统计 dict。失败时 ok=False 且 reason 非空。"""
    dest = os.path.join(BUILD_DIR, pkg)
    os.makedirs(dest, exist_ok=True)
    st = {"pkg": pkg, "ok": False, "reason": "", "source": "", "ref": "",
          "r_files": 0, "written": 0}

    if not force and _have(pkg, dest):
        st.update(ok=True, source="local", ref="-",
                  r_files=len([f for f in os.listdir(os.path.join(dest, "R"))
                               if f.endswith(".R")]))
        _ensure_provenance(pkg, spec, st, dest)
        return st

    # ---- Bioconductor ----
    if isinstance(spec, str) and spec.startswith("bioc:"):
        name = spec.split(":", 1)[1]
        try:
            ver, n = fetch_bioc(name, dest)
        except Exception as e:  # noqa: BLE001
            st["reason"] = "Bioconductor 抓取失败: %s" % str(e)[:110]
            return st
        st.update(source="bioconductor", ref=ver, written=n)
    else:
        # ---- GitHub ----
        if isinstance(spec, tuple):
            repo, fixed = spec
        else:
            repo, fixed = spec, None
        if "/" not in repo:
            st["reason"] = "非法的 repo 描述: %r" % (repo,)
            return st
        ref = resolve_ref(repo, fixed)
        if not ref:
            st["reason"] = "%s 在 %s 上取不到 DESCRIPTION" % (
                repo, "/".join(REF_CANDIDATES))
            return st
        st.update(source=repo, ref=ref)
        try:
            st["written"] = fetch_tarball(repo, ref, dest)
        except Exception as e:  # noqa: BLE001
            sys.stderr.write("    tarball 失败（%s），回退 API 逐文件\n" % str(e)[:80])
            st.update(source=repo + " (api)", written=fetch_via_api(repo, ref, dest))

    # ---- 验收：必须有 NAMESPACE 且有 R 文件，否则算失败 ----
    ns = os.path.join(dest, "NAMESPACE")
    if not (os.path.exists(ns) and os.path.getsize(ns) > 0):
        st["reason"] = "抓完后 NAMESPACE 仍为空（source=%s ref=%s）" % (
            st["source"], st["ref"])
        return st
    rdir = os.path.join(dest, "R")
    r_files = ([f for f in os.listdir(rdir) if f.endswith(".R")]
               if os.path.isdir(rdir) else [])
    st["r_files"] = len(r_files)
    if not r_files:
        st["reason"] = "抓完后 0 个 R 文件（source=%s ref=%s）" % (st["source"], st["ref"])
        return st
    st["ok"] = True
    _ensure_provenance(pkg, spec, st, dest)
    return st


def _ensure_provenance(pkg, spec, st, dest):
    """把该包真实的来源写进 <dest>/source.json，供 build_api / gen_docs 读取。

    只在缺失时补写；已有就保留（避免 --no-fetch 复用本地源码时把信息改坏）。
    复用本地源码时 st["ref"] 是 "-"，此时向 codeload 探一次真实 ref。
    """
    p = os.path.join(dest, "source.json")
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return
    repo, ref = "", st.get("ref") or ""
    if isinstance(spec, str) and spec.startswith("bioc:"):
        name = spec.split(":", 1)[1]
        repo = "bioconductor.org/packages/%s/bioc" % BIOC_REL
        ref = st.get("ref") if st.get("ref") not in ("", "-") else (bioc_version(name) or "?")
    else:
        if isinstance(spec, tuple):
            repo, fixed = spec
        else:
            repo, fixed = spec, None
        if ref in ("", "-"):
            ref = resolve_ref(repo, fixed) or "?"
    info = {
        "package": pkg,
        "repo": repo,
        "ref": ref,
        "r_files": st.get("r_files", 0),
        "fetched_at": __import__("datetime").datetime.now().isoformat(),
    }
    with io.open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(info, ensure_ascii=False, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _spec_label(pkg, spec):
    if isinstance(spec, tuple):
        return "%s @%s" % (spec[0], spec[1])
    return spec


def do_check(targets):
    """只探测可达性，不写文件。"""
    print("检查 %d 个包的数据源可达性（不下载源码）..." % len(targets))
    bad = []
    for pkg, spec in targets.items():
        if isinstance(spec, str) and spec.startswith("bioc:"):
            name = spec.split(":", 1)[1]
            try:
                v = bioc_version(name)
                print("  [OK]   %-22s bioc:%s @ %s" % (pkg, name, v))
                continue
            except Exception as e:  # noqa: BLE001
                print("  [FAIL] %-22s bioc:%s (%s)" % (pkg, name, str(e)[:60]))
                bad.append(pkg)
                continue
        repo, fixed = spec if isinstance(spec, tuple) else (spec, None)
        ref = resolve_ref(repo, fixed)
        if ref:
            print("  [OK]   %-22s %s @ %s" % (pkg, repo, ref))
        else:
            print("  [FAIL] %-22s %s（无可用 ref）" % (pkg, repo))
            bad.append(pkg)
    print("")
    print("可达 %d / %d" % (len(targets) - len(bad), len(targets)))
    if bad:
        print("不可达: %s" % ", ".join(bad))
    return 1 if bad else 0


def main():
    import argparse
    ap = argparse.ArgumentParser(description="抓取 YuLab-SMU 生态包源码")
    ap.add_argument("--pkg", action="append", default=[],
                    help="要抓的包名（可多次传）。缺省: clusterProfiler")
    ap.add_argument("--all", action="store_true", help="抓所有 PACKAGES 列出的包")
    ap.add_argument("--list", action="store_true", help="列出所有支持的包")
    ap.add_argument("--check", action="store_true",
                    help="只探测每个包的数据源可达性，不下载")
    ap.add_argument("--force", action="store_true",
                    help="忽略本地已有源码，强制重抓")
    a = ap.parse_args()

    if a.list:
        for k, v in PACKAGES.items():
            print("%-24s %s" % (k, _spec_label(k, v)))
        for k, why in KNOWN_UNAVAILABLE.items():
            print("%-24s [不可用] %s" % (k, why))
        return 0

    if a.check:
        return do_check(PACKAGES)

    if a.all:
        targets = dict(PACKAGES)
    elif a.pkg:
        unknown = [k for k in a.pkg if k not in PACKAGES]
        for u in unknown:
            why = KNOWN_UNAVAILABLE.get(u)
            if why:
                sys.stderr.write("ERROR: 包 `%s` 无公开源码：%s\n" % (u, why))
            else:
                sys.stderr.write("ERROR: 未知包名 `%s`（用 --list 查看全部）\n" % u)
        if unknown:
            return 2
        targets = {k: PACKAGES[k] for k in a.pkg}
    else:
        targets = {"clusterProfiler": PACKAGES["clusterProfiler"]}

    os.makedirs(BUILD_DIR, exist_ok=True)
    print("BUILD_DIR = %s" % BUILD_DIR)
    stats, failed = [], []
    for pkg, spec in targets.items():
        print("[%s] %s" % (pkg, _spec_label(pkg, spec)))
        st = fetch_one(pkg, spec, force=a.force)
        stats.append(st)
        if st["ok"]:
            print("  OK  %s @ %s -> %d R 文件（新写入 %d）" % (
                st["source"], st["ref"], st["r_files"], st["written"]))
        else:
            failed.append(pkg)
            print("  FAIL  %s" % st["reason"])
            sys.stderr.write("ERROR: [%s] %s\n" % (pkg, st["reason"]))

    n_ok = len(stats) - len(failed)
    print("")
    print("===== 抓取完成：%d 成功 / %d 失败（共 %d）=====" % (
        n_ok, len(failed), len(stats)))
    if failed:
        print("失败的包: %s" % ", ".join(failed))
        print("提示：失败包不会进入 whitelist，其函数在 cp_lint 里会被判为"
              "unknown-function。请先修好数据源再重建事实底座。")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
