# clusterProfiler 全量函数签名库（自源码提取，非文档转述）

> 数据源：github.com/YuLab-SMU/clusterProfiler `devel`（clusterProfiler 4.21.2）。
> 每条签名由 `R/` 源码的真实 `formals` 解析得到；
> 第三方包 re-export（enrichplot/dplyr/magrittr/...）的参数表为手工核对（标注 pkg）。
> S3 generic 取其全部 method 参数的并集。

> 用法：`grep -n "^### <函数名>" references/api-signatures.md` 精确查，不要整篇读。

共 161 个已知符号，其中 155 个解析到真实参数表。


## MODULE: ora — 过表示分析 ORA（GO / KEGG / WikiPathways / Module / PathwayCommons / DAVID / 通用 enricher）（8）

### compareCluster
`compareCluster(geneClusters, fun="enrichGO", data='', source_from=NULL, ...)`

- 来源：`compareCluster.R` · 包：clusterProfiler · 实现：compareCluster

### enrichDAVID
`enrichDAVID(gene, idType="ENTREZ_GENE_ID", universe, minGSSize=10, maxGSSize=500, annotation="GOTERM_BP_FAT", pvalueCutoff=0.05, pAdjustMethod="BH", qvalueCutoff=0.2, species=NA, david.user)`

- 来源：`enrichDAVID.R` · 包：clusterProfiler · 实现：enrichDAVID

### enricher
`enricher(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, gson=NULL, TERM2GENE, TERM2NAME=NA)`

- 来源：`enricher.R` · 包：clusterProfiler · 实现：enricher

### enrichGO
`enrichGO(gene, OrgDb, keyType="ENTREZID", ont="MF", pvalueCutoff=0.05, pAdjustMethod="BH", universe, qvalueCutoff=0.2, minGSSize=10, maxGSSize=500, readable=FALSE, pool=FALSE, evidence=NULL)`

- 来源：`enrichGO.R` · 包：clusterProfiler · 实现：enrichGO

### enrichKEGG
`enrichKEGG(gene, organism="hsa", keyType="kegg", pvalueCutoff=0.05, pAdjustMethod="BH", universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, use_internal_data=FALSE)`

- 来源：`enrichKEGG.R` · 包：clusterProfiler · 实现：enrichKEGG

### enrichMKEGG
`enrichMKEGG(gene, organism='hsa', keyType='kegg', pvalueCutoff=0.05, pAdjustMethod='BH', universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)`

- 来源：`enrichMKEGG.R` · 包：clusterProfiler · 实现：enrichMKEGG

### enrichPC
`enrichPC(gene, ...)`

- 来源：`pathwayCommons.R` · 包：clusterProfiler · 实现：enrichPC

### enrichWP
`enrichWP(gene, organism, ...)`

- 来源：`wikiPathways.R` · 包：clusterProfiler · 实现：enrichWP


## MODULE: gsea — GSEA / NSEA / 拓扑感知 / 贝叶斯（14）

### GSEA
`GSEA(geneList, exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", gson=NULL, TERM2GENE, TERM2NAME=NA, verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`

- 来源：`enricher.R` · 包：clusterProfiler · 实现：GSEA

### gseGO
`gseGO(geneList, ont="BP", OrgDb, keyType="ENTREZID", exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`

- 来源：`gseAnalyzer.R` · 包：clusterProfiler · 实现：gseGO

### gseKEGG
`gseKEGG(geneList, organism='hsa', keyType='kegg', exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, use_internal_data=FALSE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`

- 来源：`gseAnalyzer.R` · 包：clusterProfiler · 实现：gseKEGG

### gseMKEGG
`gseMKEGG(geneList, organism='hsa', keyType='kegg', exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)`

- 来源：`gseAnalyzer.R` · 包：clusterProfiler · 实现：gseMKEGG

### gsePC
`gsePC(geneList, eps=1e-10, ...)`

- 来源：`pathwayCommons.R` · 包：clusterProfiler · 实现：gsePC

### gseWP
`gseWP(geneList, organism, eps=1e-10, ...)`

- 来源：`wikiPathways.R` · 包：clusterProfiler · 实现：gseWP

### mnseGO
`mnseGO(seed_list, networks, couplings, ont="BP", OrgDb, keyType="ENTREZID", mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`

- 来源：`nseaAnalyzer.R` · 包：clusterProfiler · 实现：mnseGO

### mnseKEGG
`mnseKEGG(seed_list, networks, couplings, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, use_internal_data=FALSE, ...)`

