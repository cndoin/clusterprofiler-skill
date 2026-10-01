# clusterprofiler — 4.21.2

> 数据源：github.com/YuLab-SMU/clusterprofiler@devel
> 155 个已知符号

## Function (56)

- `add_go_level(x)`
- `append_kegg_category(x)`
- `bitr(geneID, fromType, toType, OrgDb, drop=TRUE)`
- `bitr_kegg(geneID, fromType, toType, organism, drop=TRUE)`
- `browseKEGG(x, pathID)`
- `compareCluster(geneClusters, fun="enrichGO", data='', source_from=NULL, ...)`
- `download_KEGG(species, keggType="KEGG", keyType="kegg")`
- `dropGO(x, level=NULL, term=NULL)`
- `enrichDAVID(gene, idType="ENTREZ_GENE_ID", universe, minGSSize=10, maxGSSize=500, annotation="GOTERM_BP_FAT", pvalueCutoff=0.05, pAdjustMethod="BH", qvalueCutoff=0.2, species=NA, david.user)`
- `enricher(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, gson=NULL, TERM2GENE, TERM2NAME=NA)`
- `enrichGO(gene, OrgDb, keyType="ENTREZID", ont="MF", pvalueCutoff=0.05, pAdjustMethod="BH", universe, qvalueCutoff=0.2, minGSSize=10, maxGSSize=500, readable=FALSE, pool=FALSE, evidence=NULL)`
- `enrichKEGG(gene, organism="hsa", keyType="kegg", pvalueCutoff=0.05, pAdjustMethod="BH", universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, use_internal_data=FALSE)`
- `enrichMKEGG(gene, organism='hsa', keyType='kegg', pvalueCutoff=0.05, pAdjustMethod='BH', universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)`
- `enrichPC(gene, ...)`
- `enrichWP(gene, organism, ...)`
- `get_ppi(x, ID=1, taxID="auto", required_score=NULL, network_type="functional", add_nodes=0, show_query_node_labels=0, output='igraph')`
- `get_ppi_network(taxID=9606, version="12.0", score_threshold=400, output="data.frame")`
- `get_wp_organisms(?)`
- `getPPI(x, ID=1, taxID="auto", required_score=NULL, network_type="functional", add_nodes=0, show_query_node_labels=0, output='igraph')`
- `getTaxID(species)`
- `getTaxInfo(species, source="stringdb")`
- `Gff2GeneTable(gffFile, compress=TRUE)`
- `go2ont(goid)`
- `go2term(goid)`
- `gofilter(x, level=4)`
- `groupGO(gene, OrgDb, keyType="ENTREZID", ont="CC", level=2, readable=FALSE)`
- `GSEA(geneList, exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", gson=NULL, TERM2GENE, TERM2NAME=NA, verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`
- `gseGO(geneList, ont="BP", OrgDb, keyType="ENTREZID", exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`
- `gseKEGG(geneList, organism='hsa', keyType='kegg', exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, use_internal_data=FALSE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`
- `gseMKEGG(geneList, organism='hsa', keyType='kegg', exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`
- `gsePC(geneList, eps=1e-10, ...)`
- `gseWP(geneList, organism, eps=1e-10, ...)`
- `gson_GO(OrgDb, keytype='ENTREZID', ont="BP")`
- `gson_GO_local(data, ont=c("ALL", "BP", "CC", "MF"), species=NULL, ...)`
- `gson_KEGG(species, KEGG_Type="KEGG", keyType="kegg")`
- `gson_KEGG_mapper(file, format=c("BLAST","Ghost","Kofam"), type=c("pathway","module"), species=NULL, ...)`
- `gson_KO(?)`
- `gson_WP(organism)`
- `idType(OrgDb="org.Hs.eg.db")`
- `interpret(x, context=NULL, n_pathways=20, model=NULL, task="interpretation", prior=NULL, add_ppi=FALSE, gene_fold_change=NULL, max_tokens=8192, temperature=0.3, verbose=FALSE)`
- `interpret_agent(x, context=NULL, n_pathways=50, model=NULL, add_ppi=FALSE, gene_fold_change=NULL, max_tokens=8192, temperature=0.3, verbose=FALSE)`
- `interpret_hierarchical(x_minor, x_major, mapping, model=NULL, task="cell_type", max_tokens=8192, temperature=0.3)`
- `ko2name(ko)`
- `merge_result(enrichResultList)`
- `mnseGO(seed_list, networks, couplings, ont="BP", OrgDb, keyType="ENTREZID", mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`
- `mnseKEGG(seed_list, networks, couplings, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, use_internal_data=FALSE, ...)`
- `mnseMKEGG(seed_list, networks, couplings, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`
- `mnseWP(seed_list, networks, couplings, organism, mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`
- `nseGO(geneList, network, ont="BP", OrgDb, keyType="ENTREZID", mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`
- `nseKEGG(geneList, network, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, use_internal_data=FALSE, ...)`
- `nseMKEGG(geneList, network, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`
- `nseWP(geneList, network, organism, mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`
- `plotGOgraph(x, firstSigNodes=10, useInfo="all", sigForAll=TRUE, useFullNames=TRUE, ...)`
- `read.gmt.pc(gmtfile, output="data.frame")`
- `search_kegg_organism(str, by="scientific_name", ignore.case=FALSE, use_internal_data=TRUE)`
- `uniprot_get(taxID)`

