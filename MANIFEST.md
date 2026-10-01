# MANIFEST · 文件清单

> 本文件由 `tools/pack.py` 生成。手动编辑后必须跑 `python3 tools/pack.py` 重生成。

## 顶层文件

| 文件 | 大小 | 说明 |
| --- | --- | --- |
| `SKILL.md` | Agent 的常驻入口（决策路由 + 铁律 + 失败协议 + 宿主兼容） |
| `install.py` | 跨平台安装到各 Agent 宿主（claude / workbuddy / codex / deepseek） |
| `INSTALL.md` | 安装指南（Windows / macOS / Linux） |
| `CONTRIBUTING.md` | 改这个技能前必读 |
| `LICENSE` | MIT |
| `NOTICE` | 上游归属与许可证声明 |
| `CHANGELOG.md` | 变更日志 |
| `README.md` | 项目介绍与快速上手 |
| `MANIFEST.md` | 本文件 |

## references/

| 文件 | 大小 | 说明 |
| --- | --- | --- |
| `api-signatures.md` | 145 个函数真实签名（grep 用） |
| `function-index.md` | 按模块 / S3 method / S4 method / S4 类分类索引 |
| `workflows.md` | 22 个完整流程代码模板 |
| `pitfalls.md` | 15 个常见坑（物种 / ID / 内存 / 编码 / 幻觉） |
| `environment.md` | 安装 / 版本对齐 / 离线 / HPC / 性能调优 |

## scripts/

| 文件 | 说明 |
| --- | --- |
| `preflight.R` | 环境体检（版本 / 依赖 / 内存），输出 JSON |
| `run_cp.R` | 统一执行 R 脚本入口（独立工作目录 + 日志 + 退出码） |

## tools/

| 文件 | 说明 |
| --- | --- |
| `cp_lint.py` | 核心静态校验器（防幻觉） |
| `cp_api.py` | 离线查真实签名 |
| `cp_plan.py` | 一句话需求 → 推荐流程 |
| `selftest.py` | 一键自检（fixtures + 文档 + 工具 + 数据，4 类 15 用例） |
| `whitelist.json` | 事实底座（机器读） |
| `etl/fetch_sources.py` | 抓 clusterProfiler 上游源码 |
| `etl/build_api.py` | 解析 NAMESPACE + formals + alias + S4 + re-export |
| `etl/gen_docs.py` | 生成 references + whitelist.json |
| `etl/rebuild.py` | 一键重建事实底座 |

## tests/fixtures/

| 文件 | 期望 |
| --- | --- |
| `01_valid_basic.R` | exit 0, 0 errors（enrichGO + dotplot/cnetplot/barplot） |
| `02_hallucination.R` | exit 1, 3 unknown-function + 2 unknown-arg |
| `03_valid_advanced.R` | exit 0, 0 errors（GSEA / KEGG / compareCluster / merge / GSON / NSEA / interpret） |
| `04_syntax_error.R` | exit 1, syntax error（括号不闭合） |
| `05_common_traps.R` | exit 1, 1 unknown-arg + 1 warning（dotplot width / bitr fromType WRONG / ...） |

---

## 不进安装包（运行时生成 / 第三方依赖）

| 文件 / 目录 | 说明 |
| --- | --- |
| `.build/` | etl 抓取的源码缓存（按需重建） |
| `.git/` | git 历史（install.py 排除） |
| `__pycache__/` | Python 字节码（install.py 排除） |
| `.venv/` | 虚拟环境（install.py 排除） |