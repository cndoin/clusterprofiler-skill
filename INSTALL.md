# 安装指南（Windows / macOS / Linux 通用）

clusterprofiler-skill 是**纯文本技能包**：Python 只用标准库，R 脚本只依赖 clusterProfiler。
没有二进制、没有编译步骤，解压即用。

---

## 一、安装到 Agent 宿主

### Claude Code

```bash
# 用户级（全局生效）
python3 install.py

# 项目级（只对当前项目生效）
python3 install.py --project
```

### WorkBuddy

```bash
python3 install.py --host workbuddy
```

### Codex

```bash
python3 install.py --host codex
```

### DeepSeek Hermes

```bash
python3 install.py --host deepseek
```

### 其它宿主 / 自定义位置

```bash
python3 install.py --dir <你的 skills 根目录>
```

Windows 上如果没有 `python3`，把命令里的 `python3` 换成 `python`。
装完**重启 Agent 宿主**，让它重新扫描 skills 目录。

---

## 二、准备 R 环境（要真跑分析才需要）

技能的核心校验器 `tools/cp_lint.py` **不需要 R**，装完就能用。
只有"真的要执行 R 脚本出图出数"才需要下面这步。

### 推荐：conda-forge / micromamba（三平台统一，免编译）

```bash
# 1) 装 micromamba（单文件、无需管理员）
#    https://github.com/mamba-org/micromamba#installation

# 2) 一次装齐 R + clusterProfiler 生态
micromamba create -y -n cp -c conda-forge -c bioconda \
    r-base=4.4 \
    r-clusterprofiler \
    r-org.hs.eg.db \
    r-dplyr \
    r-ggplot2 \
    r-gosemsim

micromamba activate cp
```

### 各平台替代方案

| 平台 | 方式 | 命令 |
|---|---|---|
| Windows | conda-forge（推荐） | 见上 |
| macOS | Homebrew + CRAN | `brew install r` 然后 R 里 `install.packages(...)` |
| Linux | apt / conda | `apt install r-base` 或 conda-forge |
| 任意 | 官方安装包 | https://cran.r-project.org/ |

### Bioconductor 安装

```r
# clusterProfiler 是 Bioconductor 包，不在 CRAN
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager", repos = "https://cloud.r-project.org")
BiocManager::install(c(
    "clusterProfiler", "enrichplot", "gson",
    "AnnotationDbi", "GO.db", "GOSemSim",
    "ggplot2", "dplyr", "magrittr"
))

# 底层引擎（GitHub）
remotes::install_github("YuLab-SMU/enrichit")
remotes::install_github("YuLab-SMU/aisdk")        # LLM 解读用
remotes::install_github("igordot/msigdbr")       # MSigDB 集合

# 物种 OrgDb
BiocManager::install("org.Hs.eg.db")              # 人 / 鼠 / 斑马鱼 / 果蝇 / ...
```

### 验证环境

```bash
Rscript scripts/preflight.R          # 人读
Rscript scripts/preflight.R --json  # 机器可读
```

缺包时它会**直接打印可复制的安装命令**（按 conda / CRAN / Bioconductor / GitHub 区分来源）。

---

## 三、验证技能本身

```bash
python3 tools/selftest.py        # 全绿（19/19），退出码 0
```

它会跑四类检查：fixtures 回归、文档代码块、工具冒烟、数据完整性。

---

## 四、日常使用

```bash
# 写完 R 脚本后必跑（error 必须为 0）
python3 tools/cp_lint.py my_analysis.R

# 查真实函数签名
python3 tools/cp_api.py enrichKEGG
python3 tools/cp_api.py --search kegg

# 一句话需求 -> 推荐流程
python3 tools/cp_plan.py "GO 富集 + GSEA 跑 KEGG"

# 真实执行（需要 R + 集群机器）
Rscript scripts/run_cp.R --script my_analysis.R --workdir runs/pbmc01
```

---

## 五、系统要求

| 项 | 要求 |
|---|---|
| Python | 3.7+（**只用标准库**，无需 pip install 任何东西） |
| R（可选） | 4.2+ + Bioconductor 3.16+ |
| 操作系统 | Windows 10+ / macOS / Linux（跨平台，无平台专属代码） |
| 内存 | 8 GB 起；富集分析一般 < 4 GB |
| 网络 | 离线环境也能用（推荐走 GSON 离线数据库） |

---

## 六、常见问题

**Q：`python3` 找不到？**
Windows 用 `python`。技能里所有命令写 `python3` 是为了跨平台统一。

**Q：`tools/selftest.py` 报某个函数不存在？**
上游 clusterProfiler 新增了导出。跑 `python3 tools/etl/rebuild.py` 重建事实底座。

**Q：装到一半报 `Permission denied`？**
目标 skills 目录没有写权限。用 `install.py --dir <可写目录>` 指到用户目录。

**Q：R 脚本跑不起来？**
先 `Rscript scripts/preflight.R`，看缺哪个包，按它打印的命令装。

**Q：LLM 解读报 `aisdk not found`？**
`remotes::install_github("YuLab-SMU/aisdk")`

**Q：KEGG 网络失败？**
国内网络常态。改用 `gson_KEGG("hsa")` + `enrichKEGG(organism=gson)` 离线模式。

**Q：文档代码块里有几个总是 FAIL？**
检查是不是反面示例（前一段 markdown 含 "BAD:"/"错误" 等关键词就会自动跳过）。
如果某块应该跳但没跳，加 `# BAD:` 前缀或修改 selftest.py 的 NEGATIVE_HINT。