## Generic (4)

- `as.data.frame(x, ...)`
- `dim(x)`
- `plot(x, layout="nicely", ...)`
- `print(x, ...)`

## S4method (1)

- `simplify(?)`

## Reexport (94)

- `%<>%(lhs, rhs)`
- `%>%(lhs, rhs)`
- `%||%(lhs, rhs)`
- `.data(?)`
- `aes(x, y)`
- `Agent(description, name, model)`
- `aggregate_enrichment(?)`
- `aggregate_omics(?)`
- `arrange(.data, ...)`
- `bayes_enrich(?)`
- `bayes_summary(?)`
- `browseURL(?)`
- `buildGOmap(gostats)`
- `ChatSession(agent)`
- `check_installed(?)`
- `citation(?)`
- `cnetplot(x, layout, showCategory, color_category, size_category, color_item, size_item, color_edge, size_edge, categorySizeBy, node_label, node_label_size, foldChange, fc_threshold, hilight, hilight_alpha, categorySize, colorEdge, circular, pie, split, includeAll)`
- `dlply(?)`
- `dotplot(object, x, color, showCategory, size, split, font.size, title, label_format, orderBy, decreasing, xlim, ylim)`
- `download_yulab_file(url, destfile)`
- `emapplot(x, showCategory, color, layout, cex_category, cex_line, min_edge, group_category)`
- `filter(.data, ..., .preserve=FALSE)`
- `formula(?)`
- `gather(?)`
- `geneID(x)`
- `geneInCategory(x)`
- `generate_object(session, schema)`
- `geom_label(?)`
- `geom_point(?)`
- `get_cache(dir)`
- `get_cache_item(key)`
- `get_fun_from_pkg(pkg, fun)`
- `get_organism(db)`
- `ggplot(data, mapping)`
- `ggtitle(?)`
- `GOBPCHILDREN(?)`
- `GOCCCHILDREN(?)`
- `godata(ont, organism)`
- `GOMFCHILDREN(?)`
- `goplot(x, showCategory, color, size)`
- `GOTERM(?)`
- `group_by(.data, ..., .add=FALSE, .drop=FALSE)`
- `gseaplot(x, geneSetID, by, type, color, title)`
- `gsfilter(?)`
- `gson(gsid2gene, gsid2name)`
- `harmonize_ids(?)`
- `head(x, n=6L, ...)`
- `heatplot(x, showCategory, foldChange)`
- `installed.packages(?)`
- `is(?)`
- `is.installed(pkg)`
- `keys(x)`
- `keytypes(x)`
- `ldply(?)`
- `llply(?)`
- `load_OrgDb(OrgDb)`
- `mgoSim(GO1, GO2)`
- `modifyList(?)`
- `mutate(.data, ...)`
- `n(?)`
- `na.omit(?)`
- `new(?)`
- `Ontology(object)`
- `packageDescription(?)`
- `quos(?)`
- `qvalue(?)`
- `read.blast2go(file)`
- `read.gaf(file)`
- `read.gmt(gmtfile, output="data.frame")`
- `read.gmt.wp(gmtfile)`
- `read.table(?)`
- `rename(.data, ...)`
- `ridgeplot(x, showCategory, label_format)`
- `scale_color_manual(values)`
- `select(.data, ...)`
- `select_features_for_ora(?)`
- `separate(?)`
- `setNames(?)`
- `setReadable(?)`
- `slice(.data, ..., .preserve=FALSE)`
