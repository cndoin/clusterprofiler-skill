# MicrobiotaProcess — 1.25.0

> 数据源：github.com/YuLab-SMU/MicrobiotaProcess@devel
> 156 个已知符号

## Function (147)

- `%<>%(?)`
- `%>%(?)`
- `arrange(.data, ..., by_group=FALSE, keep.mpse=FALSE)`
- `as.MPSE(.data, ...)`
- `as.mpse(.data, ...)`
- `as.phyloseq(x, .abundance, ...)`
- `as.treedata(tree, include.rownames=FALSE, use_taxatree=TRUE, tiplevel="OTU", ...)`
- `as_phyloseq(x, .abundance, ...)`
- `as_tibble(x, ...)`
- `build_tree(seqs, ...)`
- `colData(?)`
- `colData<-(?)`
- `convert_to_treedata(data, type="species", include.rownames=FALSE, ...)`
- `diff_analysis(obj, ...)`
- `distinct(.data, ..., .keep_all=FALSE)`
- `dr_extract(name, .f=NULL)`
- `drop_taxa(obj, ...)`
- `extract(?)`
- `extract_binary_offspring(.data, .node, type='tips', ...)`
- `filter(.data, ..., .preserve=FALSE, keep.mpse=TRUE)`
- `fortify(model, data, .slot="colData", ...)`
- `generalizedFC(x, y, base=10, steps=0.05, pseudo=0.00001, data, subset, na.action, ...)`
- `get_alltaxadf(obj, method=NULL, type="species", include.rownames=FALSE, ...)`
- `get_alphaindex(obj, mindepth, sampleda, force=FALSE, ...)`
- `get_clust(obj, distmethod="euclidean", sampleda=NULL, hclustmethod="average", method="hellinger", ...)`
- `get_coord(obj, pc)`
- `get_count(data, featurelist, ...)`
- `get_dist(obj, distmethod="euclidean", method="hellinger", ...)`
- `get_mean_median(datameta, feature, subclass)`
- `get_NRI_NTI(obj, mindepth, sampleda, tree, metric=c('PAE', 'NRI', 'NTI', 'PD', 'HAED', ..., abundance.weighted=TRUE, ...)`
- `get_pca(obj, method="hellinger", ...)`
- `get_pcoa(obj, distmethod="euclidean", data=NULL, sampleda=NULL, method="hellinger", ...)`
- `get_pvalue(obj)`
- `get_rarecurve(obj, ...)`
- `get_ratio(data, featurelist, ...)`
- `get_sampledflist(dalist, bootnums=30, ratio=0.7, makerownames=FALSE)`
- `get_taxadf(obj, taxlevel=2, type="species", ...)`
- `get_upset(obj, ...)`
- `get_varct(obj, ...)`
- `get_vennlist(obj, factorNames, ...)`
- `ggbartax(obj, ...)`
- `ggbartaxa(obj, ...)`
- `ggbox(obj, factorNames, ...)`
- `ggclust(obj, layout="rectangular", factorNames=NULL, factorLevels=NULL, pointsize=2, fontsize=2.6, hjust=-0.1, ...)`
- `ggdiffbartaxa(obj, ...)`
- `ggdiffbox(obj, geom="boxplot", box_notch=TRUE, box_width=0.05, dodge_width=0.6, addLDA=TRUE, factorLevels=NULL, featurelist=NULL, removeUnknown=TRUE, colorlist=NULL, l_xlabtext=NULL, ...)`
- `ggdiffclade(obj, size, removeUnknown=TRUE, ...)`
- `ggdifftaxbar(obj, featurename, classgroup, subclass, xtextsize=3, factorLevels=NULL, coloslist=NULL, ylabel="relative abundance", filepath=NULL, output="biomarker_barplot", removeUnknown=TRUE, figwidth=6, figheight=3, format="pdf", dpi=300, ...)`
- `ggeffectsize(obj, removeUnknown=TRUE, setFacet=TRUE, ...)`
- `ggordpoint(obj, pc=c(1,2), mapping=NULL, sampleda=NULL, factorNames=NULL, factorLevels=NULL, poinsize=2, linesize=0.3, arrowsize=1.5, arrowlinecolour="grey", ellipse=FALSE, showsample=FALSE, ellipse_pro=0.9, ellipse_alpha=0.2, ellipse_linewd=0.5, ellipse_lty=3, biplot=FALSE, topn=5, settheme=TRUE, speciesannot=FALSE, fontsize=2.5, labelfactor=NULL, stroke=0.1, fontface="bold.italic", fontfamily="sans", textlinesize=0.02, ...)`
- `ggrarecurve(obj, chunks=400, factorLevels=NULL, indexNames="Observe", linesize=0.5, facetnrow=1, shadow=TRUE, factorNames, se=FALSE, method="lm", formula=y ~ log(x), ...)`
- `group_by(.data, ..., .add=FALSE, .drop=group_by_drop_default(.data))`
- `import_dada2(seqtab, taxatab=NULL, reftree=NULL, sampleda=NULL, ...)`
- `import_qiime2(otuqza, taxaqza=NULL, mapfilename=NULL, refseqqza=NULL, treeqza=NULL, parallel=FALSE, ...)`
- `left_join(x, y, by=NULL, copy=FALSE, suffix=c("", ".y"), ...)`
- `mp_adonis(?)`
- `mp_aggregate(?)`
- `mp_aggregate_clade(?)`
- `mp_anosim(.data, .abundance, .group, distmethod="bray", action="add", permutations=999, seed=123, ...)`
- `mp_balance_clade(?)`
- `mp_cal_abundance(.data, .abundance=NULL, .group=NULL, relative=TRUE, action="add", force=FALSE, ...)`
- `mp_cal_alpha(.data, .abundance=NULL, action="add", force=FALSE, ...)`
- `mp_cal_cca(.data, .abundance, .formula=NULL, .dim=3, action="add", ...)`
- `mp_cal_clust(?)`
- `mp_cal_dca(.data, .abundance, .dim=3, action="add", origin=TRUE, ...)`
- `mp_cal_dist(?)`
- `mp_cal_divergence(?)`
- `mp_cal_nmds(.data, .abundance, distmethod="bray", .dim=2, action="add", seed=123, ...)`
- `mp_cal_pca(.data, .abundance, .dim=3, action="add", ...)`
- `mp_cal_pcoa(.data, .abundance, distmethod="bray", .dim=3, action="add", ...)`
- `mp_cal_pd_metric(.data, .abundance, action="add", metric=c('PAE', 'NRI', 'NTI', 'PD', 'HAED', ...)`
- `mp_cal_rarecurve(.data, .abundance=NULL, action="add", chunks=400, seed=123, force=FALSE, ...)`
- `mp_cal_rda(.data, .abundance, .formula=NULL, .dim=3, action="add", ...)`
- `mp_cal_upset(.data, .group, .abundance=NULL, action="add", force=FALSE, ...)`
- `mp_cal_venn(.data, .group, .abundance=NULL, action="add", force=FALSE, ...)`
- `mp_decostand(.data, .abundance=NULL, method="hellinger", logbase=2, ...)`
- `mp_diff_analysis(?)`
- `mp_diff_clade(?)`
- `mp_dmn(?)`
- `mp_dmngroup(?)`

## Generic (6)

- `as.data.frame(x, ...)`
- `dim(x)`
- `ggplot_add(object, plot, object_name, ...)`
- `head(x, n=6L, ...)`
- `print(object, x, n=NULL, width=NULL, max_extra_cols=NULL, max_footer_lines=NULL, ...)`
- `tail(x, n=6L, ...)`

## S4method (3)

- `[(?)`
- `rownames<-(?)`
- `show(?)`
