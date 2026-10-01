# 测试 fixture：幻觉函数 + 幻觉参数
# 期望 cp_lint.py 退出码 1，且至少报出 unknown-function / unknown-arg

library(clusterProfiler)

# 幻觉函数（不存在）：enrichGO2 / enrichKEGGG / get_pathway_plot
ego2 <- enrichGO2(gene = gene, OrgDb = org.Hs.eg.db)
ekk <- enrichKEGGG(gene = gene, organism = "hsa")
p <- get_pathway_plot(ego, showCategory = 10)

# 幻觉参数：enrichGO 不接受 fdr_method
ego3 <- enrichGO(
  gene = gene,
  OrgDb = org.Hs.eg.db,
  fdr_method = "BH"   # <-- 错误，应该是 pAdjustMethod
)

# 幻觉参数：dotplot 不接受 style
dotplot(ego, showCategory = 10, style = "fancy")   # <-- 错误