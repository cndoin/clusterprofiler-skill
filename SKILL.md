---
# clusterprofiler-skill · 必需字段（Claude Agent Skill 官方规范）
name: clusterprofiler-skill
description: "Y 叔（YuLab-SMU）全套生物信息学 R 包生态的 Agent 技能，覆盖 37 个包 / 2458 个符号：clusterProfiler 4.21.x（GO/KEGG/WikiPathways/KEGG Module/PathwayCommons/DAVID/MSigDB/enricher 富集分析，ORA/GSEA/NSEA/MNSEA/网络拓扑/贝叶斯 term 选择/LLM 解读）、enrichit（C++ 富集引擎，aggregate_enrichment/bayes_enrich/harmonize_ids/setReadable/nseGO/nseKEGG/mnsea/ora/gsea）、enrichplot 可视化（dotplot/cnetplot/emapplot/gseaplot/ridgeplot/heatplot/goplot/upsetplot）、gson 知识表示、DOSE（Disease Ontology/NCG/DisGeNET 疾病注释）、ReactomePA（Reactome pathway 分析）、meshes（MeSH 富集）、GOSemSim（GO 语义相似度，含 mgoSim/godata）、ChIPseeker（ChIP-seq/ATAC-seq peak 注释）、MicrobiomeProfiler（微生物组富集）、HDO（Human Disease Ontology）、aPEAR（网络富集装饰）、aisdk（LLM 集成）、ggtree + treeio + ggtreeExtra + tidytree（系统发育树全套）、MicrobiotaProcess（微生物组深度分析）、SVP（空间转录组）+ ggsc、sclet + scMSGNN（单细胞）、createKEGGdb + CNEr（KEGG/CNE 数据库）、aplot + ggimage + ggtangle + ggbreak + ggmsa + ivolcano（科研绘图）、yulab.utils、msigdbr（MSigDB）、epiSeeker（表观遗传）、tigeR（肿瘤免疫）、scholar（学者引用）。完整覆盖 ID 转换（bitr/bitr_kegg）、离线 GSON、KEGG Module 富集、PPI 网络（STRING）、Uniprot 查询、4 大知识源（GO/KEGG/Reactome/DO/MeSH/MSigDB）。事实底座从上游源码 NAMESPACE + R/*.R 真实 formals 解析，cp_lint 自动拦截 LLM 写 R 代码时最常见的 10 类幻觉函数 / 幻觉参数 / 拼写错误 / 全角符号 / 括号不匹配。"
# 下方为 WorkBuddy 宿主扩展字段；Claude Code 会忽略（不报错、不影响解析）。
license: MIT
version: 2.0.0
allowed-tools: Bash, Read, Grep, Glob
agent_created: true
---

# clusterprofiler-skill · Y 叔全套 R 包生态编排技能

