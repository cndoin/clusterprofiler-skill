# enrichit — 0.2.5

> 数据源：YuLab-SMU/enrichit @ devel
> 52 个已知符号

## Function (30)

- `aggregate_enrichment(res_list, method=c("brown", "fisher", "stouffer"), ...)`
- `aggregate_omics(x, method=c("fisher", "stouffer", "brown", "mea..., input=c("pvalue", "signed_score"), feature_type="gene", conflict_policy=c("keep_all", "strict", "penalty"), ...)`
- `as_enrichResult(x, geneSets=NULL, gene=NULL, universe=NULL, ontology="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", pAdjustMethod="BH", ...)`
- `as_gseaResult(x, geneList, geneSets=NULL, setType="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", exponent=1, scoreType="std", pAdjustMethod="BH", ...)`
- `bayes_enrich(x, candidate=c("top", "significant", "all"), n_terms=200, by="p.adjust", prior=0.1, false_positive=0.01, false_negative=0.1, n_iter=5000, burnin=1000, thin=1, posterior_cutoff=0.5, seed=NULL, verbose=FALSE)`
- `bayes_summary(x, active=FALSE, n=Inf)`
- `classify_omics_pattern(merged_res, single_res, p_cutoff=0.05, by="p.adjust")`
- `collapse_multilayer_scores(x, collapse=c("weighted_mean", "sum", "mean", "ma..., layer_weights=NULL, output_space=c("union", "gene"), mapping=NULL, target_layer=NULL)`
- `EXTID2NAME(OrgDb, geneID, keytype, toType="SYMBOL")`
- `extract_mnsea_subnetwork(res, pathway_id=NULL, include_couplings=TRUE, include_isolated=TRUE)`
- `geneID(x)`
- `geneInCategory(x)`
- `get_mnsea_contribution(res, pathway_id=NULL, level=c("pathway", "feature"))`
- `get_omics_contribution(res, agg, pathway_id=NULL)`
- `gsea(geneList, gene_sets, weight=NULL, minGSSize=10, maxGSSize=500, nPerm=1000, exponent=1.0, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, eps=1e-10, sampleSize=101, seed=FALSE, nPermSimple=1000, scoreType="std", verbose=TRUE)`
- `gsea_gson(geneList, gson, weight=NULL, nPerm=1000, exponent=1.0, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, seed=FALSE, verbose=TRUE, ...)`
- `gseaScores(geneList, geneSet, exponent=1, fortify=FALSE)`
- `gsfilter(x, by="GSSize", min=NA, max=NA)`
- `harmonize_ids(x, mapping, from="protein", to="gene", collapse=c("max_abs", "mean", "min_p"))`
- `mnsea(seed_list, networks, couplings, gene_sets, mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`
- `mnsea_gson(seed_list, networks, couplings, gson, mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)`
- `nsea(geneList, network, gene_sets, mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, significance=c("whole_pipeline", "internal"), nPerm=1000, seed=NULL, exponent=1, verbose=TRUE, ...)`
- `nsea_gson(geneList, network, gson, mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, significance=c("whole_pipeline", "internal"), nPerm=1000, seed=NULL, exponent=1, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, ...)`
- `ora(gene, gene_sets, universe, weight=NULL)`
- `ora_gson(gene, pvalueCutoff, pAdjustMethod="BH", universe=NULL, weight=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, gson)`
- `prepare_multilayer_network(networks, couplings, directed=FALSE, intra_normalize="column", inter_normalize="column", interlayer_strength=1, layer_order=names(networks))`
- `prepare_network(network, directed=FALSE, normalize="column")`
- `propagate_multilayer(seed_list, network, mode=c("evidence", "signed"), p=0.5, threshold=1e-9, maxIter=100, layer_weights=NULL, target_layer=NULL)`
- `select_features_for_ora(x, cutoff=0.05, by=c("pvalue", "score"), ...)`
- `setReadable(x, OrgDb, keyType="auto", toType="SYMBOL")`

## Generic (2)

- `as.data.frame(x, ...)`
- `dim(x)`

## S4method (1)

- `summary(?)`

## Reexport (19)

- `.hasSlot(?)`
- `check_installed(?)`
- `colSums(?)`
- `Diagonal(?)`
- `head(x, n=6L, ...)`
- `is(?)`
- `median(?)`
- `new(?)`
- `p.adjust(?)`
- `pchisq(?)`
- `pnorm(?)`
- `qnorm(?)`
- `rowSums(?)`
- `setNames(?)`
- `show(?)`
- `sourceCpp(?)`
- `sparseMatrix(?)`
- `str(?)`
- `tail(x, n=6L, ...)`
