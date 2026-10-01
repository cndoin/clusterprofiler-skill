# 测试 fixture：合法的 clusterProfiler 脚本（enrichGO）
# 期望 cp_lint.py 退出码 0（无 error）

library(clusterProfiler)

data(geneList, package = "DOSE")
gene <- names(geneList)[abs(geneList) > 2]
ego <- enrichGO(
  gene     = gene,
  OrgDb    = org.Hs.eg.db,
  keyType  = "ENTREZID",
  ont      = "BP",
  pAdjustMethod = "BH",
  pvalueCutoff  = 0.01,
  qvalueCutoff  = 0.05
)

dotplot(ego, showCategory = 20)
barplot(ego, showCategory = 15)
cnetplot(ego, categorySize = "pvalue", foldChange = geneList)

saveRDS(ego, file = "enrichGO_result.rds")