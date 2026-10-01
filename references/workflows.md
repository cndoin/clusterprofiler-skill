# clusterProfiler 流程代码模板

> 所有代码块的函数与参数名均已通过 `tools/cp_lint.py` 校验（基于源码 formals）。
> 复制到新脚本后**仍要再跑一次 lint**，因为改动可能引入错误。
> 参数取值（pvalueCutoff / minGSSize / ont）必须按实际数据调整，不要照抄。

---

## 0. 通用开头

```r
library(clusterProfiler)
library(org.Hs.eg.db)        # 按 species 切换：org.Mm.eg.db / org.Dr.eg.db ...
library(enrichplot)

set.seed(42)
options(stringsAsFactors = FALSE)
rm(list = ls()); gc(verbose = FALSE)
```

---

## 1. GO 过表示分析（最常用）

```r
data(geneList, package = "DOSE")
gene <- names(geneList)[abs(geneList) > 2]

ego <- enrichGO(
  gene         = gene,
  OrgDb        = org.Hs.eg.db,
  keyType      = "ENTREZID",
  ont          = "BP",             # "BP" / "CC" / "MF" / "ALL"
  pAdjustMethod = "BH",
  pvalueCutoff  = 0.01,
  qvalueCutoff  = 0.05,
  readable      = TRUE             # 自动把 ENTREZID 转回 SYMBOL
)

dotplot(ego, showCategory = 20)
barplot(ego, showCategory = 15)
cnetplot(ego, categorySize = "pvalue", foldChange = geneList)
```

**输入是 SYMBOL？** 先转 ENTREZID：

```r
gene <- bitr(deg$gene_id, fromType = "SYMBOL", toType = "ENTREZID",
             OrgDb = org.Hs.eg.db)$ENTREZID
ego <- enrichGO(gene, OrgDb = org.Hs.eg.db, keyType = "ENTREZID", ont = "BP",
               readable = TRUE)
```

---

## 2. GO 三种 ontology 一次性跑

```r
ego_all <- enrichGO(gene, OrgDb = org.Hs.eg.db, keyType = "ENTREZID",
                    ont = "ALL", readable = TRUE)

# 拆开看
ego_bp <- ego_all@result[ego_all@result$ONTOLOGY == "BP", ]
ego_cc <- ego_all@result[ego_all@result$ONTOLOGY == "CC", ]
ego_mf <- ego_all@result[ego_all@result$ONTOLOGY == "MF", ]
```

---

## 3. KEGG 通路 ORA

```r
gene <- names(geneList)[abs(geneList) > 2]

# 用 bitr_kegg 转 KEGG ID
gene_kegg <- bitr_kegg(gene, fromType = "ncbi-geneid",
                       toType = "kegg", organism = "hsa")$kegg

ek <- enrichKEGG(
  gene         = gene_kegg,
  organism     = "hsa",
  keyType      = "kegg",
  pAdjustMethod = "BH",
  pvalueCutoff  = 0.05
)

dotplot(ek, showCategory = 15)
cnetplot(ek, categorySize = "pvalue")

# 在浏览器里看具体 pathway
browseKEGG(ek, pathID = "hsa04210")    # hsa04210 = Apoptosis
```

---

## 4. KEGG 离线（无网或国内 KEGG 经常卡）

```r
# 第一次联网下载，缓存为 GSON 对象保存
gson_kegg <- gson_KEGG("hsa", KEGG_Type = "KEGG", keyType = "kegg")
saveRDS(gson_kegg, "kegg_hsa_gson.rds")

# 之后直接读
gson_kegg <- readRDS("kegg_hsa_gson.rds")

# enrichKEGG 接受 GSON 作为 organism
ek <- enrichKEGG(gene = gene_kegg, organism = gson_kegg)
```

---

## 5. WikiPathways / Module / PathwayCommons

