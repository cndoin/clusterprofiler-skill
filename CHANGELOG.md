# Changelog · clusterprofiler-skill

所有重要变更都会记录在这里。本项目遵循 [Semantic Versioning](https://semver.org/)。

## [1.0.0] - 2026-10-01

### 新增（Added）
- 首次发布。事实底座从 `YuLab-SMU/clusterProfiler@devel`（4.21.2）解析：
  - **145 个 clusterProfiler 主包符号**（78 个 clusterProfiler 自有 + 67 个第三方 re-export）
  - **35 个 S3 method**（group_by/filter/arrange/... 的 enrichResult / compareClusterResult / gseaResult 分发）
  - **6 个 S4 method** + **1 个 S4 类**（groupGOResult / interpretation / ...）
  - 完整覆盖：ORA / GSEA / NSEA / MNSEA / 贝叶斯 / LLM 解读 / 多组学
- **核心工具**：
  - `tools/cp_lint.py` —— 静态校验 R 脚本（函数名 + 参数名 + 括号 + 引号 + 全角符号 + `...` 透传降级 + 弃用参数告警）
  - `tools/cp_api.py` —— 离线查真实签名（138 个带 formals）
  - `tools/cp_plan.py` —— 一句话需求 → 推荐流程（20 套任务模板）
  - `tools/selftest.py` —— 一键自检（fixtures + 文档代码块 + 工具冒烟 + 数据完整性，4 类 15 用例）
- **R 脚本**：
  - `scripts/preflight.R` —— 环境预检（输出 JSON，按 conda/cran/bioc/github 给出安装命令）
  - `scripts/run_cp.R` —— 统一执行入口（独立工作目录 + 日志重定向 + 结构化退出码）
- **参考文档**：
  - `references/api-signatures.md` —— 138 个函数真实签名（按模块分类，grep 用）
  - `references/function-index.md` —— 按模块 / S3 method / S4 method / S4 类分类
  - `references/workflows.md` —— 22 个完整流程代码模板（GO / KEGG / GSEA / 比较 / 离线 / LLM / NSEA / MNSEA / 贝叶斯 / PPI / Uniprot / DAVID / ...）
  - `references/pitfalls.md` —— 15 个常见坑（物种代码、ID 类型、网络、内存、编码、常见幻觉）
  - `references/environment.md` —— 安装 / 版本对齐 / 离线 / HPC / 性能调优
- **宿主兼容**：
  - `install.py` 支持 Claude Code（用户级 + 项目级）/ WorkBuddy / Codex / DeepSeek Hermes / 自定义目录
  - SKILL.md 顶端声明支持 5 个宿主
- **fixtures 测试用例**（5 个）：
  - `01_valid_basic.R` —— 干净脚本（PASS）
  - `02_hallucination.R` —— 3 个未知函数 + 2 个未知参数（精确捕获）
  - `03_valid_advanced.R` —— 复杂流程（不误报，含 compareCluster `...` 透传降级为 warning）
  - `04_syntax_error.R` —— 括号不闭合
  - `05_common_traps.R` —— 5 个常见陷阱（dotplot width=、bitr fromType WRONG、enricher 缺 TERM2GENE 等）

### 关键技术决策
- **结果一致性**：clusterProfiler 是 R 包，必须调用真实 R 才能保证结果一致。本技能
  的 R 脚本层（preflight / run_cp / workflows.md 模板）保证结果与上游完全一致。
- **结果一致性**：调用 enrichplot / enrichit / gson / org.*.eg.db 等真实 R 包。
- **防幻觉**：cp_lint 拦截 LLM 写 clusterProfiler 代码最常见的 10 个错
  （enrichGO2 / enrichKEGGG / dotplot split / interpret organism / 等）。
- **跨宿主**：用纯 Python 工具（无 MCP / 无网络核心工具）+ 标准库，
  任何支持目录型 skill 的 Agent 宿主都能用。
- **跨平台**：Bash + Python 3 标准库 + 跨平台路径约定（相对路径、ASCII 安全）。

### 已知限制
- 本机（Windows）默认未安装 R。技能本身不需要 R；但要真跑分析需要 R 4.2+ + Bioconductor。
- clusterProfiler KEGG API（api.kegg.jp）在国内网络经常超时；推荐走离线 GSON。
- LLM 解读功能需要 aisdk + OPENAI_API_KEY（或本地 ollama）。

### 下一步计划
- 跟踪 clusterProfiler 4.22+ 升级（当 4.22 发布后跑 `python3 tools/etl/rebuild.py`）
- 补充 DOSE / ReactomePA / meshes / MicrobiomeProfiler 等扩展包的函数到 whitelist
  （这些是 clusterProfiler 家族的下游包，本技能暂未覆盖）
- 加 GitHub Actions workflow（setup-r + Bioconductor + BiocParallel 缓存）