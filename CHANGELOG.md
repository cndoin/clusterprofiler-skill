# Changelog · clusterprofiler-skill

所有重要变更都会记录在这里。本项目遵循 [Semantic Versioning](https://semver.org/)。

## [2.1.0] - 2026-10-01

### 重大修复（完整性与稳定性审计）

对 v2.0.0 做了一轮以「量事实、不靠声明」为准的审计，修掉 7 个真实缺陷。
审计口径：`python .build/edge_audit.py`，从 41 项检查 0 通过起步，现 41/41 全绿。

#### 修复（Fixed）

- **6 个包抓取静默失败**：`aplot` / `tidytree` / `ggbreak` / `ggimage` / `ggtangle` /
  `createKEGGdb` 只有 `master` 或 `main` 分支，脚本却一律按 `devel` 抓 → 404 →
  产出 0 字节 DESCRIPTION/NAMESPACE。改为按 `devel → master → main → HEAD` 自动探测。
- **ref 探测方法本身是错的**：原来用 `raw.githubusercontent.com/<repo>/<ref>/DESCRIPTION`
  判断 ref 是否存在，但对不存在的 ref 该端点会**静默回退到默认分支并返回 200**，
  于是抓回「有 NAMESPACE、零个 R 文件」的半残包。改用 `codeload` 的 HTTP HEAD 探测
  （不存在的 ref 老实报 404）。这一条是上面 6 个包能真正修好的前提。
- **`aPEAR` 仓库名错误**：`YuLab-SMU/aPEAR` 不存在，真实上游是 `ievaKer/aPEAR`。
- **`CNEr` 根本不在 GitHub**：它是 Bioconductor 包（1.49.1）。新增 Bioconductor
  源码 tarball 抓取路径（`bioc:<Pkg>`），该包从 0 个符号变成 249 个。
- **`HDO` 无公开源码**：GitHub 与 Bioconductor 均无仓库，已从事实底座移除并在
  `fetch_sources.KNOWN_UNAVAILABLE` 里显式登记，不再产出空 stub 冒充覆盖。
- **失败不再被吞掉**：`fetch_repo` 原来把每个文件的异常都 catch 成一行 WARN 然后正常返回，
  所以「36 个成功 / 0 个失败」是假的（实际 9 个包是空的）。现在抓完会验收
  NAMESPACE 非空且 R 文件数 > 0，不达标即记失败、退出码 1，`rebuild.py` 随之中断。
- **`build_api.py` 把 NAMESPACE 注释当成了符号名**：CNEr 的 NAMESPACE 是
  「多行块 + 块内文件注释」风格，原正则 `[^)]` 会吃掉换行，把 `## AllClasses.r` 这类
  注释写进白名单（实测污染 25 个键）。改为「剥注释 → 合并续行 → 校验符号名合法」。
- **`pkg::fn` 跨包调用被整体跳过**：`cp_lint` 原来遇到 `pkg not in
  (clusterProfiler, enrichit, enrichplot)` 就 `continue`，导致 1325 个 `pkg::sym`
  白名单键形同虚设 —— `ChIPseeker::annotatePeakxx()` 这种幻觉调用被判为通过。
  现在按白名单里的生态包集合精确路由：生态内校验（限定名优先、短名兜底），
  生态外（dplyr / ggplot2 等）放行。
- **参数校验把「没有证据」当成「证据表明不存在」**：约 975 个键只有导出名、
  没解析到 formals，原来会对此类符号做参数校验，把 `diversity(x, index="shannon")`、
  `plotCov(x, col="red")` 这类**正确代码**判成错误。现在空 args 不做参数校验，
  改计入 `stats.args_unverified` 如实暴露覆盖率。
- **`by = list(...)` 被解析成 `bylist()`**：`scan_calls` 在 `=` 处不 flush 标识符，
  左值名与右值标识符粘连，既丢掉真实的 `list()` 调用又凭空多报一个 unknown-function。
- **`aggregate(x, by=)` 等按名传参的正确写法曾被误报**（同上根因）。
- **`gen_docs.py` 用构建目录名当包名**：clusterProfiler 的构建目录是 `.build/clusterprofiler`
  （小写，v1.0 遗留），文档被写成 `ecosystem/clusterprofiler.md`，与其余包命名不一致。
  Windows 文件系统大小写不敏感所以本机看不出来，到 Linux 才会炸。改为取
  `api_full.json` 的 `package` 字段，并自动清理已移除包（HDO/TCMDATA 旧档）的残留文档。
- **`rebuild.py` 的「一键全量重建」是假的**：它调的是 `fetch_sources.py --ref devel`
  （只抓 clusterProfiler 单包）和 `build_api.py`（无 `--all`），产出的 whitelist
  只含 1 个包，与发布版完全对不上。改为 `--all` + `--all --merge`。
- **`generated_from.source` 是硬编码的假信息**（写死 `YuLab-SMU/<多个包>@devel`）。
  现在 `fetch_sources` 为每个包落一份 `source.json`，whitelist 的
  `generated_from.sources` 记录逐包真实 repo/ref。
- **审计脚本自身的假通过**：`.build/edge_audit.py` 在
  `with NamedTemporaryFile(...)` 块内直接调子进程，`f.write` 还在用户态缓冲，
  子进程读到的是空文件 —— 空文件恰好也判 ok，于是「未闭合括号」等用例静默假通过。
  改为先落盘再交给子进程，并给每个用例补上内容证据断言（如 `calls_found` / `cp_calls_checked`）。

#### 变更（Changed）

- 覆盖包数 37 → **38**：新增 `CBNplot`、`TCMDATA`、`clusterProfiler.dplyr`；
  移除 `HDO`（无公开源码，已登记）。白名单 2458 → **6137** 键；**零符号包从 9 个降到 0 个**。
- `SKILL.md` 路由表按白名单订正：删掉 20+ 个不存在的函数名
  （`CNE_range` / `RunSVP` / `summarize_taxa` / `peakAnno` / `enrichHDO` /
  `meshHyperGTest` / `networkPlot` / `run_SCSeed` / `wp_profile` / `upsetplot` 等），
  改用真实导出名。技能包的文档不得违反它自己的第一规则。
- `cp_lint` 新增 `stats.args_unverified`，人类可读输出同步展示。

## [2.0.0] - 2026-10-01

### 重大变更（Ecosystem Expansion）

复刻 Y 叔（YuLab-SMU）全套 R 包生态：**37 个生态包 / 2458 个符号 / 987 个带 formals**。

#### 新增（Added）

- **覆盖包清单**（37 个，按用途分类）：
  - P0 富集核心：clusterProfiler / enrichit / enrichplot / gson / DOSE / ReactomePA / meshes / GOSemSim / ChIPseeker / MicrobiomeProfiler / HDO / aPEAR / aisdk
  - P1 系统发育：ggtree / treeio / ggtreeExtra / tidytree
  - P1 微/单细胞/空间：MicrobiotaProcess / SVP / sclet / scMSGNN / ggsc
  - P1 数据库/工具：createKEGGdb / CNEr / yulab.utils
  - P2 科研绘图：aplot / ggimage / ggtangle / ggbreak / ggmsa / ivolcano
  - P2 疾病/表观：tigeR / wikiprofiler / epiSeeker
  - P2 工具：scholar / seqmagick
- **etl 链路重写**：
  - `tools/etl/fetch_sources.py`：支持 `--all` / `--pkg X` / per-package ref（含 main / master / devel 自适应）
  - `tools/etl/build_api.py`：通用 R 解析器（每个包独立 build）+ `merge_all_whitelist` 合并多包 + THIRD_PARTY_PARAMS 注入（覆盖 msigdbr / build_kegg_graph / simplify 等无 importFrom 的常用函数）
  - `tools/etl/gen_docs.py`：按生态包分组生成 `references/api-signatures.md`（110KB）+ `references/function-index.md`（27KB）+ `references/ecosystem/<pkg>.md`（37 份 mini 速查）
- **新增生态专属文档**：37 份 `references/ecosystem/<pkg>.md`（每个包一份函数列表 + 触发场景）
- **SKILL.md 扩展**：
  - description 关键词扩展到所有 37 个包
  - 新增「生态包路由」章节（37 包按场景映射：用户场景 → 包 → 函数）
- **whitelist.json 扩容**：从 145 → 2458 符号（1325 带 `pkg::sym` 前缀 + 1133 单名）
- **fixtures 适应新 cp_lint**：`...` 透传降级为 warning 后，EXPECT 表更新（fixture 02: unknown-arg 减 1；fixture 05: 改 0 errors）

#### 修复（Fixed）

- `cp_lint` 兼容 `datacharacter` 为 dict 时崩溃（args 现在统一为 list of str）
- `cp_lint` 换行处不 flush ident 的 bug（之前会拼出 `log2fcnames` 这种鬼函数名）
- `cp_lint` 把 `compareCluster(OrgDb=, ont=)` 错误地当 unknown-arg；现在 `...` 透传降级为 warning
- `cnetplot(categorySize=)`（兼容别名）以前补进 NOTES_PARAMS
- merge_all_whitelist 短名优先选 args 最完整的版本（避免 clusterProfiler 包先跑占位空 args 覆盖 enrichit 的完整 args）
- build_api.py FN_RE 支持 `<-` 和 `=` 两种赋值风格（修复 gson_KEGG_mapper 等的解析）
- build_api.py 处理 exportMethods(...)、alias 赋值（name <- alias）、S4 method dispatch

#### 技术细节

- `tools/whitelist.json` 格式：`{generated_from: {format_version: "ecosystem-1.0"}, symbols: {pkg::sym 或 sym: {pkg, args, ecosystem_pkg, ecosystem_module, ...}}}`
- `references/api-signatures.md` 110KB，按生态包分组（37 个 section），可 grep `^### <func-name>` 定位
- `references/function-index.md` 27KB，含跨包同名函数索引（同符号被多包 re-export 时提示）
- `references/ecosystem/<pkg>.md` 37 份，每份列该包 export 列表 + 函数签名速查

#### 自检状态

- **fixtures 5/5 PASS**：01_valid_basic / 02_hallucination / 03_valid_advanced / 04_syntax_error / 05_common_traps
- **文档代码块**：44 个 block，0 bad
- **工具冒烟 5/5**：cp_api / cp_plan / 拒识别 / --search / --list
- **数据完整性 4/4**：size >= 140 / 关键符号 / generated_from / 12 modules (ora/gsea/viz/semantic/disease/reactome/mesh/phylo/microbiome/chippeak/singlecell/spatial)
- **总计 15/15 全绿**

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