```r
# WikiPathways（organism 用 Latin 学名）
ewp <- enrichWP(gene, organism = "Homo sapiens")

# KEGG Module
emk <- enrichMKEGG(gene = gene, organism = "hsa")

# PathwayCommons
epc <- enrichPC(gene, pathway = "reactome_pathway")    # reactome / nci_pathway / biocarta ...
```

---

## 6. GSEA / GO

```r
gl <- deg$log2fc
names(gl) <- deg$entrez
gl <- sort(gl, decreasing = TRUE)

ggo <- gseGO(
  gl,
  OrgDb    = org.Hs.eg.db,
  ont      = "BP",
  keyType  = "ENTREZID",
  minGSSize = 15,
  maxGSSize = 500,
  pvalueCutoff = 0.05,
  pAdjustMethod = "BH",
  verbose = FALSE
)

gseaplot(ggo, geneSetID = 1:3)
ridgeplot(ggo, showCategory = 5)
dotplot(ggo, showCategory = 10) + facet_grid(~ .sign)
```

**输入是 SYMBOL？** `gseGO` 会按 keyType 自动转。

---

## 7. GSEA / MSigDB（hallmark 等）

```r
library(msigdbr)

# hallmark 50 组
gmt <- msigdbr(species = "Homo sapiens", category = "H") |>
       dplyr::select(gs_name, entrez_gene)

ge <- GSEA(sort(gl, decreasing = TRUE), TERM2GENE = gmt,
           pvalueCutoff = 0.05)

dotplot(ge, showCategory = 10)
```

---

## 8. 多组学比较（compareCluster）

```r
deg$cluster <- sample(c("A", "B", "C"), nrow(deg), replace = TRUE)

# 每组单独做 GO BP；用 formula 表达 分组~gene
ck <- compareCluster(
  entrez ~ cluster,
  data     = deg,
  fun      = "enrichGO",
  OrgDb    = org.Hs.eg.db,
  ont      = "BP",
  readable = TRUE
)

dotplot(ck, showCategory = 5)
cnetplot(ck, showCategory = 5)
```

**fun 接受哪些？** `"enrichGO"` / `"enrichKEGG"` / `"enrichWP"` / `"enrichMKEGG"`
/ `"enrichPC"` / `"enrichDAVID"` / `"enricher"` / `"gseGO"` / `"gseKEGG"` ...

---

## 9. 多组结果合并（merge_result）

```r
m <- merge_result(list(A = ek1, B = ek2, C = ek3))
dotplot(m, showCategory = 10)
```

---

## 10. ID 转换

```r
# SYMBOL → ENTREZID + ENSEMBL（一次多列）
idmap <- bitr(deg$gene_id, fromType = "SYMBOL",
              toType = c("ENTREZID", "ENSEMBL"),
              OrgDb = org.Hs.eg.db)

# SYMBOL → KEGG
idmap_kegg <- bitr_kegg(deg$gene_id, fromType = "ncbi-geneid",
                        toType = "kegg", organism = "hsa")

# enrichResult → SYMBOL 列
x <- setReadable(ego, OrgDb = org.Hs.eg.db, keyType = "ENTREZID")
idType(x)        # 现在是 SYMBOL
```

---

## 11. 网络感知 GSEA（NSEA）

```r
library(enrichit)

g <- build_kegg_graph("hsa")      # 或 build_go_graph("BP", org.Hs.eg.db)
nse <- nseGO(sort(gl, decreasing = TRUE),
             OrgDb = org.Hs.eg.db, ont = "BP",
             graph = g)
dotplot(nse, showCategory = 10)
```

---

## 12. 多层网络 GSEA（MNSEA）

```r
g1 <- build_kegg_graph("hsa")
g2 <- build_string_graph("9606")  # 9606 = human taxID

mnse <- mnseGO(sort(gl, decreasing = TRUE),
               OrgDb = org.Hs.eg.db, ont = "BP",
               graphs = list(g1, g2))
```

---

## 13. 贝叶斯 term 选择

