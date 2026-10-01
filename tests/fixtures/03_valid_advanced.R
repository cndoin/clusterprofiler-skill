# 测试 fixture：合法复杂流程（GSEA + 比较 + 合并 + 离线 GSON）
# 期望 cp_lint.py 退出码 0

library(clusterProfiler)

# GSEA
data(geneList, package = "DOSE")
gl <- sort(geneList, decreasing = TRUE)
ggo <- gseGO(
  gl,
  OrgDb    = org.Hs.eg.db,
  ont      = "BP",
  keyType  = "SYMBOL",
  minGSSize = 15,
  maxGSSize = 500,
  pvalueCutoff = 0.05,
  verbose = FALSE
)
gseaplot(ggo, geneSetID = 1:3)
dotplot(ggo, showCategory = 10) +
  facet_grid(~ .sign)        # 标准 facet grid 拼版
ridgeplot(ggo, showCategory = 5)

# KEGG
gene <- names(geneList)[abs(geneList) > 2]
ek  <- enrichKEGG(gene = gene, organism = "hsa", keyType = "kegg")
emk <- enrichMKEGG(gene = gene, organism = "hsa")
ewp <- enrichWP(gene, organism = "Homo sapiens")

# 多组比较（OrgDb / ont 透传给 fun="enrichGO" —— compareCluster 有 ... 透传）
deg$cluster <- sample(c("A", "B", "C"), nrow(deg), replace = TRUE)
ck <- compareCluster(
  entrez ~ cluster,
  data     = deg,
  fun      = "enrichGO",
  OrgDb    = org.Hs.eg.db,
  ont      = "BP"
)
dotplot(ck, showCategory = 5)

# 合并
m <- merge_result(list(A = ek, B = emk))
dotplot(m, showCategory = 10)

# 离线 GSON
gson_kegg <- gson_KEGG("hsa", KEGG_Type = "KEGG", keyType = "kegg")
ek_off <- enrichKEGG(gene = gene, organism = gson_kegg)

# 网络感知
nse <- nseGO(gl, OrgDb = org.Hs.eg.db, ont = "BP")

# LLM 解读（真实签名：x, context, n_pathways, model, task, prior, add_ppi, ...）
interpret(ek, model = "gpt-4o", task = "summarize")

# ID 类型查看 + setReadable
idType(ek)
ek_r <- setReadable(ek, OrgDb = org.Hs.eg.db, keyType = "ENTREZID")
idType(ek_r)

# PPI 网络
g <- getPPI(ek, ID = 1)

# 简化
ego <- simplify(ek)

saveRDS(list(ggo = ggo, ek = ek, ck = ck, m = m, ek_r = ek_r),
        file = "results.rds")