- 来源：`nseaAnalyzer.R` · 包：clusterProfiler · 实现：mnseKEGG

### mnseMKEGG
`mnseMKEGG(seed_list, networks, couplings, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`

- 来源：`nseaAnalyzer.R` · 包：clusterProfiler · 实现：mnseMKEGG

### mnseWP
`mnseWP(seed_list, networks, couplings, organism, mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`

- 来源：`nseaAnalyzer.R` · 包：clusterProfiler · 实现：mnseWP

### nseGO
`nseGO(geneList, network, ont="BP", OrgDb, keyType="ENTREZID", mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`

- 来源：`nseaAnalyzer.R` · 包：clusterProfiler · 实现：nseGO

### nseKEGG
`nseKEGG(geneList, network, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, use_internal_data=FALSE, ...)`

- 来源：`nseaAnalyzer.R` · 包：clusterProfiler · 实现：nseKEGG

### nseMKEGG
`nseMKEGG(geneList, network, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`

- 来源：`nseaAnalyzer.R` · 包：clusterProfiler · 实现：nseMKEGG

### nseWP
`nseWP(geneList, network, organism, mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`

- 来源：`nseaAnalyzer.R` · 包：clusterProfiler · 实现：nseWP


## MODULE: id — 基因 ID 转换与位点注释（10）

### bitr
`bitr(geneID, fromType, toType, OrgDb, drop=TRUE)`

- 来源：`bitr.R` · 包：clusterProfiler · 实现：bitr

### bitr_kegg
`bitr_kegg(geneID, fromType, toType, organism, drop=TRUE)`

- 来源：`bitr.R` · 包：clusterProfiler · 实现：bitr_kegg

### get_wp_organisms
`get_wp_organisms(?)`

- 来源：`wikiPathways.R` · 包：clusterProfiler · 实现：get_wp_organisms

### getTaxID
`getTaxID(species)`

- 来源：`taxa.R` · 包：clusterProfiler · 实现：getTaxID

### getTaxInfo
`getTaxInfo(species, source="stringdb")`

- 来源：`taxa.R` · 包：clusterProfiler · 实现：getTaxInfo

### Gff2GeneTable
`Gff2GeneTable(gffFile, compress=TRUE)`

- 来源：`GFFparser.R` · 包：clusterProfiler · 实现：Gff2GeneTable

### go2ont
`go2ont(goid)`

- 来源：`go-utilities.R` · 包：clusterProfiler · 实现：go2ont

### go2term
`go2term(goid)`

- 来源：`go-utilities.R` · 包：clusterProfiler · 实现：go2term

### idType
`idType(OrgDb="org.Hs.eg.db")`

- 来源：`bitr.R` · 包：clusterProfiler · 实现：idType

### ko2name
`ko2name(ko)`

- 来源：`kegg-utilities.R` · 包：clusterProfiler · 实现：ko2name


## MODULE: db — 数据库 / GSON / KEGG 下载（10）

### append_kegg_category
`append_kegg_category(x)`

- 来源：`kegg-utilities.R` · 包：clusterProfiler · 实现：append_kegg_category

### download_KEGG
`download_KEGG(species, keggType="KEGG", keyType="kegg")`

- 来源：`enrichKEGG.R` · 包：clusterProfiler · 实现：download_KEGG

### gson_GO
`gson_GO(OrgDb, keytype='ENTREZID', ont="BP")`

- 来源：`gson.R` · 包：clusterProfiler · 实现：gson_GO

### gson_GO_local
`gson_GO_local(data, ont=c("ALL", "BP", "CC", "MF"), species=NULL, ...)`

- 来源：`gson.R` · 包：clusterProfiler · 实现：gson_GO_local

### gson_KEGG
`gson_KEGG(species, KEGG_Type="KEGG", keyType="kegg")`

- 来源：`gson.R` · 包：clusterProfiler · 实现：gson_KEGG

### gson_KEGG_mapper
`gson_KEGG_mapper(file, format=c("BLAST","Ghost","Kofam"), type=c("pathway","module"), species=NULL, ...)`

- 来源：`gson.R` · 包：clusterProfiler · 实现：gson_KEGG_mapper

### gson_KO
`gson_KO(?)`

- 来源：`gson.R` · 包：clusterProfiler · 实现：gson_KO

### gson_WP
`gson_WP(organism)`

- 来源：`gson.R` · 包：clusterProfiler · 实现：gson_WP