```r
be <- bayes_enrich(ego, candidate = "top", n_terms = 200, n_iter = 5000, burnin = 1000)
bayes_summary(be, active = TRUE, n = 30)
```

---

## 14. PPI 网络（STRING）

```r
g <- getPPI(ek, ID = 1)                       # igraph 对象
plot(g)
df <- getPPI(ek, output = "data.frame")
```

---

## 15. 简化（去冗余）

```r
ego_simple <- simplify(ego, cutoff = 0.7, by = "p.adjust", measure = "Wang")
dotplot(ego_simple, showCategory = 20)
```

需要 `GOSemSim` 装上 + 提供 `semData`（用 `godata("BP", "hsapiens")` 提前算）。

---

## 16. LLM 解读

```r
interpret(ek, model = "gpt-4o", task = "summarize")
# 多 agent 深度分析
interpret_agent(list(ek, ego))
# 层级聚合
interpret_hierarchical(list(A = ek1, B = ek2))
```

需要 aisdk + OPENAI_API_KEY（或本地 ollama）。

---

## 17. Universal enricher（自备注释）

```r
# 任意 GMT / custom gene sets
gmt <- read.gmt("my_pathways.gmt")

er <- enricher(
  gene,
  TERM2GENE = gmt,
  TERM2NAME = NULL,
  pvalueCutoff = 0.05,
  pAdjustMethod = "BH",
  minGSSize = 10,
  maxGSSize = 500
)
```

---

## 18. 过滤结果

```r
# 按 gene set 大小 / 命中基因数过滤
ego_f <- gsfilter(ego, by = "GSSize", min = 10, max = 200)
ego_f <- gsfilter(ego, by = "Count",  min = 5)
```

---

## 19. KEGG module

```r
emk <- enrichMKEGG(gene = gene, organism = "hsa")
dotplot(emk, showCategory = 15)
```

---

## 20. PathwayCommons

```r
epc <- enrichPC(gene, pathway = "reactome_pathway")
# 或：nci_pathway / biocarta / humancyc / wikipathways / pid
```

---

## 21. DAVID（需要 DAVID 账号）

```r
ed <- enrichDAVID(
  gene         = gene,
  idType       = "ENTREZ_GENE_ID",
  david.user   = "your@email.com",       # 注册 DAVID 后会发 token
  species      = "Homo sapiens",
  annotation   = "GO_BP"
)
```

DAVID 2022 年起功能受限，新项目建议用 enrichKEGG / enrichGO。

---

## 22. 完整脚手架

```r
library(clusterProfiler)
library(org.Hs.eg.db)
library(enrichplot)

set.seed(42)

# 1) 读你的差异分析结果
deg <- read.csv("deg.csv")   # 含 gene_id / log2FC / padj 三列

# 2) 转 ID
gene <- bitr(unique(deg$gene_id), fromType = "SYMBOL",
             toType = "ENTREZID", OrgDb = org.Hs.eg.db)$ENTREZID

# 3) GO BP
ego <- enrichGO(gene, OrgDb = org.Hs.eg.db, keyType = "ENTREZID",
                ont = "BP", pAdjustMethod = "BH",
                pvalueCutoff = 0.01, qvalueCutoff = 0.05, readable = TRUE)

# 4) 可视化
pdf("go_bp.pdf", width = 8, height = 12)
print(dotplot(ego, showCategory = 20))
print(barplot(ego, showCategory = 15))
print(cnetplot(ego, categorySize = "pvalue", foldChange = deg$log2fc))
dev.off()

# 5) 简化（去冗余）
ego_simple <- simplify(ego)
print(dotplot(ego_simple, showCategory = 15))

# 6) 保存
saveRDS(list(ego = ego, ego_simple = ego_simple), file = "results.rds")
write.csv(as.data.frame(ego), file = "ego.csv", row.names = FALSE)
```

跑前必跑：

```bash
python3 tools/cp_lint.R my_analysis.R --json   # error 必须 0
```