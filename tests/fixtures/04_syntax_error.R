# 测试 fixture：语法错误（括号不闭合）
# 期望 cp_lint.py 退出码 1，报 syntax

library(clusterProfiler)

ego <- enrichGO(
  gene     = gene,
  OrgDb    = org.Hs.eg.db,
  keyType  = "ENTREZID",
  ont      = "BP"
# 这里缺一个右括号

dotplot(ego)