### read.gmt.pc
`read.gmt.pc(gmtfile, output="data.frame")`

- 来源：`pathwayCommons.R` · 包：clusterProfiler · 实现：read.gmt.pc

### search_kegg_organism
`search_kegg_organism(str, by="scientific_name", ignore.case=FALSE, use_internal_data=TRUE)`

- 来源：`kegg-utilities.R` · 包：clusterProfiler · 实现：search_kegg_organism


## MODULE: go — GO 工具（groupGO / gofilter / dropGO / buildGOmap）（4）

### add_go_level
`add_go_level(x)`

- 来源：`go-utilities.R` · 包：clusterProfiler · 实现：add_go_level

### dropGO
`dropGO(x, level=NULL, term=NULL)`

- 来源：`enrichGO.R` · 包：clusterProfiler · 实现：dropGO

### gofilter
`gofilter(x, level=4)`

- 来源：`gofilter.R` · 包：clusterProfiler · 实现：gofilter

### groupGO
`groupGO(gene, OrgDb, keyType="ENTREZID", ont="CC", level=2, readable=FALSE)`

- 来源：`groupGO.R` · 包：clusterProfiler · 实现：groupGO


## MODULE: manip — 结果操作（merge_result / simplify）（6）

### as.data.frame
`as.data.frame(x, ...)`

- 来源：`accessor.R` · 包：clusterProfiler · 实现：as.data.frame.groupGOResult
- 方法变体：`*groupGOResult*`

### dim
`dim(x)`

- 来源：`accessor.R` · 包：clusterProfiler · 实现：dim.compareClusterResult
- 方法变体：`*compareClusterResult*`

### geneID
`geneID(x)`

- 来源：`accessor.R` · 包：clusterProfiler · 实现：geneID.groupGOResult

### geneInCategory
`geneInCategory(x)`

- 来源：`accessor.R` · 包：clusterProfiler · 实现：geneInCategory.groupGOResult

### merge_result
`merge_result(enrichResultList)`

- 来源：`compareCluster.R` · 包：clusterProfiler · 实现：merge_result

### simplify
`simplify(x, cutoff=0.7, by="p.adjust", select_fun=min, measure="Wang", semData=NULL)`

- 来源：`simplify.R` · 包：clusterProfiler · 实现：simplify.enrichResult
- 方法变体：`*compareClusterResult*`, `*enrichResult*`, `*gseaResult*`


## MODULE: viz — 可视化（dotplot/cnetplot/emapplot/gseaplot/heatmap/ridgeplot/goplot）（3）

### browseKEGG
`browseKEGG(x, pathID)`

- 来源：`kegg-utilities.R` · 包：clusterProfiler · 实现：browseKEGG

### plot
`plot(x, layout="nicely", ...)`

- 来源：`plot_interpret.R` · 包：clusterProfiler · 实现：plot.interpretation
- 方法变体：`*interpretation*`, `*interpretation_list*`

### plotGOgraph
`plotGOgraph(x, firstSigNodes=10, useInfo="all", sigForAll=TRUE, useFullNames=TRUE, ...)`

- 来源：`plotGOgraph.R` · 包：clusterProfiler · 实现：plotGOgraph


## MODULE: external — 外部数据（PPI / Uniprot / Taxa）（4）

### get_ppi
`get_ppi(x, ID=1, taxID="auto", required_score=NULL, network_type="functional", add_nodes=0, show_query_node_labels=0, output='igraph')`

- 来源：`ppi.R` · 包：clusterProfiler · 实现：getPPI

### get_ppi_network
`get_ppi_network(taxID=9606, version="12.0", score_threshold=400, output="data.frame")`

- 来源：`ppi.R` · 包：clusterProfiler · 实现：get_ppi_network

### getPPI
`getPPI(x, ID=1, taxID="auto", required_score=NULL, network_type="functional", add_nodes=0, show_query_node_labels=0, output='igraph')`

- 来源：`ppi.R` · 包：clusterProfiler · 实现：getPPI

### uniprot_get
`uniprot_get(taxID)`

- 来源：`uniprot.R` · 包：clusterProfiler · 实现：uniprot_get


## MODULE: llm — LLM 解读（interpret / interpret_agent / interpret_hierarchical）（4）

### interpret
`interpret(x, context=NULL, n_pathways=20, model=NULL, task="interpretation", prior=NULL, add_ppi=FALSE, gene_fold_change=NULL, max_tokens=8192, temperature=0.3, verbose=FALSE)`

