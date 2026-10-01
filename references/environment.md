# clusterProfiler 环境搭建

> 安装 R + clusterProfiler + 所有依赖。
> 跨平台（Windows / macOS / Linux）。Windows 上强烈建议用 conda-forge 或 micromamba
> 走预编译二进制，避开 Rtools 编译地狱。

---

## 一、装 R（≥4.2.0）

### Windows（推荐：conda-forge / micromamba）

```bash
# 1) 装 micromamba（单文件、无需管理员）
#    https://github.com/mamba-org/micromamba#installation
# 2) 创建环境
micromamba create -y -n cp -c conda-forge r-base=4.4
micromamba activate cp
```

或者直接装 R 官方：https://cran.r-project.org/bin/windows/base/

### macOS

```bash
brew install r
```

### Linux（Ubuntu / Debian）

```bash
sudo apt-get update
sudo apt-get install r-base
```

---

## 二、装 Bioconductor（clusterProfiler 在 Bioconductor，不在 CRAN）

```r
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager", repos = "https://cloud.r-project.org")
BiocManager::install(version = "3.18")    # 配当前 R 版本
```

---

## 三、装 clusterProfiler 主包 + 所有依赖

```r
# 主包 + 核心依赖
BiocManager::install(c(
  "clusterProfiler", "enrichplot", "gson",
  "AnnotationDbi", "GO.db", "GOSemSim",
  "ggplot2", "dplyr", "magrittr", "rlang",
  "httr", "jsonlite", "yulab.utils",
  "igraph", "ggraph"
))

# 底层引擎（clusterProfiler 的依赖）
remotes::install_github("YuLab-SMU/enrichit")

# LLM 解读
remotes::install_github("YuLab-SMU/aisdk")

# 物种 OrgDb（按需）
BiocManager::install(c(
  "org.Hs.eg.db",    # 人
  "org.Mm.eg.db",    # 鼠
  "org.Dr.eg.db",    # 斑马鱼
  "org.Dm.eg.db"     # 果蝇
))

# MSigDB 注释
remotes::install_github("igordot/msigdbr")

# KEGG 数据库本地化（一次性，需联网）
gson_KEGG("hsa", KEGG_Type = "KEGG", keyType = "kegg")
saveRDS(gson_KEGG, "kegg_hsa.rds")
```

Windows 上 R 4.4 + Bioconductor 3.18 整套装好大约 **20-40 分钟**（取决于网速）。
Linux/macOS 通常快 2-3 倍。

---

## 四、验证环境

```r
library(clusterProfiler)
sessionInfo()$R.version$version.string   # R >= 4.2.0
packageVersion("clusterProfiler")        # >= 4.21.0
packageVersion("enrichit")
packageVersion("enrichplot")
```

或用本技能自带脚本：

```bash
Rscript scripts/preflight.R --json
```

缺哪个包会自动列出 + 给出**可直接复制**的安装命令（conda / BiocManager / GitHub 区分来源）。

---

## 五、跑 sample 验证 R / clusterProfiler 没坏

```r
library(clusterProfiler)
data(geneList, package = "DOSE")
gene <- names(geneList)[abs(geneList) > 2]
ego <- enrichGO(gene, OrgDb = org.Hs.eg.db,
                keyType = "ENTREZID", ont = "BP")
head(as.data.frame(ego))
# 不空 = OK
```

---

## 六、不在本机装 R 的替代方案

| 方案 | 适用场景 | 代价 |
| --- | --- | --- |
| 1. 本机装 R + Bioconductor | 自己做实验，数据小 | 20-40 分钟首次装 |
| 2. Linux 服务器 / HPC | 数据大 / 跑批量 | 需 SSH / 集群账号 |
| 3. Colab / Kaggle | 临时性、轻量 | 单次 session 重启就丢 |
| 4. GitHub Actions | CI 化、可复现 | 每次 push 触发，需缓存 |

**本技能本身不需要 R**（校验器是纯 Python）。只在真要跑分析时才需要 R。
**不要在没有 R 的环境下假装跑过**。

---

## 七、conda 单一环境方案（Windows / Linux / macOS 通用）

```bash
micromamba create -y -n cp -c conda-forge -c bioconda \
    r-base=4.4 \
    r-clusterprofiler \
    r-org.hs.eg.db \
    r-dplyr \
    r-ggplot2 \
    r-gosemsim

micromamba activate cp
```

注：conda 上的 clusterProfiler / org.Hs.eg.db 经常落后 Bioconductor release 半年到一年；
新功能（如 GSON 接收）可能不在。生产环境建议直接走 BiocManager。

---

## 八、离线 / 内网场景

1. **KEGG 离线**：用 `gson_KEGG("hsa")` 把 KEGG 缓存为本地 RDS，存 U 盘 / 内网共享盘。
2. **GO 离线**：`gson_GO(org.Hs.eg.db, ont = "BP")` 同样保存。
3. **包离线**：在有网的机器上 `BiocManager::install()`，把
   `library/R/3.5/site-library/`（或 `lib/R/site-library/`）整个目录打包带走。
4. **MSigDB 离线**：`msigdbr::msigdbr()` 缓存本地。

---

## 九、常见安装错误

| 症状 | 原因 | 解决 |
| --- | --- | --- |
| `package 'X' is not available` | 没装 Bioconductor 源 | `BiocManager::install(...)` |
| `compilation failed` | 没装 Rtools / gcc | Windows 走 conda-forge；Linux `apt install r-base-dev` |
| `SSL certificate problem` | 网络证书过期 | `options(repos = "https://cloud.r-project.org")` |
| `dependency not available: enrichit` | enrichit 不在 CRAN | `remotes::install_github("YuLab-SMU/enrichit")` |
| `cannot remove installed package` | 多版本冲突 | `remove.packages("clusterProfiler"); BiocManager::install("clusterProfiler")` |
| 安装到一半卡住 | R 4.4 + Bioconductor 3.18 没对应包 | 升 / 降 R 版本到 4.3.x |

---

## 十、性能调优

```r
# 并行（用 future，跨平台；clusterProfiler 的 enrichit C++ 后端已内部并行）
library(future)
plan(multisession, workers = 4)        # 跨平台；Linux 上可改 plan("multicore", workers = 4)

# 大数据集先抽样
set.seed(42)
if (length(gene) > 5000) gene <- sample(gene, 5000)

# 限制 GSEA permutation
gseGO(..., nPerm = 1000)        # 默认值；想精确改 10000

# 过滤大基因集
gsfilter(ego, by = "GSSize", min = 10, max = 200)
```

---

## 十一、版本对齐（重要）

| R | Bioconductor | clusterProfiler |
| --- | --- | --- |
| 4.4 | 3.18 | 4.10+ |
| 4.3 | 3.17 | 4.8+ |
| 4.2 | 3.16 | 4.6+ |

本技能事实底座生成自 **4.21.2 devel**（最新版本，含 4.21 系列的新 GSON / enrichit 接口）。
如果用户机器上装的 clusterProfiler < 4.10，会少一些函数（特别是 enrichit / aisdk / nseaGO 等），
cp_lint 仍能正常校验（以事实底座为准，但运行时找不到函数）。