面向 **37 个 YuLab-SMU 生态包**（事实底座取自每个上游仓库 `devel` 分支的 NAMESPACE + R/*.R 真实 formals + 手工核对的第三方包 formals）。

本技能负责：**选对函数 → 写对参数 → 校验脚本 → 编排流程 → 解读报错**。
不负责替用户猜数据、猜基因、猜物种 —— 那些必须由用户给或从结果里读。

---

## 一、不可违反的事实（违反 = 交付幻觉代码）

1. **任何一个 clusterProfiler 函数名，必须能在 `tools/whitelist.json` 里查到。**
   白名单是从 NAMESPACE + R/ 源码解析出的 145 个真实符号，加上 enrichplot / dplyr /
   magrittr / enrichit / ggplot2 / aisdk 等 re-export 函数共 165 个 known symbols。
   交付任何 R 代码前，**必须**跑 `tools/cp_lint.py`，把 error 清零。
   这是本技能存在的第一理由：clusterProfiler 是 LLM 幻觉重灾区。

2. **已知高频幻觉函数（源码里根本没有，见到立即改掉）**

   | 幻觉写法 | 真实情况 |
   | --- | --- |
   | `enrichGO2()` / `enrichKEGGG()` | 写错名，正确是 `enrichGO` / `enrichKEGG` |
   | `get_pathway_plot()` | 不存在。点图/网络图统一走 `dotplot()` / `cnetplot()` / `emapplot()`（来自 enrichplot） |
   | `dotplot(split=...)` | dotplot 不接受 `split`；分面用 ggplot2 `facet_wrap()` 拼版 |
   | `barplot(ego)` | ego 不是 barplot 输入；用 `barplot()` 或 `dotplot(ego)` |
   | `compareCluster(fun="enrichGOO")` | fun 只接受 "enrichGO" / "enrichKEGG" / "enrichWP" / "enrichMKEGG" / "enrichPC" / "enrichDAVID" / "enricher" / "gseGO" / "gseKEGG" 等 |
   | `enrichGO(fdr_method=...)` | 参数名错，正确是 `pAdjustMethod` |
   | `bitr(fromType="WRONG_TYPE")` | fromType 必须是 KEYTYPE 之一（SYMBOL / ENTREZID / ENSEMBL / UNIPROT ...） |
   | `organism = c("hsa", "mmu")` | enrichKEGG / gseKEGG 的 organism 只接受单个物种代码 |

3. **enrichGO 的 ont 默认是 `"MF"`，不是 `"BP"`。** 真要用 BP 必须显式写。

4. **enrichKEGG 的 organism 是三字母 KEGG 代码（"hsa" / "mmu" / "dre"），不是 Latin 学名。**
   WikiPathways 的 organism 是学名（"Homo sapiens" / "Mus musculus"）—— 两者**完全不同的命名体系**。
   拿 Latin 学名喂给 `enrichKEGG()` 会被 KEGG 当 UNKNOWN 处理，结果全空。

5. **`compareCluster()` 把不在 formals 里的参数（如 `OrgDb` / `ont`）通过 `...` 透传给 `fun`。**
   cp_lint 收到这种参数会降级为 warning（而不是 error），但**用户必须保证透传目标函数确实接受它**。

6. **`simplify()` 是 S4 method（`exportMethods(simplify)`），不是普通函数。**
   接收 `enrichResult / gseaResult / compareClusterResult` 会触发 S4 dispatch。

7. **网络感知函数（`nseGO` / `nseKEGG` / `mnseGO` / `mnseKEGG`）必须传 `graph` / `graphs`。**
   不传 = 必报错。

8. **interpret(x, ...) 的真实签名**：`x, context, n_pathways, model, task, prior, add_ppi, gene_fold_change, max_tokens, temperature, verbose`
   **不接受 `organism=` / `provider=` / `api_key=`**（这些是早期 API）。LLM 默认走 `aisdk` 后端，api_key 走环境变量 `OPENAI_API_KEY`。

9. **enrichit 是 clusterProfiler 的底层引擎。** `aggregate_enrichment` / `aggregate_omics`
   / `bayes_enrich` / `bayes_summary` / `gsfilter` / `harmonize_ids` /
   `select_features_for_ora` / `setReadable` 由 enrichit 提供，clusterProfiler 在 export() 里
   re-export，**用户脚本里直接写这些名字即可**（无需 `enrichit::xxx`）。

10. **绝不臆造的东西**：物种代码（人 hsa / 鼠 mmu / 斑马鱼 dre）、基因 ID 类型（SYMBOL /
    ENTREZID / ENSEMBL）、OrgDb 名（人 org.Hs.eg.db / 鼠 org.Mm.eg.db / 斑马鱼 org.Dr.eg.db）、
    pathway 来源（KEGG / Reactome / WikiPathways / MSigDB category 名）。这些只能来自用户输入
    或 `search_kegg_organism()` / `get_wp_organisms()` 实际探测。

---

## 二、标准动作序列（先按这个走）

```
1. 明确任务类型   → tools/cp_plan.py "<一句话需求>"  给出推荐流程
2. 查真实签名     → python tools/cp_api.py <函数名>   或 grep references/api-signatures.md
3. 写 R 脚本      → 每个任务一个独立工作目录 + 独立 .R 文件
4. 强制校验       → python tools/cp_lint.py <script.R> --json   （error 必须 0）
5. 环境检查       → Rscript scripts/preflight.R --json          （有 R 的机器上）
6. 执行           → Rscript scripts/run_cp.R --script <file> --workdir <dir>
7. 读结果         → 从输出文件读数字，不靠复述
```

**第 4 步不能跳。** 没跑校验就说"脚本写好了"，等于没验证。

---

## 三、生态包路由（37 包按用途归类）

按用户的实际问题路由到对应包：

| 用户场景 | 该用包 | 关键函数 |
|---|---|---|
| GO / KEGG / 通路 ORA / GSEA | **clusterProfiler** | `enrichGO` / `enrichKEGG` / `gseGO` / `gseKEGG` / `compareCluster` |
| Disease / NCG / DisGeNET 注释 | **DOSE** | `enrichDO` / `gseDO` / `enrichNCG` / `gseNCG` / `enricher` (DisGeNET) |
| Reactome 通路 | **ReactomePA** | `enrichPathway` / `gsePathway` |
| MeSH 富集 + 语义 | **meshes** | `enrichMeSH` / `gseMeSH` / `meshHyperGTest` |
| GO term / gene 相似度 | **GOSemSim** | `godata` / `mgoSim` / `geneSim` / `Wang` / `Rel` |
| C 富集分析（GO+KEGG+其他） | **clusterProfiler::enricher** + GMT 文件 | `read.gmt` + `enricher` |
| ChIP-seq / ATAC-seq peak 注释 | **ChIPseeker** | `annotatePeak` / `peakAnno` / `makeTxDbFromGFF` / `covplot` / `getGEO` |
| 微生物组功能富集 | **MicrobiomeProfiler** | `taxaMe` + Shiny App |
| 人类疾病本体（HDO） | **HDO** | `enrichHDO` / `gseHDO` |
| 富集结果网络化 | **aPEAR** | `enrichmentNetwork` / `networkPlot` |
| 网络感知 GSEA | **enrichit** | `nseGO` / `nseKEGG` / `mnseGO` / `mnseKEGG` |
| 贝叶斯 term 选择 | **enrichit** | `bayes_enrich` / `bayes_summary` |
| 多组学聚合 | **enrichit** | `aggregate_enrichment` / `aggregate_omics` / `harmonize_ids` |
| ID 映射 | **clusterProfiler / DOSE / ReactomePA / meshes** | `bitr` / `bitr_kegg` / `bitr_dgn` |
| 富集结果可视化 | **enrichplot** | `dotplot` / `cnetplot` / `emapplot` / `gseaplot` / `ridgeplot` / `heatplot` |
| 系统发育树绘制 | **ggtree** + treeio | `ggtree` / `ggtree` + GROSS 文件 / `rotate` / `collapse` |
| 系统发育树 + 子图 | **ggtreeExtra** | `geom_fruit` / `geom_inset` |
| 微生物组数据 | **MicrobiotaProcess** | `summarize_taxa` / `alpha_diversity` / `beta_diversity` |
| 空间转录组高变特征 | **SVP** | `RunSVP` / `spatial_heatmap` |
| 空间 / 单细胞可视化 | **ggsc** | `SpatialMap` / `CellDifferentiogram` |
| 单细胞分类 / 聚类 | **sclet** | `run_SCSeed` / `run_PRESS` |
| 单细胞 GNN 整合 | **scMSGNN** | `scMSGNN` |
| KEGG 数据库构建 | **createKEGGdb** | `create_kegg_db` |
| CNE（非编码元件）数据库 | **CNEr** | `CNE_range` / `CNErscan` |
| 进化保守非编码元件 | **CNEr** + **ggtree** | 结合使用 |
| 火山图 | **ivolcano** | `ivolcano` |
| 轴断点 | **ggbreak** | `scale_x_break` / `scale_y_break` |
| 多序列比对 | **ggmsa** | `ggmsa` |
| 装饰图 | **aplot** | `plot_list` / `insert_top` |
| 图中加图 | **ggimage** | `geom_subview` |
| 网络图 / 关联图 | **ggtangle** | `ggtangle` |
| 肿瘤免疫 | **tigeR** | `tigeR` / `receptor_clonotype` |
| Wiki 注释 | **wikiprofiler** | `wp_profile` |
| 表观遗传峰 | **epiSeeker** | `epiStat` / `diffBind` |
| 学者引用分析 | **scholar** | `get_profile` / `get_citation_history` |
| 序列处理 | **seqmagick** | `fa_mask` / `fa_rc` |
| 中文医案数据 | **TCMDATA** | `TCM_API` |
| 通用工具 | **yulab.utils** | `yread` / `get_fun_from_pkg` / `user_dir` |
| 离线 GSON 数据库 | **gson** | `gson_GO` / `gson_KEGG` / `read.gmt` |
| LLM 解读 | **aisdk** | `Agent` / `ChatSession` / `generate_object` |

---

## 四、任务 → 流程路由表

| 用户要什么 | 关键函数序列（顺序不能乱） |
| --- | --- |
| GO BP/CC/MF 过表示分析 | `bitr(SYMBOL→ENTREZID)` → `enrichGO(ont=)` → `dotplot` / `barplot` / `cnetplot` |
| GO 全部 ontology 合并 | `enrichGO(ont="ALL")` |
| KEGG 通路 ORA | `bitr_kegg` → `enrichKEGG(organism="hsa")` → `dotplot` / `browseKEGG` |
| KEGG 离线（无网） | `gson_KEGG("hsa")` → `enrichKEGG(organism=gson)` |
| WikiPathways | `enrichWP(organism="Homo sapiens")` |
| KEGG Module | `enrichMKEGG(organism="hsa")` |
| PathwayCommons | `enrichPC(pathway="reactome_pathway")` |
| DAVID 在线 | `enrichDAVID(idType=, davidUser=)` |
| 通用 ORA（自备注释） | `enricher(gene, TERM2GENE=, TERM2NAME=)` |
| GSEA（GO） | `gseGO(gl, OrgDb=, ont=, keyType=)` |
| GSEA（KEGG） | `gseKEGG(gl, organism="hsa", keyType="kegg")` |
| GSEA（MSigDB） | `msigdbr(species, category)` → `GSEA(gl, TERM2GENE=gmt)` |
| 多组学比较 | `compareCluster(entrez~cluster, data=, fun="enrichGO")` → `dotplot(ck)` |
| 多组学合并 | `merge_result(list(A=ek1, B=ek2))` |
| ID 转换 | `bitr(gene, fromType, toType, OrgDb=)` 或 `bitr_kegg(gene, fromType, toType, organism=)` |
| ID 转换结果转 SYMBOL | `setReadable(ego, OrgDb=, keyType="ENTREZID")` |
| 离线 GO 数据库 | `gson_GO(org.Hs.eg.db, ont="BP")` → `enrichGO(gson=gson)` |
| 网络感知 GSEA | `build_*_graph()` → `nseGO(gl, ..., graph=g)` |
| 多层网络 GSEA | `nseGO` / `nseKEGG` 配 `graphs=list(g1, g2, ...)` |
| 贝叶斯 term 选择 | `bayes_enrich(ego, candidate="top", ...)` → `bayes_summary(be)` |
| PPI 网络（STRING） | `getPPI(ego, ID=1)` → `plot()` |
| Uniprot 转换 | `uniprot_get(ids, from="GENENAME", to="ACC")` |
| LLM 解读富集结果 | `interpret(ego, model="gpt-4o", task="summarize")` |
| 简化（去冗余） | `simplify(ego)` |
| 过滤结果 | `gsfilter(ego, by="GSSize", min=10, max=500)` |

细节代码模板见 `references/workflows.md`。

---

## 五、常用函数签名速查（从源码提取的真实 formals）

```r
enrichGO(gene, OrgDb, keyType="ENTREZID", ont="MF", pvalueCutoff=0.05,
         pAdjustMethod="BH", universe, qvalueCutoff=0.2,
         minGSSize=10, maxGSSize=500, readable=FALSE, pool=FALSE, evidence=NULL)
enrichKEGG(gene, organism="hsa", keyType="kegg", pvalueCutoff=0.05,
           pAdjustMethod="BH", universe, minGSSize=10, maxGSSize=500,
           qvalueCutoff=0.2)
gseGO(geneList, OrgDb, ont="MF", keyType="ENTREZID", minGSSize=15,
      maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE,
      eps=1e-10, nPerm=1000, seed=NULL, by="fgsea")
gseKEGG(geneList, organism="hsa", keyType="kegg", minGSSize=15,
        maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH",
        verbose=TRUE, seed=NULL, by="fgsea", nPerm=1000)
compareCluster(geneClusters, fun="enrichGO", data, source_from, ...)
bitr(gene, fromType, toType, OrgDb, dropAmbiguous=FALSE, ...)

dotplot(x, showCategory=10, size, title, font.size, label_format, color,
        orderBy="xorder", decreasing=TRUE, xlim, ylim)
cnetplot(x, showCategory=10, foldChange, layout="nicely", colorEdge,
         nodeLabel, cex_category, cex_gene)
emapplot(x, showCategory=30, color="pvalue", layout, cex_category, cex_line)
gseaplot(x, geneSetID=1, by="runningScore", type="l", color, title,
         pvalue_table=FALSE)
ridgeplot(x, showCategory=5, label_format=30, fill, orderBy="NES",
          decreasing=FALSE)

simplify(enrichResultObject, cutoff=0.7, by="p.adjust", select_fun=min,
         measure="Wang", semData=NULL)
setReadable(x, OrgDb, keyType="auto", toType="SYMBOL")
merge_result(enrichResultList)
```

**完整 145 个符号的签名库在 `references/api-signatures.md`**，
用 `grep -n "^### <函数名>"` 精确查，不要整篇读。

---

## 六、工具

| 工具 | 干什么 | 依赖 R 吗 |
| --- | --- | --- |
| `tools/cp_lint.py` | **核心**。静态校验 R 脚本：函数名是否存在（含大小写/拼写纠错建议）、参数名是否合法（`...` 透传降为 warning）、deprecated 参数告警、括号与引号配对、中文全角符号、library() 缺失告警 | 否 |
| `tools/cp_api.py` | 查函数签名/模块归属，支持模糊搜索 | 否 |
| `tools/cp_plan.py` | 一句话需求 → 推荐流程与函数序列 | 否 |
| `tools/selftest.py` | 一键自检（fixtures+文档+工具+数据四类检查） | 否 |
| `tools/etl/fetch_sources.py` | 抓 clusterProfiler 上游源码（不依赖 git 二进制） | 否 |
| `tools/etl/build_api.py` | 解析 NAMESPACE + R/*.R → 真实 formals | 否 |
| `tools/etl/gen_docs.py` | 生成 references + whitelist.json | 否 |
| `tools/etl/rebuild.py` | 一键重建事实底座（抓源 → 解析 → 生成） | 否 |
| `scripts/preflight.R` | 检查 R / clusterProfiler / OrgDb 版本与常用依赖，输出 JSON | 是 |
| `scripts/run_cp.R` | 批量执行 R 脚本（日志 + 退出码 + JSON） | 是 |

用法：

```bash
# 校验（必做）
python3 tools/cp_lint.py my_analysis.R --json

# 查签名
python3 tools/cp_api.py enrichKEGG
python3 tools/cp_api.py --search kegg

# 规划流程
python3 tools/cp_plan.py "GO 富集 + GSEA 跑 KEGG" --json

# 环境（需要 R）
Rscript scripts/preflight.R --json

# 执行（需要 R）
Rscript scripts/run_cp.R --script my_analysis.R --workdir runs/pbmc01
```

`cp_lint.py` 的退出码：0 = 无 error；1 = 有 error；2 = 用法错误。
warning 不阻断（`...` 透传、未装 library()），但要在回复里说明。

---

## 七、失败协议（按症状查）

| 症状 | 真实原因 | 处置 |
| --- | --- | --- |
| `could not find function "xxx"` | 函数不存在或包名写错 | `cp_api.py xxx` 查真实名 |
| `unused argument (...)` | 参数名幻觉 | `cp_api.py xxx` 查真实参数 |
| `Error in download_KEGG` | KEGG 网络失败 | 改用 `gson_KEGG('hsa')` 离线 |
| `Error: No gene can be mapped` | keyType 与 geneID 类型不一致 | `bitr` 先转 ENTREZID |
| `object 'OBONG' not found` | typo | 看 graph |
| `Error: universe length < differ` | universe 比 gene 还短 / 错填 | 不要传 universe 让 R 用 default |
| GO 富集结果全空 | ont/物种/OrgDb 三者之一错了 | 打印 `head(ego)` 看 ID 列名 |
| KEGG 富集结果全 UNKNOWN | organism 代码错（不是 Latin 学名） | `search_kegg_organism()` 查正确代码 |
| `dotplot(width=)` 报 `unused argument` | width 不是 dotplot 参数 | 去掉 width，要控制宽用 `pdf()` |
| `compareCluster` 报 `unused argument (OrgDb)` | compareCluster 把 OrgDb 透传给 fun | 这不是错；如果 fun="enrichGOO" 才是真的错 |
| LLM 解读返回空 | aisdk 没装 / API key 缺 | `library(aisdk)` + `Sys.setenv(OPENAI_API_KEY=...)` |
| 网络感知 GSEA 报 `graph required` | 没传 graph/graphs | `build_*_graph()` 先建图 |
| 内存爆 / 太慢 | 基因集太大 | `gsfilter(ego, by="GSSize", min=10, max=200)` |
| `non-conformable arguments` in dotplot | enrichResult 对象不对 | `class(ego)` 确认是 `enrichResult` / `gseaResult` / `compareClusterResult` |
| 中文路径报错 | R 在 Windows 编码敏感 | 工作目录用纯 ASCII 路径 |
| `setReadable` 后 geneID 还是 ENTREZID | OrgDb 装错 / keyType 错 | `columns(OrgDb)` 查支持类型 |
| `simplify(ego)` 报 'no applicable method' | simplify 没收到原 easy 方法 | 那是 `simplify` 不是 `simplify()` |

更多坑见 `references/pitfalls.md`。

---

## 八、本机环境边界（诚实说明）

Windows 上**当前未安装 R**（`which R` 无输出，已实测）。因此：

- 本技能在本机可以完整做到：**选函数、写代码、校验脚本、规划流程、解读报错**；
- 本技能在本机**做不到**：真实跑 `Rscript` 出图出数。
- 需要真跑时，给用户三选一，说清楚代价：
  1. 本机装 R（≥4.2）+ `BiocManager::install('clusterProfiler')`（依赖多，装一次约 15-40 分钟）；
  2. 交付脚本交给 Linux 服务器 / HPC / Colab；
  3. GitHub Actions（`r-lib/actions/setup-r` + `setup-bioconductor` + 缓存 `renv`）。

**不要假装跑过、不要编造任何数值结果。** 没跑就是没跑。

---

## 九、参考文件

- `references/api-signatures.md` —— 145 个真实符号的完整签名（grep 用）
- `references/function-index.md` —— 按模块 / S3 method / S4 method / S4 类分类
- `references/workflows.md` —— 可直接改用的流程模板（GO / KEGG / GSEA / 比较 / 离线 / LLM / 网络 / 多组学）
- `references/pitfalls.md` —— 物种 / ID 类型 / 网络 / 性能 / 内存 / 编码 / 常见幻觉
- `references/environment.md` —— 安装、版本对齐、离线与 HPC 场景

---

## 十、宿主兼容性（Claude Code / WorkBuddy / Codex / DeepSeek Hermes）

本技能只依赖三样东西：**Bash（跑 python3）+ Read + Grep**。
不联网（核心工具全离线）、不依赖 MCP、不依赖任何宿主专有能力，因此任何支持「目录型 skill」
的 Agent 宿主都能用。

| 宿主 | 安装位置 | 安装命令 |
|---|---|---|
| Claude Code（用户级） | `~/.claude/skills/clusterprofiler-skill/` | `python3 install.py` |
| Claude Code（项目级） | `<项目>/.claude/skills/clusterprofiler-skill/` | `python3 install.py --project` |
| WorkBuddy | `~/.workbuddy/skills/clusterprofiler-skill/` | `python3 install.py --host workbuddy` |
| Codex | `~/.codex/skills/clusterprofiler-skill/` | `python3 install.py --host codex` |
| DeepSeek Hermes | `~/.deepseek/skills/clusterprofiler-skill/` | `python3 install.py --host deepseek` |
| 其它宿主 | 自定义 | `python3 install.py --dir <skills 根目录>` |

约定（改动本技能时必须遵守，否则会破坏兼容性）：

1. 所有路径一律**相对 skill 根目录**写：`tools/cp_lint.py`、`references/workflows.md`。
   不写任何绝对路径 —— 换机器、换用户、换宿主都不用改。
2. 命令统一写 `python3`；Windows 上若没有 `python3`，把它换成 `python`。
3. SKILL.md 是唯一常驻入口。`references/*.md` 按需 grep 读取，不要整篇加载
   （`api-signatures.md` 有 19 KB，整读既慢又挤占上下文）。
4. 改动技能后必须跑 `python3 tools/selftest.py`（fixtures 回归 + 文档代码块 + 工具冒烟 + 数据完整性四类检查，全绿才能提交）；
   交付 R 代码前必须跑 `python3 tools/cp_lint.py <脚本>`（error 必须为 0）。