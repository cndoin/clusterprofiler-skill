# enrichplot — 1.99.7

> 数据源：github.com/YuLab-SMU/enrichplot@devel
> 51 个已知符号

## Function (45)

- `as_enrichResult(?)`
- `as_gseaResult(?)`
- `autofacet(by='row', scales="free", levels=NULL)`
- `cnetplot(x, layout=igraph::layout_with_kk, showCategory=5, color_category="#E5C494", size_category=1, color_item="#B3B3B3", size_item=1, color_edge="grey", size_edge=.5, categorySizeBy=~itemNum, node_label="all", node_label_size=NULL, foldChange=NULL, fc_threshold=NULL, hilight="none", hilight_alpha=.3, pathway_id=NULL, layer=NULL, include_couplings=TRUE, ...)`
- `color_palette(colors)`
- `consensusmap(x, fill_var=c("NES", "delta_NES")`
- `dotplot(object, x="geneRatio", color="p.adjust", showCategory=10, size=NULL, split=NULL, font.size=12, title="", orderBy="x", label_format=30, decreasing=TRUE, layer=NULL, colorBy="p.adjust", by="geneRatio", includeAll=TRUE, group=FALSE, shape=FALSE, facet=NULL, strip_width=15, ...)`
- `dotplot2(object, x="FoldEnrichment", vars=NULL, label="auto", ...)`
- `emapplot(x, layout=igraph::layout_with_kk, coords=NULL, showCategory=30, color="p.adjust", size_category=1, min_edge=.2, color_edge="grey", size_edge=.5, group=NULL, group_legend=TRUE, node_label="category", node_label_size=5, pie="equal", layer=NULL, label_format=30, clusterFunction=stats::kmeans, nWords=4, nCluster=NULL, show_category_size_legend=TRUE, edge_filter="threshold", top_k=5, target_density=.1, edge_diagnostic=FALSE, ...)`
- `emapplot_edge_density(pair_sim, min_edge=.2, edge_filter="threshold", top_k=5, target_density=.1, dense_threshold=.2)`
- `facet_grid(?)`
- `fortify_mnsea_contribution(x, level=c("pathway", "feature"), pathway_id=NULL, layer=NULL, ...)`
- `fortify_mnsea_subnetwork(x, pathway_id=NULL, layer=NULL, include_couplings=TRUE, include_isolated=FALSE, ...)`
- `geneID(?)`
- `geneInCategory(?)`
- `geom_cnet_label(?)`
- `geom_gsea_gene(genes, mapping=NULL, geom=ggplot2::geom_text, ..., geneSet=NULL)`
- `get_enrichplot_color(n=2)`
- `ggtable(d, p=NULL)`
- `ggtitle(?)`
- `goplot(x, showCategory=10, color="p.adjust", layout=igraph::layout_with_sugiyama, geom="text", ID="Description", ...)`
- `gseadist(x, IDs, type='density')`
- `gseaplot(x, geneSetID, by="all", title="", color='black', color.line="green", color.vline="#FA5860", layer=NULL, ...)`
- `gseaplot2(x, geneSetID, title="", color="green", base_size=11, rel_heights=c(1.5, .5, 1), subplots=1:3, pvalue_table=FALSE, pvalue_table_columns=c("NES", "p.adjust"), pvalue_table_rownames="Description", ES_geom="line", layer=NULL)`
- `gsearank(x, geneSetID, title="", output="plot", layer=NULL)`
- `gseaScores(?)`
- `heatplot(x, showCategory=30, showTop=NULL, symbol="rect", foldChange=NULL, pvalue=NULL, label_format=30, pathway_id=NULL, layer=NULL, value=c("score", "abs_score", "share", "con...)`
- `hplot(x, geneSetID, layer=NULL)`
- `import_enrichr(x, db=1, gene=NULL, universe=NULL, ontology="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", pAdjustMethod="BH", ...)`
- `import_fgsea(x, stats, geneSets=NULL, setType="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", exponent=1, scoreType="std", pAdjustMethod="BH", ...)`
- `import_gprofiler2(x, gene=NULL, ontology="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", pAdjustMethod="BH", ...)`
- `import_webgestalt(x, gene=NULL, universe=NULL, ontology="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", pAdjustMethod="BH", ...)`
- `manhattanplot(x, color="p.adjust", showCategory=5, size="Count", split=NULL, font.size=12, title="", label_format=30, colorBy="p.adjust", includeAll=TRUE, facet="Cluster", strip_width=15, ...)`
- `mechanismflow(x, reference=NULL, flow_var=c("NES", "delta_NES", "leading_edge_s...)`
- `phaseplot(x, reference=NULL, selected_layer=NULL, reference_layer=NULL, x_axis=NULL, size_var=c("leading_edge_size", "leading_edge_...)`
- `plot_list(?)`
- `pmcplot(query, period, proportion=TRUE, data=NULL)`
- `rewireplot(x, ...)`
- `ridgeplot(x, showCategory=30, fill="p.adjust", core_enrichment=TRUE, label_format=30, orderBy="NES", decreasing=FALSE, stat="density_ridges", layer=NULL)`
- `set_enrichplot_color(colors=get_enrichplot_color(2), type="color", name=NULL, .fun=NULL, reverse=TRUE, transform='identity', ...)`
- `ssplot(x, showCategory=30, drfun=NULL, dr.params=list(), node_label="group", min_edge=.2, size_edge=.5, edge_filter="threshold", top_k=5, target_density=.1, edge_diagnostic=FALSE, layer=NULL, pie="equal", ...)`
- `theme_dose(?)`
- `treeplot(x, ...)`
- `upsetplot(x, n=10, type="boxplot", layer=NULL, value=c("score", "abs_score"), core_enrichment=FALSE, ...)`
- `volplot(x, color="zScore", xintercept=1, yintercept=2, showCategory=5, label_format=30, font.size=12, size=5)`

## Generic (5)

- `as.data.frame(x, ...)`
- `barplot(height, x="Count", color="p.adjust", showCategory=8, font.size=12, title="", label_format=30, by="geneRatio", includeAll=TRUE, ...)`
- `fortify(model, data, showCategory=5, by="Count", order=FALSE, drop=FALSE, split=NULL, includeAll=TRUE, level=c("result", "pathway"), layer=NULL, ...)`
- `ggplot_add(object, plot, ...)`
- `gsInfo(object, geneSetID, layer=NULL, ...)`

## S4method (1)

- `pairwise_termsim(?)`