- 来源：`interpret.R` · 包：clusterProfiler · 实现：interpret

### interpret_agent
`interpret_agent(x, context=NULL, n_pathways=50, model=NULL, add_ppi=FALSE, gene_fold_change=NULL, max_tokens=8192, temperature=0.3, verbose=FALSE)`

- 来源：`interpret.R` · 包：clusterProfiler · 实现：interpret_agent

### interpret_hierarchical
`interpret_hierarchical(x_minor, x_major, mapping, model=NULL, task="cell_type", max_tokens=8192, temperature=0.3)`

- 来源：`interpret.R` · 包：clusterProfiler · 实现：interpret_hierarchical

### print
`print(x, ...)`

- 来源：`interpret.R` · 包：clusterProfiler · 实现：print.interpretation
- 方法变体：`*interpretation*`, `*interpretation_list*`


## MODULE: dplyr — dplyr 风格 S3 method（arrange/filter/group_by/mutate/...）（9）

### arrange
`arrange(.data, ...)`

- 来源：`dplyr-arrange.R` · 包：clusterProfiler · 实现：arrange.enrichResult

### filter
`filter(.data, ..., .preserve=FALSE)`

- 来源：`dplyr-filter.R` · 包：clusterProfiler · 实现：filter.enrichResult

### group_by
`group_by(.data, ..., .add=FALSE, .drop=FALSE)`

- 来源：`dplyr-group_by.R` · 包：clusterProfiler · 实现：group_by.enrichResult

### mutate
`mutate(.data, ...)`

- 来源：`dplyr-mutate.R` · 包：clusterProfiler · 实现：mutate.enrichResult

### n
`n(?)`

- 来源：`—` · 包：clusterProfiler · 实现：—

### rename
`rename(.data, ...)`

- 来源：`dplyr-rename.R` · 包：clusterProfiler · 实现：rename.enrichResult

### select
`select(.data, ...)`

- 来源：`dplyr-select.R` · 包：clusterProfiler · 实现：select.enrichResult

### slice
`slice(.data, ..., .preserve=FALSE)`

- 来源：`dplyr-slice.R` · 包：clusterProfiler · 实现：slice.enrichResult

### summarise
`summarise(.data, ...)`

- 来源：`dplyr-summarise.R` · 包：clusterProfiler · 实现：summarise.enrichResult


## MODULE: reexport — 第三方包 re-export（enrichplot/dplyr/magrittr/...）（89）

### %<>%
`%<>%(lhs, rhs)`

- 来源：`—` · 包：magrittr · 实现：—

### %>%
`%>%(lhs, rhs)`

- 来源：`—` · 包：magrittr · 实现：—

### %||%
`%||%(lhs, rhs)`

- 来源：`—` · 包：rlang · 实现：—

### aes
`aes(x, y)`

- 来源：`—` · 包：ggplot2 · 实现：—

### Agent
`Agent(description, name, model)`

- 来源：`—` · 包：aisdk · 实现：—

### aggregate_enrichment
`aggregate_enrichment(res_list, method)`

- 来源：`—` · 包：enrichit · 实现：—

### aggregate_omics
`aggregate_omics(x, method, input, feature_type, conflict_policy)`

- 来源：`—` · 包：enrichit · 实现：—

### as_enrichResult
`as_enrichResult(x)`

- 来源：`—` · 包：enrichit · 实现：—

### as_gseaResult
`as_gseaResult(x)`

- 来源：`—` · 包：enrichit · 实现：—

### bayes_enrich
`bayes_enrich(x, candidate, n_terms, by, prior, false_positive, false_negative, n_iter, burnin, thin, posterior_cutoff, seed, verbose)`

- 来源：`—` · 包：enrichit · 实现：—

### bayes_summary
`bayes_summary(x, active, n)`

- 来源：`—` · 包：enrichit · 实现：—

### browseURL
`browseURL(url)`

- 来源：`—` · 包：utils · 实现：—

### build_go_graph
`build_go_graph(ont, organism)`

- 来源：`—` · 包：enrichit · 实现：—

### build_kegg_graph
`build_kegg_graph(organism)`

- 来源：`—` · 包：enrichit · 实现：—

### build_string_graph
`build_string_graph(taxID)`

- 来源：`—` · 包：enrichit · 实现：—

### buildGOmap
`buildGOmap(gostats, db, ont, genome)`

- 来源：`—` · 包：GOSemSim · 实现：—

### ChatSession
`ChatSession(agent, user_message)`

