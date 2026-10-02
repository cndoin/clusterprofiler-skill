# clusterprofiler-skill · Y 叔全套 R 包生态 Agent Skill

给 AI Agent 用的 **Y 叔（YuLab-SMU）全套生物信息学 R 包**编排技能，让 Agent 写出的 R 代码**不出现幻觉函数、不出现幻觉参数**。

它不是一个 clusterProfiler 教程，也不是 API 文档的抄写件。它的全部事实来自**程序解析 38 个上游 R 包源码**
（每个包的 `NAMESPACE` + `R/*.R` 的真实 `formals` + `setMethod` + 别名赋值 + 第三方包 re-export），
并且任何交付前的 R 脚本都会被 `cp_lint.py` 静态校验器拦一遍。

- **覆盖范围**：生态 **38 个包 / 6137 个白名单键**（2384 个导出符号名 + 3753 个 `pkg::sym` 限定名；3087 个键带真实 formals）
- **核心包**：clusterProfiler 4.21.2 / enrichit / enrichplot / gson / DOSE / ReactomePA / meshes / GOSemSim / ChIPseeker / MicrobiomeProfiler / aPEAR / CBNplot / clusterProfiler.dplyr / aisdk / TCMDATA
- **生态包**：ggtree + treeio + ggtreeExtra + tidytree + MicrobiotaProcess + SVP + sclet + scMSGNN + ggsc + createKEGGdb + CNEr + aplot + ggmsa + ... 共 23 个
- 依赖：**零第三方包**，只用 Python 3 标准库 + 可选 R

---

## 为什么需要它

LLM 写 clusterProfiler 代码的典型翻车方式，不是逻辑错，是**编造 API**：

| 幻觉 | 真相 |
| --- | --- |
| `enrichGO2()` / `enrichKEGGG()` | 写错名，正确是 `enrichGO` / `enrichKEGG` |
| `compareCluster(fun="enrichGOO")` | fun 只接受 11 个合法字符串 |
| `enrichGO(fdr_method=)` | 参数名错，正确是 `pAdjustMethod` |
| `dotplot(split=...)` | dotplot 不接受 split；用 ggplot2 `facet_wrap` 拼版 |
| `organism = "Homo sapiens"` 喂给 enrichKEGG | KEGG 用三字母代码 `hsa`；学名只用于 WikiPathways |
| `interpret(..., organism=, provider=, api_key=)` | 4.21+ 重写了 interpret；这些参数已被移除 |
| `simplify` 当成普通函数调用 | `simplify` 是 S4 method（`exportMethods(simplify)`） |
| `gseGO` 不传 OrgDb | OrgDb 必需 |
| `bitr(fromType="WRONG")` | fromType 必须是 KEYTYPE 之一 |
| `dotplot(width=)` | width 不是 dotplot 参数 |

`cp_lint.py` 把这些都拦下来了。**没跑 lint 就提交 = 翻车。**

---

## 30 秒上手

```bash
# 1) 装到 Claude Code（用户级）
python3 install.py
#   WorkBuddy:  python3 install.py --host workbuddy
#   Codex:      python3 install.py --host codex
#   DeepSeek:   python3 install.py --host deepseek
#   项目级:     python3 install.py --project

# 2) 确认技能本身没坏
python3 tools/selftest.py          # 全绿（15/15 通过），退出码 0

# 3) 交付 R 代码前，必跑
python3 tools/cp_lint.py my_analysis.R --json
```

Windows 上若没有 `python3`，把命令里的 `python3` 换成 `python`。

---

## 三个工具

| 命令 | 作用 |
| --- | --- |
| `python3 tools/cp_lint.py <脚本.R>` | **核心**。静态校验：函数名是否存在（含拼写纠错建议）、参数名是否合法（`...` 透传降为 warning）、deprecated 参数告警、括号/引号配对、中文全角符号 |
| `python3 tools/cp_api.py enrichGO` | 离线查真实签名。`--search kegg` 模糊搜，`--module gsea` 列模块 |
| `python3 tools/cp_plan.py "<一句话需求>"` | 需求 → 推荐流程与函数序列（纯规则，不联网、不调 LLM） |

`cp_lint.py` 的退出码：`0` = 无 error；`1` = 有 error；`2` = 用法错误。
warning 不阻断（例如 `...` 透传、未装 library()），但要在回复里说明。

实测精度：干净脚本 **0 误报**；植入 6+ 个幻觉的脚本 **全捕获**。

---

## 目录结构

