# ReactomePA — 1.99.2

> 数据源：YuLab-SMU/ReactomePA @ devel
> 44 个已知符号

## Function (7)

- `bayes_reactome(x, candidate=c("top", "significant", "all"), n_terms=200, by="p.adjust", prior=0.1, false_positive=0.01, false_negative=0.1, n_iter=5000, burnin=1000, thin=1, posterior_cutoff=0.5, seed=NULL, verbose=FALSE)`
- `enrichPathway(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, weight=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, organism="human", readable=FALSE)`
- `gsePathway(geneList, organism="human", exponent=1, weight=NULL, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`
- `gson_Reactome(organism="human")`
- `nsePathway(geneList, organism="human", mode=c("evidence", "signed"), network=NULL, restart_prob=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, nPerm=1000, seed=NULL, verbose=TRUE, ...)`
- `prepareReactomeNetwork(organism="human", directed=FALSE, cores=getOption("mc.cores", 1L))`
- `viewPathway(pathName, organism="human", readable=TRUE, foldChange=NULL, keyType="ENTREZID", layout="kk")`

## Reexport (37)

- `aes(x, y)`
- `as.undirected(?)`
- `cnetplot(x, layout, showCategory, color_category, size_category, color_item, size_item, color_edge, size_edge, categorySizeBy, node_label, node_label_size, foldChange, fc_threshold, hilight, hilight_alpha, categorySize, colorEdge, circular, pie, split, includeAll)`
- `columns(?)`
- `convertIdentifiers(?)`
- `dotplot(object, x, color, showCategory, size, split, font.size, title, label_format, orderBy, decreasing, xlim, ylim)`
- `E(?)`
- `emapplot(x, showCategory, color, layout, cex_category, cex_line, min_edge, group_category)`
- `EXTID2NAME(?)`
- `geneID(?)`
- `geneInCategory(?)`
- `geom_edge_link(?)`
- `geom_node_point(?)`
- `geom_node_text(?)`
- `getFromNamespace(?)`
- `ggraph(?)`
- `graph_from_graphnel(?)`
- `gseaplot(x, geneSetID, by, type, color, title)`
- `gson(gsid2gene, gsid2name)`
- `heatplot(x, showCategory, foldChange)`
- `mapIds(?)`
- `nsea_gson(?)`
- `pathwayGraph(?)`
- `prepare_network(graph)`
- `reactomeEXTID2PATHID(?)`
- `reactomePATHID2EXTID(?)`
- `reactomePATHID2NAME(?)`
- `ridgeplot(x, showCategory, label_format)`
- `scale_color_continuous(?)`
- `scale_size(?)`
- `setReadable(?)`
- `sparseMatrix(?)`
- `stack(?)`
- `theme_void(?)`
- `V(?)`
- `with_cache(?)`
- `yulab_msg(?)`
