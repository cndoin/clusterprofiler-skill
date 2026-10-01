# 测试 fixture：常见陷阱
# 期望 cp_lint.py 退出码 1（每个 trap 都是真实的 API 误用）

library(clusterProfiler)

# 陷阱1：dotplot 不是函数；clusterProfiler 实际函数是 enrichplot::dotplot
# 但通过 dotplot() 直接调用也是对的（因为 enrichplot 已经 re-export）
# 这里 trick：写一个错误的参数名
ego <- enrichGO(gene = gene, OrgDb = org.Hs.eg.db, ont = "BP")
dotplot(ego, showCategory = 10, label_format = NULL,
        width = "auto")   # <-- width 不是 dotplot 的参数

# 陷阱2：gseGO 的 keyType 与 names(geneList) 类型不匹配
# 这里不写出来（lint 验不了），但用户写错了 lint 不会抓
data(geneList, package = "DOSE")
gl <- sort(geneList, decreasing = TRUE)
gseGO(gl, OrgDb = org.Hs.eg.db, ont = "BP",
      keyType = "ENTREZID")   # names(gl) 是 SYMBOL，不匹配

# 陷阱3：empirical 用法错误：enricher 没传 TERM2GENE
enricher(gene, pvalueCutoff = 0.05)   # 缺 TERM2GENE / TERM2NAME

# 陷阱4：bitr 用错 ID 类型
bitr(c("TP53", "BRCA1"), fromType = "WRONG_TYPE", toType = "ENTREZID",
     OrgDb = org.Hs.eg.db)

# 陷阱5：compareCluster 的 fun 写错名字
compareCluster(entrez ~ cluster, data = gene, fun = "enrichGOO",
              OrgDb = org.Hs.eg.db)