- 来源：`—` · 包：aisdk · 实现：—

### citation
`citation(package)`

- 来源：`—` · 包：utils · 实现：—

### classify_omics_pattern
`classify_omics_pattern(x)`

- 来源：`—` · 包：enrichit · 实现：—

### cnetplot
`cnetplot(x, showCategory, foldChange, layout, colorEdge, nodeLabel, cex_category, cex_gene, cex_label_category, cex_label_gene, categorySize, shadowtext, color_category)`

- 来源：`—` · 包：enrichplot · 实现：—

### collapse_multilayer_scores
`collapse_multilayer_scores(scores)`

- 来源：`—` · 包：enrichit · 实现：—

### dlply
`dlply(.data, .variables, .fun)`

- 来源：`—` · 包：plyr · 实现：—

### dotplot
`dotplot(object, x, showCategory, size, title, font.size, label_format, color, orderBy, decreasing, xlim, ylim)`

- 来源：`—` · 包：enrichplot · 实现：—

### download_yulab_file
`download_yulab_file(url, destfile, method, extra)`

- 来源：`—` · 包：yulab.utils · 实现：—

### emapplot
`emapplot(x, showCategory, color, layout, cex_category, cex_line, min_edge, group_category, group_legend, node_label, label_format)`

- 来源：`—` · 包：enrichplot · 实现：—

### extract_mnsea_subnetwork
`extract_mnsea_subnetwork(x)`

- 来源：`—` · 包：enrichit · 实现：—

### formula
`formula(?)`

- 来源：`—` · 包：stats · 实现：—

### gather
`gather(data, key, value)`

- 来源：`—` · 包：tidyr · 实现：—

### generate_object
`generate_object(session, schema, prompt)`

- 来源：`—` · 包：aisdk · 实现：—

### geom_label
`geom_label(mapping, data)`

- 来源：`—` · 包：ggplot2 · 实现：—

### geom_point
`geom_point(mapping, data)`

- 来源：`—` · 包：ggplot2 · 实现：—

### get_cache
`get_cache(dir, create)`

- 来源：`—` · 包：yulab.utils · 实现：—

### get_cache_item
`get_cache_item(key, cache_dir)`

- 来源：`—` · 包：yulab.utils · 实现：—

### get_fun_from_pkg
`get_fun_from_pkg(pkg, fun)`

- 来源：`—` · 包：yulab.utils · 实现：—

### get_mnsea_contribution
`get_mnsea_contribution(x)`

- 来源：`—` · 包：enrichit · 实现：—

### get_omics_contribution
`get_omics_contribution(x)`

- 来源：`—` · 包：enrichit · 实现：—

### get_organism
`get_organism(db)`

- 来源：`—` · 包：GOSemSim · 实现：—

### ggplot
`ggplot(data, mapping)`

- 来源：`—` · 包：ggplot2 · 实现：—

### ggtitle
`ggtitle(label)`

- 来源：`—` · 包：ggplot2 · 实现：—

### godata
`godata(ont, organism, db, keytype)`

- 来源：`—` · 包：GOSemSim · 实现：—

### goplot
`goplot(x, showCategory, color, size, geom, hi, lo, font.size)`

- 来源：`—` · 包：enrichplot · 实现：—

### gsea
`gsea(gene_list, pathway)`

- 来源：`—` · 包：enrichit · 实现：—

### gseaplot
`gseaplot(x, geneSetID, by, type, color, title, pvalue_table)`

- 来源：`—` · 包：enrichplot · 实现：—

### gseaScores
`gseaScores(geneList)`

- 来源：`—` · 包：enrichit · 实现：—

### gsfilter
`gsfilter(x, by, min, max)`

- 来源：`—` · 包：enrichit · 实现：—

### gson
`gson(gsid2gene, gsid2name, species, gsname, version, keytype, accessed_date, file, obo)`

- 来源：`—` · 包：gson · 实现：—

### harmonize_ids
`harmonize_ids(x, mapping, from, to, collapse)`

- 来源：`—` · 包：enrichit · 实现：—

### head
`head(x, n=6L, ...)`

- 来源：`accessor.R` · 包：utils · 实现：head.compareClusterResult
- 方法变体：`*compareClusterResult*`

### heatplot
`heatplot(x, showCategory, foldChange, color, label)`

- 来源：`—` · 包：enrichplot · 实现：—

### installed.packages
`installed.packages(pkgs, lib)`

- 来源：`—` · 包：utils · 实现：—

