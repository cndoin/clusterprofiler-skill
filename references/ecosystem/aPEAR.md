# aPEAR — 1.0

> 数据源：ievaKer/aPEAR @ main
> 11 个已知符号

## Function (5)

- `enrichmentNetwork(enrichment, clusters, params, dt, sim, clust, innerCutoff=0.1, outerCutoff=0.5, colorType=c('nes', 'pval'), pCutoff=-10, drawEllipses=FALSE, fontSize=5, repelLabels=FALSE, plot, pathways, c, a, b, alpha, bigger=0)`
- `findClusters(sim, minClusterSize=2, method=c('markov', 'hier', 'spectral'), nameMethod=c('pagerank', 'hits', 'none'), verbose=FALSE)`
- `getGenes(enrichment, geneCol, pathCol='Description')`
- `pathwaySimilarity(enrichment, geneCol, pathCol='Description', method=c('jaccard', 'cosine', 'cor'))`
- `validateEnrichment(enrichment, colorBy=NULL, nodeSize=NULL, verbose=TRUE)`

## Reexport (6)

- `%>%(lhs, rhs)`
- `cosine(?)`
- `deframe(?)`
- `hits(?)`
- `jaccardSets(?)`
- `mcl(?)`
