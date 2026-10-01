# ReactomePA — 1.99.2

> 数据源：github.com/YuLab-SMU/ReactomePA@devel
> 15 个已知符号

## Function (15)

- `bayes_reactome(x, candidate=c("top", "significant", "all"), n_terms=200, by="p.adjust", prior=0.1, false_positive=0.01, false_negative=0.1, n_iter=5000, burnin=1000, thin=1, posterior_cutoff=0.5, seed=NULL, verbose=FALSE)`
- `cnetplot(?)`
- `dotplot(?)`
- `emapplot(?)`
- `enrichPathway(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, weight=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, organism="human", readable=FALSE)`
- `geneID(?)`
- `geneInCategory(?)`
- `gseaplot(?)`
- `gsePathway(geneList, organism="human", exponent=1, weight=NULL, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`
- `gson_Reactome(organism="human")`
- `heatplot(?)`
- `nsePathway(geneList, organism="human", mode=c("evidence", "signed"), network=NULL, restart_prob=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, nPerm=1000, seed=NULL, verbose=TRUE, ...)`
- `prepareReactomeNetwork(organism="human", directed=FALSE, cores=getOption("mc.cores", 1L))`
- `ridgeplot(?)`
- `viewPathway(pathName, organism="human", readable=TRUE, foldChange=NULL, keyType="ENTREZID", layout="kk")`