### is
`is(object, class2)`

- 来源：`—` · 包：methods · 实现：—

### is.installed
`is.installed(pkg)`

- 来源：`—` · 包：yulab.utils · 实现：—

### keys
`keys(x, k)`

- 来源：`—` · 包：AnnotationDbi · 实现：—

### keytypes
`keytypes(x)`

- 来源：`—` · 包：AnnotationDbi · 实现：—

### ldply
`ldply(.data, .fun)`

- 来源：`—` · 包：plyr · 实现：—

### llply
`llply(.data, .fun)`

- 来源：`—` · 包：plyr · 实现：—

### load_OrgDb
`load_OrgDb(orgdb)`

- 来源：`—` · 包：yulab.utils · 实现：—

### mgoSim
`mgoSim(GO1, GO2, semData, measure, combine)`

- 来源：`—` · 包：GOSemSim · 实现：—

### modifyList
`modifyList(x, val)`

- 来源：`—` · 包：utils · 实现：—

### new
`new(Class)`

- 来源：`—` · 包：methods · 实现：—

### Ontology
`Ontology(object)`

- 来源：`—` · 包：AnnotationDbi · 实现：—

### ora
`ora(gene, pathway)`

- 来源：`—` · 包：enrichit · 实现：—

### packageDescription
`packageDescription(pkg, lib)`

- 来源：`—` · 包：utils · 实现：—

### prepare_multilayer_network
`prepare_multilayer_network(graphs)`

- 来源：`—` · 包：enrichit · 实现：—

### prepare_network
`prepare_network(graph, organism)`

- 来源：`—` · 包：enrichit · 实现：—

### propagate_multilayer
`propagate_multilayer(multilayer_graph)`

- 来源：`—` · 包：enrichit · 实现：—

### read.blast2go
`read.blast2go(file, format)`

- 来源：`—` · 包：GOSemSim · 实现：—

### read.gaf
`read.gaf(file)`

- 来源：`—` · 包：GOSemSim · 实现：—

### read.gmt
`read.gmt(gmtfile, output="data.frame")`

- 来源：`pathwayCommons.R` · 包：gson · 实现：read.gmt.pc
- 方法变体：`*pc*`, `*pc_internal*`

### read.gmt.wp
`read.gmt.wp(gmtfile)`

- 来源：`—` · 包：gson · 实现：—

### read.table
`read.table(file, header, sep, quote, dec)`

- 来源：`—` · 包：utils · 实现：—

### ridgeplot
`ridgeplot(x, showCategory, label_format, fill, orderBy, decreasing, scale_bar)`

- 来源：`—` · 包：enrichplot · 实现：—

### scale_color_manual
`scale_color_manual(values)`

- 来源：`—` · 包：ggplot2 · 实现：—

### select_features_for_ora
`select_features_for_ora(x, cutoff, by)`

- 来源：`—` · 包：enrichit · 实现：—

### separate
`separate(data, col, into, sep, remove, convert)`

- 来源：`—` · 包：tidyr · 实现：—

### setNames
`setNames(object, nm)`

- 来源：`—` · 包：stats · 实现：—

### setReadable
`setReadable(x, OrgDb, keyType, toType)`

- 来源：`—` · 包：enrichit · 实现：—

### stack
`stack(x)`

- 来源：`—` · 包：utils · 实现：—

### str
`str(object)`

- 来源：`—` · 包：utils · 实现：—

### tail
`tail(x, n=6L, ...)`

- 来源：`accessor.R` · 包：utils · 实现：tail.compareClusterResult
- 方法变体：`*compareClusterResult*`

### theme_void
`theme_void(?)`

- 来源：`—` · 包：ggplot2 · 实现：—

### toTable
`toTable(x)`

- 来源：`—` · 包：AnnotationDbi · 实现：—

### user_dir
`user_dir(.appname)`

- 来源：`—` · 包：yulab.utils · 实现：—

### yread
`yread(file)`

- 来源：`—` · 包：yulab.utils · 实现：—

### yread_tsv
`yread_tsv(file)`

- 来源：`—` · 包：yulab.utils · 实现：—

### z_array
`z_array(items)`

- 来源：`—` · 包：aisdk · 实现：—

### z_enum
`z_enum(values)`

- 来源：`—` · 包：aisdk · 实现：—

### z_object
`z_object(fields)`

- 来源：`—` · 包：aisdk · 实现：—

### z_string
`z_string(?)`

- 来源：`—` · 包：aisdk · 实现：—