```
clusterprofiler-skill/
├── SKILL.md                  # Agent 的唯一常驻入口（决策路由 + 铁律 + 失败协议）
├── install.py                # 跨平台安装到各 Agent 宿主
├── INSTALL.md                # 安装指南（Windows / macOS / Linux）
├── MANIFEST.md               # 文件清单 + SHA-256（由 pack.py 生成）
├── LICENSE                   # MIT
├── NOTICE                    # 上游归属与许可证声明
├── CONTRIBUTING.md           # 改这个技能前必读
├── CHANGELOG.md
├── README.md
├── references/
│   ├── api-signatures.md     # 3731 个符号（38 包，按生态包分组，225KB）
│   ├── function-index.md     # 模块索引 + 跨包同名函数（86KB）
│   ├── ecosystem/<pkg>.md    # 38 个 mini 速查（每个包一份）
│   ├── workflows.md         # 22 个可直接改用的流程模板
│   ├── pitfalls.md          # 跨生态常见坑
│   └── environment.md       # 安装、版本对齐、离线与 HPC 场景
├── scripts/
│   ├── preflight.R          # 环境体检（版本/依赖/内存）
│   └── run_cp.R             # 批量执行 R 脚本（日志 + 退出码）
├── tools/
│   ├── cp_lint.py            # 核心校验器
│   ├── cp_api.py             # 签名查询
│   ├── cp_plan.py            # 流程规划
│   ├── selftest.py           # 一键自检（4 类 15 用例）
│   ├── pack.py               # 打包成 zip + tar.gz，强制 LF、生成 MANIFEST
│   ├── whitelist.json        # 事实底座（机器读）
│   └── etl/                  # 事实底座的重建链路
│       ├── rebuild.py        #   一键重建（抓源码 → 解析 → 生成）
│       ├── fetch_sources.py  #   抓上游源码（不依赖 git 二进制）
│       ├── build_api.py      #   解析 NAMESPACE + formals + alias + S4
│       └── gen_docs.py        #   生成 references + whitelist.json
└── tests/fixtures/*.R       # 5 个回归用例（含"作者踩过的坑"陷阱用例）
```

---

## 重建事实底座

`whitelist.json` 与 `references/*.md` 不是手写常量，全部可由上游源码重新生成：

```bash
python3 tools/etl/rebuild.py            # 抓源码 + 解析 + 生成
python3 tools/etl/rebuild.py --no-fetch # 用 .build/ 里已有的源码离线重建
python3 tools/etl/rebuild.py --ref v4.20.0   # 指定 clusterProfiler 版本
```

已验证的复现性：用同一份源码重建，`whitelist.json` 符号数 145 → 145（零增删），
`references/*.md` 五个文件 SHA-256 **逐字节一致**。

重建后必须跑 `python3 tools/selftest.py`。

---

## 宿主兼容性

只依赖 **Bash + Read + Grep**：不联网（核心工具全离线）、不依赖 MCP、不依赖任何宿主专有能力。
所有路径一律相对 skill 根目录书写，不含任何绝对路径。

| 宿主 | 位置 | 命令 |
| --- | --- | --- |
| Claude Code 用户级 | `~/.claude/skills/clusterprofiler-skill/` | `python3 install.py` |
| Claude Code 项目级 | `<项目>/.claude/skills/clusterprofiler-skill/` | `python3 install.py --project` |
| WorkBuddy | `~/.workbuddy/skills/clusterprofiler-skill/` | `python3 install.py --host workbuddy` |
| Codex | `~/.codex/skills/clusterprofiler-skill/` | `python3 install.py --host codex` |
| DeepSeek Hermes | `~/.deepseek/skills/clusterprofiler-skill/` | `python3 install.py --host deepseek` |
| 其它 | 自定义 | `python3 install.py --dir <skills 根目录>` |

---

## 能力边界（说清楚，不含糊）

- **能做**：选函数、写脚本、校验脚本、规划流程、解读报错、环境体检建议。
- **不能做**：在没有 R 的机器上真实跑 `Rscript` 出图出数。
  技能要求在这种情况下给用户三选一（本机装 R / 交服务器 / GitHub Actions），
  **并明确禁止假装跑过或编造任何数值结果**。

---

## 许可证与归属

本技能以 **MIT** 发布（见 `LICENSE`）。

它不隶属于 Y 叔 / YuLab-SMU，也不是 clusterProfiler 官方产物。事实底座派生自
[clusterProfiler](https://github.com/YuLab-SMU/clusterProfiler)（Artistic-2.0, © 2021-2026 Guangchuang Yu）
与
[enrichit](https://github.com/YuLab-SMU/enrichit)（Artistic-2.0）的源码，
仅提取接口性事实信息，不含上游实现代码。完整声明见 `NOTICE`。