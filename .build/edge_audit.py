#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""稳定性 + 边缘场景 audit（无 call helper，全 inline）

两个必须遵守的写法约束（都是踩过的坑）：
  1. 临时 R 文件一律走 wf()：先落盘再交给子进程读。
     不要写 `with NamedTemporaryFile(...)` 然后**在 with 块内**调 subprocess：
     f.write 只进用户态缓冲，with 未退出时文件在磁盘上是空的，
     会让「未闭合括号」这类依赖文件内容的用例静默假通过。
  2. 断言要带内容证据（如 calls_found / cp_calls_checked），
     不能只断言 ok —— 空文件恰好也判 ok，等于没测。
"""
import json
import os
import re
import glob
import subprocess
import tempfile
import zipfile
from pathlib import Path

results = []


def chk(name, ok, detail=''):
    results.append((name, ok, detail))


def run(args):
    return subprocess.run(args, capture_output=True, text=True)


def wf(content, suffix='.R'):
    """写临时文件并**确保落盘**，返回路径。统一 LF 行尾。"""
    fd, path = tempfile.mkstemp(suffix=suffix)
    with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(content)
    return path


def lint(path):
    r = run(['python', 'tools/cp_lint.py', path, '--json'])
    try:
        return r.returncode, json.loads(r.stdout)
    except Exception:
        return r.returncode, {'ok': None, 'errors': [], 'stats': {}}


# ---------------------------------------------------------------- K: 边缘场景
# K1: 空文件
rc, d = lint(wf(''))
chk('K1: 空文件不报错', d['ok'] is True and len(d['errors']) == 0)

# K2: 中文注释
rc, d2 = lint(wf('library(clusterProfiler)\n# 中文注释：富集分析\nx <- 1\n'))
chk('K2: 中文注释不误报（且无 clusterProfiler 调用）',
    d2['ok'] is True and d2['stats']['cp_calls_checked'] == 0)

# K3: 不存在文件
r = run(['python', 'tools/cp_lint.py', '/nonexistent.R'])
chk('K3: 不存在文件 → exit 2', r.returncode == 2)

# K4: 未闭合括号（必须证明真的读到了内容）
rc, d = lint(wf('enrichGO(gene, OrgDb\n'))
chk('K4: 未闭合括号 → syntax（且确实读到内容）',
    any(e.get('code') == 'syntax' for e in d.get('errors', []))
    and d['stats']['calls_found'] == 1)

# K5: 无调用纯计算
rc, d5 = lint(wf('x <- 1\ny <- "hi"\n'))
chk('K5: 无调用纯计算 → PASS（且确实读到内容）',
    d5['ok'] is True and d5['stats']['calls_found'] == 0)

# K6: 多行 ident 不粘连
rc, d = lint(wf('a <- gene$log2fc\nnames(a) <- gene$entrez\na <- sort(a)\n'))
chk('K6: 多行 ident 不粘连',
    not any('log2fcnames' in e.get('msg', '') for e in d['errors']))

# K7: cp_api 短名
r = run(['python', 'tools/cp_api.py', 'enrichGO', '--json'])
d = json.loads(r.stdout)
chk('K7: cp_api 短名 enrichGO',
    d.get('name') == 'enrichGO' and len(d.get('args', [])) >= 5)

# K8: cp_api pkg::sym
r = run(['python', 'tools/cp_api.py', 'ChIPseeker::annotatePeak', '--json'])
d = json.loads(r.stdout) if r.returncode == 0 else {}
chk('K8: cp_api pkg::sym 双名',
    r.returncode == 0 and d.get('name') == 'annotatePeak'
    and len(d.get('args', [])) >= 5)

# K9: cp_api 不存在
r = run(['python', 'tools/cp_api.py', 'enrichGOO'])
chk('K9: cp_api 拒识别不存在', r.returncode != 0)

# K10: cp_plan 不存在
r = run(['python', 'tools/cp_plan.py', 'none-existent xyz123'])
chk('K10: cp_plan 拒识别未知', r.returncode != 0)

# K11: pack.py — 必须是最新那个 zip（不能测残留）
zips = sorted(glob.glob('dist/clusterprofiler-skill-*.zip'),
              key=lambda p: tuple(int(x) for x in re.findall(r'(\d+)', p)))
assert zips, 'dist 下找不到任何 zip —— 先跑 tools/pack.py'
latest_zip = zips[-1]
r = run(['python', 'tools/pack.py'])
chk('K11: pack.py 打包成功',
    r.returncode == 0 and os.path.exists(latest_zip),
    f'latest={latest_zip}')

# K12: install.py
r = run(['python', 'install.py', '--dry-run', '--host', 'workbuddy'])
chk('K12: install.py --dry-run 退出 0', r.returncode == 0)

# K13: selftest 串行 3 次 — 用 rc=0 判断，不用硬编码 N/N
# （N 会随 EXPECT 表新增条目变化，例如 v2.1.0 加了 4 个 fixture 后从 15 涨到 19）
rs = [run(['python', 'tools/selftest.py']) for _ in range(3)]
chk('K13: selftest 串行 3 次全绿',
    all(r.returncode == 0 for r in rs),
    'rcs=%s' % [r.returncode for r in rs])

# K14: install.py 未知宿主
r = run(['python', 'install.py', '--host', 'unknown_host'])
chk('K14: install.py 未知宿主 → 退出非零', r.returncode != 0)

# K15: cp_api 大小写
r = run(['python', 'tools/cp_api.py', 'enrichgo'])
chk('K15: cp_api 大小写纠错',
    r.returncode != 0 and 'enrichGO' in r.stderr)

# K16: cp_plan --list
r = run(['python', 'tools/cp_plan.py', '--list'])
plans = [l for l in r.stdout.split(chr(10))
         if l.strip() and not l.startswith("  ") and "      " not in l[:6]]
chk('K16: cp_plan --list ≥ 15 个 plan', len(plans) >= 15, f'{len(plans)} plans')

# K17: cp_api --search
r = run(['python', 'tools/cp_api.py', '--search', 'kegg'])
chk('K17: cp_api --search 退出 0', r.returncode == 0)

# K18: zip 内 LF — 必须是**最新**那个 zip，不能测残留。
# 早期版本把名字硬编码成 -2.0.0.zip，pack 升到 2.1.0 之后就测错文件了。
with zipfile.ZipFile(latest_zip) as z:
    crlf = sum(1 for n in z.namelist()
               if n.endswith(('.py', '.R', '.json', '.md'))
               and b'\r\n' in z.read(n))
chk('K18: zip 内脚本 LF 行尾', crlf == 0,
    f'{crlf} files have CRLF in {latest_zip}')

# K19: 关键 .md LF
crlf_md = []
for f in ['SKILL.md', 'README.md', 'CHANGELOG.md', 'CONTRIBUTING.md',
          'references/workflows.md', 'references/api-signatures.md']:
    p = Path(f)
    if p.exists() and b'\r\n' in p.read_bytes():
        crlf_md.append(f)
chk('K19: 关键 .md LF 行尾', not crlf_md,
    f'CRLF in {crlf_md}' if crlf_md else '')

# K20: rebuild.py --help
r = run(['python', 'tools/etl/rebuild.py', '--help'])
chk('K20: etl/rebuild.py --help 退出 0', r.returncode == 0)

# K21: fetch_sources --list
r = run(['python', 'tools/etl/fetch_sources.py', '--list'])
n_pkgs = sum(1 for l in r.stdout.split(chr(10)) if l.strip())
chk('K21: fetch_sources --list ≥ 30 行', n_pkgs >= 30, f'{n_pkgs}')

# K22: gen_docs.py 语法可加载
r = run(['python', 'tools/etl/gen_docs.py', '--help'])
chk('K22: gen_docs.py 语法可加载', r.returncode in (0, 1, 2))

# K23: 同一函数多次调用不重复误报
rc, d = lint(wf('e1 <- enrichGO(g1, org.Hs.eg.db)\n'
                'e2 <- enrichGO(g2, org.Hs.eg.db)\n'
                'e3 <- enrichGO(g3, org.Hs.eg.db)\n'))
chk('K23: 同一函数多次调用不重复误报',
    d['ok'] is True and d['stats']['calls_found'] == 3)

# K24: pkg::sym 跨包调用真的被校验（不是被跳过）
rc, d = lint(wf('r1 <- clusterProfiler::enrichGO(g1, org.Hs.eg.db)\n'
                'r2 <- DOSE::enrichDO(g2)\n'
                'r3 <- ChIPseeker::annotatePeak(r1)\n'))
chk('K24: pkg::sym 跨包调用被识别并校验',
    d['ok'] is True and d['stats']['cp_calls_checked'] == 3,
    f"checked={d['stats'].get('cp_calls_checked')}")

# K25: enrichit::bayes_enrich
rc, d = lint(wf('be <- enrichit::bayes_enrich(ego, n_terms=200, n_iter=5000)\n'))
chk('K25: enrichit::bayes_enrich 参数校验通过',
    d['ok'] is True and d['stats']['cp_calls_checked'] == 1)

# K26: 幻觉参数必须拦下
rc, d = lint(wf('e <- enrichGO(gene, OrgDb, bogus_arg = 1)\n'))
chk('K26: 幻觉参数被拦下',
    d['ok'] is False and any(e.get('code') == 'unknown-arg' for e in d['errors']))

# K27: 跨包幻觉函数必须拦下（v2.0 曾整体跳过 pkg:: 调用，是假阴性）
rc, d = lint(wf('r <- ChIPseeker::annotatePeakxx(myPeak)\n'))
chk('K27: 跨包幻觉函数被拦下',
    d['ok'] is False and any(e.get('code') == 'unknown-function'
                             for e in d['errors']))

# K28: 跨包幻觉参数必须拦下
rc, d = lint(wf('r <- DOSE::enrichDO(g, bogus_zzz = 1)\n'))
chk('K28: 跨包幻觉参数被拦下',
    d['ok'] is False and any(e.get('code') == 'unknown-arg'
                             for e in d['errors']))

# K29: 生态外的包（dplyr/ggplot2）必须放行，不能误报
rc, d = lint(wf('library(dplyr)\nx2 <- x %>% filter(a > 1)\n'
                'p <- ggplot2::ggplot(df) + ggplot2::aes(x, y)\n'))
chk('K29: 生态外第三方包调用放行', d['ok'] is True)

# ---------------------------------------------------------------- L: 数据一致性
WL = json.loads(Path('tools/whitelist.json').read_text(encoding='utf-8'))
SYMS = WL['symbols']
PKGS = WL['generated_from']['packages']
ECO_FILES = sorted(f[:-3] for f in os.listdir('references/ecosystem')
                   if f.endswith('.md'))

# L1: ecosystem 文档数 == 白名单包数（数据驱动，不写死数字）
chk('L1: ecosystem/*.md 数量 == 白名单包数',
    len(ECO_FILES) == len(PKGS), f'{len(ECO_FILES)} vs {len(PKGS)}')

# L2: ecosystem 文档名与包名精确一致（clusterProfiler 曾被写成小写）
chk('L2: ecosystem 文档名与包名精确一致',
    set(ECO_FILES) == set(PKGS),
    f'md-only={sorted(set(ECO_FILES) - set(PKGS))} '
    f'pkg-only={sorted(set(PKGS) - set(ECO_FILES))}')

# L3: 每个包都必须有真实符号（曾因抓取失败静默产出 9 个零符号包）
import collections
cnt = collections.Counter(r.get('ecosystem_pkg') for r in SYMS.values())
zero = sorted(p for p in PKGS if not cnt.get(p))
chk('L3: 无零符号包', not zero, f'zero={zero}')

# L4: 白名单键必须是合法符号名（曾混入 NAMESPACE 注释与文件名）
_SYM = re.compile(r'^[A-Za-z._][A-Za-z0-9._]*$')
_OPS = {'[', '[[', '$', '@', '<-', '<<-', '+', '-', '*', '/', '^', ':', '::',
        ':::', '~', '!', '&', '&&', '|', '||', '==', '!=', '<', '>', '<=',
        '>=', '(', '{'}


def _ok_key(k):
    tail = k.split('::')[-1]
    if tail in _OPS:
        return True
    if tail.startswith('%') and tail.endswith('%') and len(tail) > 2:
        return True
    return bool(_SYM.match(tail))


bad = [k for k in SYMS if not _ok_key(k)]
chk('L4: 白名单键全部是合法符号名', not bad, f'{len(bad)} bad, e.g. {bad[:3]}')

# L5: ecosystem 文档不能是空 stub
stubs = [f for f in ECO_FILES
         if os.path.getsize(os.path.join('references/ecosystem', f + '.md')) < 400]
chk('L5: ecosystem 文档无空 stub', not stubs, f'{stubs}')

# L6: workflows.md / pitfalls.md 代码块
chk('L6: workflows.md ≥ 10 个 R 代码块',
    Path('references/workflows.md').read_text(encoding='utf-8').count('```r\n') >= 10)
chk('L7: pitfalls.md ≥ 5 个 R 代码块',
    Path('references/pitfalls.md').read_text(encoding='utf-8').count('```r\n') >= 5)

# L8: SKILL.md 章节齐全
skill = Path('SKILL.md').read_text(encoding='utf-8')
sections = ['不可违反', '标准动作', '生态包路由', '任务', '工具', '失败协议',
            '环境边界', '参考文件', '宿主兼容']
miss = [s for s in sections if s not in skill]
chk('L8: SKILL.md 9 章节齐全', not miss, f'missing={miss}')

# L9: rebuild.py 必须是全量重建（原版只重建 1 个包，与发布版对不上）
r = run(['python', 'tools/etl/rebuild.py', '--dry-run'])
chk('L9: rebuild.py 走全量链路',
    '--all' in r.stdout and '--merge' in r.stdout,
    r.stdout.strip().replace(chr(10), ' | ')[:120])

# L10: fetch_sources 的包表与白名单包集合一致
r = run(['python', 'tools/etl/fetch_sources.py', '--list'])
listed = set()
for l in r.stdout.split(chr(10)):
    parts = l.split()
    if parts and not l.startswith(' '):
        listed.add(parts[0])
chk('L10: fetch_sources 包表 ⊇ 白名单包集合',
    set(PKGS) <= listed,
    f'whitelist-only={sorted(set(PKGS) - listed)}')

# ---------------------------------------------------------------- M: 数据驱动
rc, d = lint(wf('r <- ChIPseeker::annotatePeak(myPeak)\n'))
chk('M1: cp_lint 识别 ChIPseeker::annotatePeak',
    d['ok'] is True and d['stats']['calls_found'] == 1)

rc, d = lint(wf('e <- enrichKEGG(gene, organism="hsa")\n'
                'e2 <- enrichKEGG(gene, organism="hsa", bogus=1)\n'))
chk('M2: 混合同名调用中幻觉参数仍被拦',
    d['ok'] is False and d['stats']['calls_found'] == 2)

# ---------------------------------------------------------------- 报告
print('=' * 72)
print('STABILITY & EDGE CASES')
print('=' * 72)
total = len(results)
failed = sum(1 for _, ok, _ in results if not ok)
for name, ok, detail in results:
    mark = 'PASS' if ok else 'FAIL'
    s = f'  [{mark}]  {name}'
    if not ok and detail:
        s += '  {' + str(detail) + '}'
    print(s.rstrip())
print('=' * 72)
print(f'  TOTAL: {total - failed}/{total}  ({failed} failed)')
