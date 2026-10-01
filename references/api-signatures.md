# clusterprofiler-skill · 全量函数签名（按生态包分组）

> 数据源：github.com/YuLab-SMU/<生态包>@devel
> 每条签名由 `R/` 源码的真实 `formals` 解析得到；第三方包 re-export 函数用 THIRD_PARTY_PARAMS 手工核对。
> 用法：`grep -n "^### <函数名>"` 精确查，不要整篇读。

涵盖 37 个 Y 叔生态包，1284 个已知符号（其中 987 个解析到真实参数表）。

## CNEr (?) — 0 symbols

## ChIPseeker (1.49.2) — 48 symbols

### Function (40)
- `.(..., .env=parent.frame())` — pkg=ChIPseeker
- `annotatePeak(peak, tssRegion=c(-3000, 3000), TxDb=NULL, level="transcript", assignGenomicAnnotation=TRUE, genomicAnnotationPriority=c("Promoter", "5UTR", "3UTR", "Exon",..., annoDb=NULL, addFlankGeneInfo=FALSE, flankDistance=5000, sameStrand=FALSE, ignoreOverlap=FALSE, ignoreUpstream=FALSE, ignoreDownstream=FALSE, overlap="TSS", verbose=TRUE, columns=c("ENTREZID", "ENSEMBL", "SYMBOL", "G...)` — pkg=ChIPseeker
- `as.GRanges(x)` — pkg=ChIPseeker
- `combine_csAnno(x, ...)` — pkg=ChIPseeker
- `covplot(peak, weightCol=NULL, xlab="Chromosome Size (bp)", ylab="", title="ChIP Peaks over Chromosomes", chrs=NULL, xlim=NULL, lower=1, fill_color="black")` — pkg=ChIPseeker
- `downloadGEObedFiles(genome, destDir=getwd())` — pkg=ChIPseeker
- `downloadGSMbedFiles(GSM, destDir=getwd())` — pkg=ChIPseeker
- `dropAnno(csAnno, distanceToTSS_cutoff=10000)` — pkg=ChIPseeker
- `enrichAnnoOverlap(queryPeak, targetPeak, TxDb=NULL, pAdjustMethod="BH", chainFile=NULL, distanceToTSS_cutoff=NULL)` — pkg=ChIPseeker
- `enrichPeakOverlap(queryPeak, targetPeak, TxDb=NULL, pAdjustMethod="BH", nShuffle=1000, chainFile=NULL, pool=TRUE, mc.cores=detectCores()-1, verbose=TRUE)` — pkg=ChIPseeker
- `getAnnoStat(x)` — pkg=ChIPseeker
- `getBioRegion(TxDb=NULL, upstream=1000, downstream=1000, by="gene", type="start_site")` — pkg=ChIPseeker
- `getGEOgenomeVersion(?)` — pkg=ChIPseeker
- `getGEOInfo(genome, simplify=TRUE)` — pkg=ChIPseeker
- `getGEOspecies(?)` — pkg=ChIPseeker
- `getPromoters(TxDb=NULL, upstream=1000, downstream=1000, by="gene")` — pkg=ChIPseeker
- `getSampleFiles(?)` — pkg=ChIPseeker
- `getTagMatrix(peak, upstream, downstream, windows, type, by, TxDb=NULL, weightCol=NULL, nbin=NULL, verbose=TRUE, ignore_strand=FALSE)` — pkg=ChIPseeker
- `GRangesList(?)` — pkg=ChIPseeker
- `makeBioRegionFromGranges(gr, by, type, upstream=1000, downstream=1000)` — pkg=ChIPseeker
- `overlap(Sets)` — pkg=ChIPseeker
- `peak_Profile_Heatmap(peak, weightCol=NULL, TxDb=NULL, upstream=1000, downstream=1000, xlab="", ylab="", title=NULL, palette=NULL, verbose=TRUE, by="gene", type="start_site", nbin=NULL, ignore_strand=FALSE, windows_name=NULL, ncol=NULL, nrow=NULL, facet_label_text_size=12, conf, facet="row", free_y=TRUE, height_proportion=4)` — pkg=ChIPseeker
- `peakHeatmap(peak, weightCol=NULL, TxDb=NULL, upstream=1000, downstream=1000, xlab="", ylab="", title=NULL, palette=NULL, verbose=TRUE, by="gene", type="start_site", nbin=NULL, ignore_strand=FALSE, windows, ncol=NULL, nrow=NULL)` — pkg=ChIPseeker
- `peakHeatmap_multiple_Sets(peak, weightCol=NULL, TxDb=NULL, upstream=1000, downstream=1000, xlab="", ylab="", title=NULL, palette=NULL, verbose=TRUE, by="gene", type="start_site", nbin=NULL, ignore_strand=FALSE, windows_name=NULL, ncol=NULL, nrow=NULL, facet_label_text_size=12)` — pkg=ChIPseeker
- `plotAnnoBar(x, xlab="", ylab='Percentage(%)` — pkg=ChIPseeker
- `plotAnnoPie(x, ndigit=2, cex=0.8, col=NA, legend.position="rightside", pie3D=FALSE, radius=0.8, ...)` — pkg=ChIPseeker
- `plotAnnoPie.csAnno(x, ndigit=2, cex=0.8, col=NA, legend.position="rightside", pie3D=FALSE, radius=0.8, ...)` — pkg=ChIPseeker
- `plotAvgProf(tagMatrix, conf, xlim=c(-3000,3000), xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", facet="none", free_y=TRUE, origin_label, upstream=NULL, downstream=NULL, label, ...)` — pkg=ChIPseeker
- `plotAvgProf2(peak, weightCol=NULL, TxDb=NULL, upstream=1000, downstream=1000, xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", conf, facet="none", free_y=TRUE, verbose=TRUE, ignore_strand=FALSE, ...)` — pkg=ChIPseeker
- `plotDistToTSS(x, distanceColumn="distanceToTSS", xlab="", ylab="Binding sites (%)` — pkg=ChIPseeker
- `plotPeakProf(tagMatrix=NULL, peak, upstream, downstream, conf, by, type, windows_name=NULL, weightCol=NULL, TxDb=NULL, xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", facet="row", free_y=TRUE, verbose=TRUE, nbin=NULL, ignore_strand=FALSE, ...)` — pkg=ChIPseeker
- `plotPeakProf2(peak, upstream, downstream, conf, by, type, weightCol=NULL, TxDb=NULL, xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", facet="none", free_y=TRUE, verbose=TRUE, nbin=NULL, ignore_strand=FALSE, ...)` — pkg=ChIPseeker
- `readPeakFile(peakfile, as="GRanges", ...)` — pkg=ChIPseeker
- `rel(?)` — pkg=ChIPseeker
- `seq2gene(seq, tssRegion, flankDistance, TxDb, sameStrand=FALSE)` — pkg=ChIPseeker
- `shuffle(peak.gr, TxDb)` — pkg=ChIPseeker
- `tagHeatmap(tagMatrix, xlab="", ylab="", title=NULL, palette="RdBu", nrow=NULL, ncol=NULL)` — pkg=ChIPseeker
- `vennpie(x, r=0.2, cex=1.2, col=NULL)` — pkg=ChIPseeker
- `vennplot(Sets, by="gplots", ...)` — pkg=ChIPseeker
- `vennplot.peakfile(files, labels=NULL)` — pkg=ChIPseeker

### Generic (6)
- `arrange(.data, .by_group=FALSE, ...)` — pkg=ChIPseeker
- `as.data.frame(x, row.names=NULL, optional=FALSE, ...)` — pkg=ChIPseeker
- `filter(.data, .by=NULL, .preserve=FALSE, ...)` — pkg=ChIPseeker
- `mutate(.data, .by=NULL, .keep=c("all", "used", "unused", "none"), .before=NULL, .after=NULL, ...)` — pkg=ChIPseeker
- `rename(x, ...)` — pkg=ChIPseeker
- `subset(x, ...)` — pkg=ChIPseeker

### S4method (2)
- `show(?)` — pkg=ChIPseeker
- `upsetplot(?)` — pkg=ChIPseeker

## DOSE (4.7.3) — 23 symbols

### Function (20)
- `clusterSim(cluster1, cluster2, ont="HDO", organism=NULL, measure="Wang", combine="BMA")` — pkg=DOSE
- `doseInterpretResult(result=NULL, evidence=NULL, query=NULL, sources=NULL, parameters=list(), explanation=list())` — pkg=DOSE
- `doseSim(DOID1, DOID2, measure="Wang", ont="HDO")` — pkg=DOSE
- `doSim(DOID1, DOID2, measure="Wang", ont="HDO")` — pkg=DOSE
- `enrichDO(gene, ont="HDO", organism=NULL, pvalueCutoff=0.05, pAdjustMethod="BH", universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, readable=FALSE)` — pkg=DOSE
- `enrichNCG(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, readable=FALSE)` — pkg=DOSE
- `evidence(x, target_id=NULL, type=NULL, source=NULL, direction=NULL)` — pkg=DOSE
- `explainDisease(x, method=c("template", "llm"), max_features=3L, provider=NULL, model=NULL, language=c("en", "zh"), style=c("brief", "research", "cautious"), generation_params=list(), llm_adapter=NULL)` — pkg=DOSE
- `facet_grid(?)` — pkg=DOSE
- `gene2DO(gene, organism=NULL, ont="HDO")` — pkg=DOSE
- `geneSim(geneID1, geneID2=NULL, ont="HDO", organism=NULL, measure="Wang", combine="BMA")` — pkg=DOSE
- `get_organism(?)` — pkg=DOSE
- `gseDO(geneList, ont="HDO", organism=NULL, exponent=1, nPerm=1000, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, method="multilevel", adaptive=FALSE, minPerm=1000, maxPerm=10000, seed=FALSE, ...)` — pkg=DOSE
- `gseNCG(geneList, exponent=1, nPerm=1000, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, method="multilevel", adaptive=FALSE, minPerm=1000, maxPerm=10000, seed=FALSE, ...)` — pkg=DOSE
- `interpretDisease(x, input=c("auto", "gene", "ranked_gene", "gen..., organism=c("human", "mouse"), target=c("disease", "mouse_model", "both"), ontology="auto", id_type="auto", orthology=c("one_to_one", "all"), explain=c("none", "template", "llm"), top=50, ...)` — pkg=DOSE
- `mclusterSim(clusters, ont="HDO", organism=NULL, measure="Wang", combine="BMA")` — pkg=DOSE
- `rankMouseModels(gene, disease_model_file, homology_file, gene_pheno_file, top=50)` — pkg=DOSE
- `set_auto_update(?)` — pkg=DOSE
- `simplot(sim, xlab="", ylab="", color.low="white", color.high="red", labs=TRUE, digits=2, labs.size=3, font.size=14)` — pkg=DOSE
- `theme_dose(font.size=14)` — pkg=DOSE

### S4method (3)
- `as.data.frame(?)` — pkg=DOSE
- `show(?)` — pkg=DOSE
- `summary(?)` — pkg=DOSE

## GOSemSim (2.39.3) — 18 symbols

### Function (18)
- `buildGOmap(TERM2GENE)` — pkg=GOSemSim
- `clusterSim(cluster1, cluster2, semData, measure="Wang", drop="IEA", combine="BMA")` — pkg=GOSemSim
- `combineScores(SimScores, combine)` — pkg=GOSemSim
- `geneSim(gene1, gene2, semData, measure="Wang", drop="IEA", combine="BMA")` — pkg=GOSemSim
- `get_organism(object)` — pkg=GOSemSim
- `godata(OrgDb=NULL, annoDb=NULL, keytype="ENTREZID", ont, computeIC=TRUE, processTCSS=FALSE, cutoff=NULL)` — pkg=GOSemSim
- `goSim(GOID1, GOID2, semData, measure="Wang")` — pkg=GOSemSim
- `load_OrgDb(?)` — pkg=GOSemSim
- `mclusterSim(clusters, semData, measure="Wang", drop="IEA", combine="BMA", BPPARAM=NULL)` — pkg=GOSemSim
- `mgeneSim(genes, semData, measure="Wang", drop="IEA", combine="BMA", verbose=TRUE, BPPARAM=NULL)` — pkg=GOSemSim
- `mgoSim(GO1, GO2, semData, measure="Wang", combine="BMA")` — pkg=GOSemSim
- `parse_gff(file, asis=FALSE, add_indirect_GO=FALSE)` — pkg=GOSemSim
- `read.blast2go(file, add_indirect_GO=FALSE)` — pkg=GOSemSim
- `read.gaf(file, asis=FALSE, add_indirect_GO=FALSE)` — pkg=GOSemSim
- `set_auto_update(x=TRUE)` — pkg=GOSemSim
- `tcss_cutoff(OrgDb=NULL, keytype="ENTREZID", ont, combine_method="max", ppidata)` — pkg=GOSemSim
- `termSim(t1, t2, semData, method=c("Wang", "Resnik", "Rel", "Jiang", "...)` — pkg=GOSemSim
- `wangMethod_internal(ID1, ID2, ont="BP")` — pkg=GOSemSim

## HDO (?) — 0 symbols

## MicrobiomeProfiler (1.19.2) — 22 symbols

### Function (22)
- `available_datasets(include_remote=FALSE)` — pkg=MicrobiomeProfiler
- `clear_dataset_cache(dataset=NULL)` — pkg=MicrobiomeProfiler
- `dataset_cache_info(dataset=NULL)` — pkg=MicrobiomeProfiler
- `download_dataset(dataset, refresh=FALSE)` — pkg=MicrobiomeProfiler
- `enrichBugSigDB(microbe_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, refresh=FALSE)` — pkg=MicrobiomeProfiler
- `enrichCOG(gene, dtype="category", pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)` — pkg=MicrobiomeProfiler
- `enrichEggNOG(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, refresh=FALSE)` — pkg=MicrobiomeProfiler
- `enrichHMDB(metabo_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)` — pkg=MicrobiomeProfiler
- `enrichKO(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)` — pkg=MicrobiomeProfiler
- `enrichMBKEGG(metabo_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)` — pkg=MicrobiomeProfiler
- `enrichMDA(microbe_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, refresh=FALSE)` — pkg=MicrobiomeProfiler
- `enrichModule(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)` — pkg=MicrobiomeProfiler
- `enrichSMPDB(metabo_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)` — pkg=MicrobiomeProfiler
- `gseCOG(geneList, dtype="category", nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)` — pkg=MicrobiomeProfiler
- `gseEggNOG(geneList, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", refresh=FALSE, seed=FALSE)` — pkg=MicrobiomeProfiler
- `gseHMDB(metabo_list, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)` — pkg=MicrobiomeProfiler
- `gseKO(geneList, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)` — pkg=MicrobiomeProfiler
- `gseMBKEGG(metabo_list, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)` — pkg=MicrobiomeProfiler
- `gseMDA(microbe_list, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, refresh=FALSE, seed=FALSE)` — pkg=MicrobiomeProfiler
- `gseModule(geneList, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)` — pkg=MicrobiomeProfiler
- `gseSMPDB(metabo_list, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)` — pkg=MicrobiomeProfiler
- `run_MicrobiomeProfiler(onStart=NULL, options=list(), enableBookmarking=NULL, uiPattern="/", ...)` — pkg=MicrobiomeProfiler

## MicrobiotaProcess (1.25.0) — 156 symbols

### Function (147)
- `%<>%(?)` — pkg=MicrobiotaProcess
- `%>%(?)` — pkg=MicrobiotaProcess
- `arrange(.data, ..., by_group=FALSE, keep.mpse=FALSE)` — pkg=MicrobiotaProcess
- `as.MPSE(.data, ...)` — pkg=MicrobiotaProcess
- `as.mpse(.data, ...)` — pkg=MicrobiotaProcess
- `as.phyloseq(x, .abundance, ...)` — pkg=MicrobiotaProcess
- `as.treedata(tree, include.rownames=FALSE, use_taxatree=TRUE, tiplevel="OTU", ...)` — pkg=MicrobiotaProcess
- `as_phyloseq(x, .abundance, ...)` — pkg=MicrobiotaProcess
- `as_tibble(x, ...)` — pkg=MicrobiotaProcess
- `build_tree(seqs, ...)` — pkg=MicrobiotaProcess
- `colData(?)` — pkg=MicrobiotaProcess
- `colData<-(?)` — pkg=MicrobiotaProcess
- `convert_to_treedata(data, type="species", include.rownames=FALSE, ...)` — pkg=MicrobiotaProcess
- `diff_analysis(obj, ...)` — pkg=MicrobiotaProcess
- `distinct(.data, ..., .keep_all=FALSE)` — pkg=MicrobiotaProcess
- `dr_extract(name, .f=NULL)` — pkg=MicrobiotaProcess
- `drop_taxa(obj, ...)` — pkg=MicrobiotaProcess
- `extract(?)` — pkg=MicrobiotaProcess
- `extract_binary_offspring(.data, .node, type='tips', ...)` — pkg=MicrobiotaProcess
- `filter(.data, ..., .preserve=FALSE, keep.mpse=TRUE)` — pkg=MicrobiotaProcess
- `fortify(model, data, .slot="colData", ...)` — pkg=MicrobiotaProcess
- `generalizedFC(x, y, base=10, steps=0.05, pseudo=0.00001, data, subset, na.action, ...)` — pkg=MicrobiotaProcess
- `get_alltaxadf(obj, method=NULL, type="species", include.rownames=FALSE, ...)` — pkg=MicrobiotaProcess
- `get_alphaindex(obj, mindepth, sampleda, force=FALSE, ...)` — pkg=MicrobiotaProcess
- `get_clust(obj, distmethod="euclidean", sampleda=NULL, hclustmethod="average", method="hellinger", ...)` — pkg=MicrobiotaProcess
- `get_coord(obj, pc)` — pkg=MicrobiotaProcess
- `get_count(data, featurelist, ...)` — pkg=MicrobiotaProcess
- `get_dist(obj, distmethod="euclidean", method="hellinger", ...)` — pkg=MicrobiotaProcess
- `get_mean_median(datameta, feature, subclass)` — pkg=MicrobiotaProcess
- `get_NRI_NTI(obj, mindepth, sampleda, tree, metric=c('PAE', 'NRI', 'NTI', 'PD', 'HAED', ..., abundance.weighted=TRUE, ...)` — pkg=MicrobiotaProcess
- `get_pca(obj, method="hellinger", ...)` — pkg=MicrobiotaProcess
- `get_pcoa(obj, distmethod="euclidean", data=NULL, sampleda=NULL, method="hellinger", ...)` — pkg=MicrobiotaProcess
- `get_pvalue(obj)` — pkg=MicrobiotaProcess
- `get_rarecurve(obj, ...)` — pkg=MicrobiotaProcess
- `get_ratio(data, featurelist, ...)` — pkg=MicrobiotaProcess
- `get_sampledflist(dalist, bootnums=30, ratio=0.7, makerownames=FALSE)` — pkg=MicrobiotaProcess
- `get_taxadf(obj, taxlevel=2, type="species", ...)` — pkg=MicrobiotaProcess
- `get_upset(obj, ...)` — pkg=MicrobiotaProcess
- `get_varct(obj, ...)` — pkg=MicrobiotaProcess
- `get_vennlist(obj, factorNames, ...)` — pkg=MicrobiotaProcess
- `ggbartax(obj, ...)` — pkg=MicrobiotaProcess
- `ggbartaxa(obj, ...)` — pkg=MicrobiotaProcess
- `ggbox(obj, factorNames, ...)` — pkg=MicrobiotaProcess
- `ggclust(obj, layout="rectangular", factorNames=NULL, factorLevels=NULL, pointsize=2, fontsize=2.6, hjust=-0.1, ...)` — pkg=MicrobiotaProcess
- `ggdiffbartaxa(obj, ...)` — pkg=MicrobiotaProcess
- `ggdiffbox(obj, geom="boxplot", box_notch=TRUE, box_width=0.05, dodge_width=0.6, addLDA=TRUE, factorLevels=NULL, featurelist=NULL, removeUnknown=TRUE, colorlist=NULL, l_xlabtext=NULL, ...)` — pkg=MicrobiotaProcess
- `ggdiffclade(obj, size, removeUnknown=TRUE, ...)` — pkg=MicrobiotaProcess
- `ggdifftaxbar(obj, featurename, classgroup, subclass, xtextsize=3, factorLevels=NULL, coloslist=NULL, ylabel="relative abundance", filepath=NULL, output="biomarker_barplot", removeUnknown=TRUE, figwidth=6, figheight=3, format="pdf", dpi=300, ...)` — pkg=MicrobiotaProcess
- `ggeffectsize(obj, removeUnknown=TRUE, setFacet=TRUE, ...)` — pkg=MicrobiotaProcess
- `ggordpoint(obj, pc=c(1,2), mapping=NULL, sampleda=NULL, factorNames=NULL, factorLevels=NULL, poinsize=2, linesize=0.3, arrowsize=1.5, arrowlinecolour="grey", ellipse=FALSE, showsample=FALSE, ellipse_pro=0.9, ellipse_alpha=0.2, ellipse_linewd=0.5, ellipse_lty=3, biplot=FALSE, topn=5, settheme=TRUE, speciesannot=FALSE, fontsize=2.5, labelfactor=NULL, stroke=0.1, fontface="bold.italic", fontfamily="sans", textlinesize=0.02, ...)` — pkg=MicrobiotaProcess
- `ggrarecurve(obj, chunks=400, factorLevels=NULL, indexNames="Observe", linesize=0.5, facetnrow=1, shadow=TRUE, factorNames, se=FALSE, method="lm", formula=y ~ log(x), ...)` — pkg=MicrobiotaProcess
- `group_by(.data, ..., .add=FALSE, .drop=group_by_drop_default(.data))` — pkg=MicrobiotaProcess
- `import_dada2(seqtab, taxatab=NULL, reftree=NULL, sampleda=NULL, ...)` — pkg=MicrobiotaProcess
- `import_qiime2(otuqza, taxaqza=NULL, mapfilename=NULL, refseqqza=NULL, treeqza=NULL, parallel=FALSE, ...)` — pkg=MicrobiotaProcess
- `left_join(x, y, by=NULL, copy=FALSE, suffix=c("", ".y"), ...)` — pkg=MicrobiotaProcess
- `mp_adonis(?)` — pkg=MicrobiotaProcess
- `mp_aggregate(?)` — pkg=MicrobiotaProcess
- `mp_aggregate_clade(?)` — pkg=MicrobiotaProcess
- `mp_anosim(.data, .abundance, .group, distmethod="bray", action="add", permutations=999, seed=123, ...)` — pkg=MicrobiotaProcess
- `mp_balance_clade(?)` — pkg=MicrobiotaProcess
- `mp_cal_abundance(.data, .abundance=NULL, .group=NULL, relative=TRUE, action="add", force=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_cal_alpha(.data, .abundance=NULL, action="add", force=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_cal_cca(.data, .abundance, .formula=NULL, .dim=3, action="add", ...)` — pkg=MicrobiotaProcess
- `mp_cal_clust(?)` — pkg=MicrobiotaProcess
- `mp_cal_dca(.data, .abundance, .dim=3, action="add", origin=TRUE, ...)` — pkg=MicrobiotaProcess
- `mp_cal_dist(?)` — pkg=MicrobiotaProcess
- `mp_cal_divergence(?)` — pkg=MicrobiotaProcess
- `mp_cal_nmds(.data, .abundance, distmethod="bray", .dim=2, action="add", seed=123, ...)` — pkg=MicrobiotaProcess
- `mp_cal_pca(.data, .abundance, .dim=3, action="add", ...)` — pkg=MicrobiotaProcess
- `mp_cal_pcoa(.data, .abundance, distmethod="bray", .dim=3, action="add", ...)` — pkg=MicrobiotaProcess
- `mp_cal_pd_metric(.data, .abundance, action="add", metric=c('PAE', 'NRI', 'NTI', 'PD', 'HAED', ...)` — pkg=MicrobiotaProcess
- `mp_cal_rarecurve(.data, .abundance=NULL, action="add", chunks=400, seed=123, force=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_cal_rda(.data, .abundance, .formula=NULL, .dim=3, action="add", ...)` — pkg=MicrobiotaProcess
- `mp_cal_upset(.data, .group, .abundance=NULL, action="add", force=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_cal_venn(.data, .group, .abundance=NULL, action="add", force=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_decostand(.data, .abundance=NULL, method="hellinger", logbase=2, ...)` — pkg=MicrobiotaProcess
- `mp_diff_analysis(?)` — pkg=MicrobiotaProcess
- `mp_diff_clade(?)` — pkg=MicrobiotaProcess
- `mp_dmn(?)` — pkg=MicrobiotaProcess
- `mp_dmngroup(?)` — pkg=MicrobiotaProcess
- `mp_envfit(?)` — pkg=MicrobiotaProcess
- `mp_extract_abundance(?)` — pkg=MicrobiotaProcess
- `mp_extract_assays(x, .abundance, byRow=TRUE, ...)` — pkg=MicrobiotaProcess
- `mp_extract_dist(?)` — pkg=MicrobiotaProcess
- `mp_extract_feature(x, addtaxa=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_extract_internal_attr(?)` — pkg=MicrobiotaProcess
- `mp_extract_otutree(x, ...)` — pkg=MicrobiotaProcess
- `mp_extract_rarecurve(?)` — pkg=MicrobiotaProcess
- `mp_extract_refseq(?)` — pkg=MicrobiotaProcess
- `mp_extract_sample(x, ...)` — pkg=MicrobiotaProcess
- `mp_extract_taxatree(x, tip.level="OTU", ...)` — pkg=MicrobiotaProcess
- `mp_extract_taxonomy(x, ...)` — pkg=MicrobiotaProcess
- `mp_extract_tree(x, type="taxatree", tip.level="OTU", ...)` — pkg=MicrobiotaProcess
- `mp_filter_taxa(.data, .abundance=NULL, min.abun=0, min.prop=0.05, include.lowest=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_fortify(model, verbose=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_import_biom(biomfilename, mapfilename=NULL, otutree=NULL, refseq=NULL, ...)` — pkg=MicrobiotaProcess
- `mp_import_dada2(seqtab, taxatab=NULL, reftree=NULL, sampleda=NULL, ...)` — pkg=MicrobiotaProcess
- `mp_import_humann_regroup(profile, mapfilename=NULL, rm.unknown=TRUE, keep.contribute.abundance=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_import_metaphlan(profile, mapfilename=NULL, treefile=NULL, linenum=NULL, ...)` — pkg=MicrobiotaProcess
- `mp_import_qiime(otufilename, mapfilename=NULL, otutree=NULL, refseq=NULL, ...)` — pkg=MicrobiotaProcess
- `mp_import_qiime2(otuqza, taxaqza=NULL, mapfilename=NULL, refseqqza=NULL, treeqza=NULL, parallel=FALSE, ...)` — pkg=MicrobiotaProcess
- `mp_mantel(?)` — pkg=MicrobiotaProcess
- `mp_mrpp(.data, .abundance, .group, distmethod="bray", action="add", permutations=999, seed=123, ...)` — pkg=MicrobiotaProcess
- `mp_plot_abundance(?)` — pkg=MicrobiotaProcess
- `mp_plot_alpha(?)` — pkg=MicrobiotaProcess
- `mp_plot_diff_boxplot(?)` — pkg=MicrobiotaProcess
- `mp_plot_diff_cladogram(.data, .group, .size='pvalue', taxa.class, removeUnknown=FALSE, layout='radial', hilight.alpha=.3, hilight.size=.2, bg.tree.size=.15, bg.tree.color='#bed0d1', bg.point.color='#bed0d1', bg.point.fill='white', bg.point.stroke=.2, bg.point.size=2, label.size=2.6, tip.annot=TRUE, as.tiplab=TRUE, ...)` — pkg=MicrobiotaProcess
- `mp_plot_diff_manhattan(?)` — pkg=MicrobiotaProcess
- `mp_plot_diff_res(?)` — pkg=MicrobiotaProcess
- `mp_plot_dist(?)` — pkg=MicrobiotaProcess
- `mp_plot_ord(?)` — pkg=MicrobiotaProcess
- `mp_plot_rarecurve(?)` — pkg=MicrobiotaProcess
- `mp_plot_upset(?)` — pkg=MicrobiotaProcess
- `mp_plot_venn(?)` — pkg=MicrobiotaProcess
- `mp_rrarefy(.data, .abundance=NULL, raresize, trimOTU=FALSE, trimSample=FALSE, seed=123, ...)` — pkg=MicrobiotaProcess
- `mp_select_as_tip(?)` — pkg=MicrobiotaProcess
- `mp_stat_taxa(?)` — pkg=MicrobiotaProcess
- `MPSE(assays, colData=NULL, otutree=NULL, taxatree=NULL, refseq=NULL, ...)` — pkg=MicrobiotaProcess
- `multi_compare(fun=wilcox.test, data, feature, factorNames, subgroup=NULL, ...)` — pkg=MicrobiotaProcess
- `mutate(.data, keep.mpse=TRUE, ...)` — pkg=MicrobiotaProcess
- `nest(.data, ..., .names_sep=NULL)` — pkg=MicrobiotaProcess
- `otutree(x, ...)` — pkg=MicrobiotaProcess
- `otutree<-(?)` — pkg=MicrobiotaProcess
- `pull(.data, var=-1, name=NULL, ...)` — pkg=MicrobiotaProcess
- `read_qza(qzafile, parallel=FALSE)` — pkg=MicrobiotaProcess
- `refsequence(x, ...)` — pkg=MicrobiotaProcess
- `refsequence<-(?)` — pkg=MicrobiotaProcess
- `remove_missing(?)` — pkg=MicrobiotaProcess
- `rename(.data, ..., keep.mpse=TRUE)` — pkg=MicrobiotaProcess
- `rowData(?)` — pkg=MicrobiotaProcess
- `scale_fill_diff_cladogram(values, breaks=waiver(), na.value='grey50', ...)` — pkg=MicrobiotaProcess
- `select(.data, ..., keep.mpse=FALSE)` — pkg=MicrobiotaProcess
- `set_diff_boxplot_color(.data, values, ...)` — pkg=MicrobiotaProcess
- `set_scale_theme(.data, x, aes_var)` — pkg=MicrobiotaProcess
- `slice(.data, ..., .preserve=FALSE)` — pkg=MicrobiotaProcess
- `split_data(x, nums, chunks=NULL, random=FALSE)` — pkg=MicrobiotaProcess
- `split_str_to_list(strdataframe, prefix="tax", sep="; ", extra="drop", fill="right", ...)` — pkg=MicrobiotaProcess
- `tax_table(?)` — pkg=MicrobiotaProcess
- `taxatree(x, ...)` — pkg=MicrobiotaProcess
- `taxatree<-(?)` — pkg=MicrobiotaProcess
- `taxonomy(?)` — pkg=MicrobiotaProcess
- `taxonomy<-(?)` — pkg=MicrobiotaProcess
- `td_filter(?)` — pkg=MicrobiotaProcess
- `td_unnest(?)` — pkg=MicrobiotaProcess
- `theme_taxbar(axis.text.x=element_text(angle = -45, hjust = 0, ..., legend.position="bottom", legend.box="horizontal", legend.text=element_text(size = 8), legend.title=element_blank(), strip.text.x=element_text(size=12, face="bold"), strip.background=element_rect(colour="white", fill="gr..., ...)` — pkg=MicrobiotaProcess
- `ungroup(x, ...)` — pkg=MicrobiotaProcess
- `unnest(data, cols, ..., keep_empty=FALSE, ptype=NULL, names_sep=NULL, names_repair="check_unique")` — pkg=MicrobiotaProcess

### Generic (6)
- `as.data.frame(x, ...)` — pkg=MicrobiotaProcess
- `dim(x)` — pkg=MicrobiotaProcess
- `ggplot_add(object, plot, object_name, ...)` — pkg=MicrobiotaProcess
- `head(x, n=6L, ...)` — pkg=MicrobiotaProcess
- `print(object, x, n=NULL, width=NULL, max_extra_cols=NULL, max_footer_lines=NULL, ...)` — pkg=MicrobiotaProcess
- `tail(x, n=6L, ...)` — pkg=MicrobiotaProcess

### S4method (3)
- `[(?)` — pkg=MicrobiotaProcess
- `rownames<-(?)` — pkg=MicrobiotaProcess
- `show(?)` — pkg=MicrobiotaProcess

## ReactomePA (1.99.2) — 15 symbols

### Function (15)
- `bayes_reactome(x, candidate=c("top", "significant", "all"), n_terms=200, by="p.adjust", prior=0.1, false_positive=0.01, false_negative=0.1, n_iter=5000, burnin=1000, thin=1, posterior_cutoff=0.5, seed=NULL, verbose=FALSE)` — pkg=ReactomePA
- `cnetplot(?)` — pkg=ReactomePA
- `dotplot(?)` — pkg=ReactomePA
- `emapplot(?)` — pkg=ReactomePA
- `enrichPathway(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, weight=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, organism="human", readable=FALSE)` — pkg=ReactomePA
- `geneID(?)` — pkg=ReactomePA
- `geneInCategory(?)` — pkg=ReactomePA
- `gseaplot(?)` — pkg=ReactomePA
- `gsePathway(geneList, organism="human", exponent=1, weight=NULL, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)` — pkg=ReactomePA
- `gson_Reactome(organism="human")` — pkg=ReactomePA
- `heatplot(?)` — pkg=ReactomePA
- `nsePathway(geneList, organism="human", mode=c("evidence", "signed"), network=NULL, restart_prob=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, nPerm=1000, seed=NULL, verbose=TRUE, ...)` — pkg=ReactomePA
- `prepareReactomeNetwork(organism="human", directed=FALSE, cores=getOption("mc.cores", 1L))` — pkg=ReactomePA
- `ridgeplot(?)` — pkg=ReactomePA
- `viewPathway(pathName, organism="human", readable=TRUE, foldChange=NULL, keyType="ENTREZID", layout="kk")` — pkg=ReactomePA

## SVP (1.5.1) — 49 symbols

### Function (47)
- `as_tbl_df(x, listn=NULL, diag=TRUE, rmrd=TRUE, flag.clust=FALSE, dist.method='euclidean', hclust.method='average')` — pkg=SVP
- `cal_lisa_f1(data, lisa.res, type='High', group.by, rm.group.nm=NULL, ...)` — pkg=SVP
- `cluster.assign(?)` — pkg=SVP
- `extract_weight_adj(?)` — pkg=SVP
- `fast_cor(x, y=NULL, combine=FALSE, method=c('pearson', 'spearman', 'bicorr'), alternative=c("two.sided", "less", "greater"), add.pvalue=FALSE, p.adjust.method='BH')` — pkg=SVP
- `fscoreDf(?)` — pkg=SVP
- `fscoreDf<-(?)` — pkg=SVP
- `fscoreDfNames(?)` — pkg=SVP
- `fscoreDfNames<-(?)` — pkg=SVP
- `fscoreDfs(x)` — pkg=SVP
- `fscoreDfs<-(?)` — pkg=SVP
- `gsvaExp(?)` — pkg=SVP
- `gsvaExp<-(?)` — pkg=SVP
- `gsvaExpNames(?)` — pkg=SVP
- `gsvaExpNames<-(?)` — pkg=SVP
- `gsvaExps(?)` — pkg=SVP
- `gsvaExps<-(?)` — pkg=SVP
- `imgData(?)` — pkg=SVP
- `imgData<-(?)` — pkg=SVP
- `LISAResult(x, type=NULL, features=NULL, ...)` — pkg=SVP
- `LISAsce(data, lisa.res, gsvaexp.name="LISA", ...)` — pkg=SVP
- `mainGsvaExpName(x)` — pkg=SVP
- `mainGsvaExpName<-(?)` — pkg=SVP
- `plot_heatmap_globalbv(globalbv, moran.t=NULL, moran.l=NULL, lisa.t=NULL, lisa.l=NULL, max.point.size=4.5, font.size=2.5, limits.size=NULL, limits.colour=NULL, dist.method="euclidean", hclust.method="average", threshold=0.05)` — pkg=SVP
- `pred.cell.signature(?)` — pkg=SVP
- `runCORR(data, features1=NULL, features2=NULL, assay.type="logcounts", method=c("spearman", "pearson", "bicorr")` — pkg=SVP
- `runDetectMarker(?)` — pkg=SVP
- `runDetectSVG(?)` — pkg=SVP
- `runENCODE(data, group.by, rm.group.nm=NULL, ...)` — pkg=SVP
- `runGLOBALBV(data, features1=NULL, features2=NULL, assay.type="logcounts", sample_id='all', method=c("lee")` — pkg=SVP
- `runKldSVG(?)` — pkg=SVP
- `runLISA(data, features, assay.type="logcounts", sample_id='all', method=c("localG", "localmoran")` — pkg=SVP
- `runLOCALBV(data, features1=NULL, features2=NULL, assay.type="logcounts", sample_id='all', bv.method=c("locallee", "localmoran")` — pkg=SVP
- `runMCA(?)` — pkg=SVP
- `runSGSA(?)` — pkg=SVP
- `runWKDE(?)` — pkg=SVP
- `spatialCoords(?)` — pkg=SVP
- `spatialCoords<-(?)` — pkg=SVP
- `spatialCoordsNames(?)` — pkg=SVP
- `spatialCoordsNames<-(?)` — pkg=SVP
- `svDf(?)` — pkg=SVP
- `svDf<-(?)` — pkg=SVP
- `svDfNames(?)` — pkg=SVP
- `svDfNames<-(?)` — pkg=SVP
- `svDfs(x)` — pkg=SVP
- `svDfs<-(?)` — pkg=SVP
- `SVPExperiment(..., gsvaExps=list())` — pkg=SVP

### S4method (2)
- `coerce(?)` — pkg=SVP
- `show(?)` — pkg=SVP

## TCMDATA (?) — 0 symbols

## aPEAR (?) — 0 symbols

## aisdk (?) — 0 symbols

## aplot (?) — 0 symbols

## clusterprofiler (4.21.2) — 155 symbols

### Function (56)
- `add_go_level(x)` — pkg=clusterProfiler
- `append_kegg_category(x)` — pkg=clusterProfiler
- `bitr(geneID, fromType, toType, OrgDb, drop=TRUE)` — pkg=clusterProfiler
- `bitr_kegg(geneID, fromType, toType, organism, drop=TRUE)` — pkg=clusterProfiler
- `browseKEGG(x, pathID)` — pkg=clusterProfiler
- `compareCluster(geneClusters, fun="enrichGO", data='', source_from=NULL, ...)` — pkg=clusterProfiler
- `download_KEGG(species, keggType="KEGG", keyType="kegg")` — pkg=clusterProfiler
- `dropGO(x, level=NULL, term=NULL)` — pkg=clusterProfiler
- `enrichDAVID(gene, idType="ENTREZ_GENE_ID", universe, minGSSize=10, maxGSSize=500, annotation="GOTERM_BP_FAT", pvalueCutoff=0.05, pAdjustMethod="BH", qvalueCutoff=0.2, species=NA, david.user)` — pkg=clusterProfiler
- `enricher(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, gson=NULL, TERM2GENE, TERM2NAME=NA)` — pkg=clusterProfiler
- `enrichGO(gene, OrgDb, keyType="ENTREZID", ont="MF", pvalueCutoff=0.05, pAdjustMethod="BH", universe, qvalueCutoff=0.2, minGSSize=10, maxGSSize=500, readable=FALSE, pool=FALSE, evidence=NULL)` — pkg=clusterProfiler
- `enrichKEGG(gene, organism="hsa", keyType="kegg", pvalueCutoff=0.05, pAdjustMethod="BH", universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, use_internal_data=FALSE)` — pkg=clusterProfiler
- `enrichMKEGG(gene, organism='hsa', keyType='kegg', pvalueCutoff=0.05, pAdjustMethod='BH', universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)` — pkg=clusterProfiler
- `enrichPC(gene, ...)` — pkg=clusterProfiler
- `enrichWP(gene, organism, ...)` — pkg=clusterProfiler
- `get_ppi(x, ID=1, taxID="auto", required_score=NULL, network_type="functional", add_nodes=0, show_query_node_labels=0, output='igraph')` — pkg=clusterProfiler
- `get_ppi_network(taxID=9606, version="12.0", score_threshold=400, output="data.frame")` — pkg=clusterProfiler
- `get_wp_organisms(?)` — pkg=clusterProfiler
- `getPPI(x, ID=1, taxID="auto", required_score=NULL, network_type="functional", add_nodes=0, show_query_node_labels=0, output='igraph')` — pkg=clusterProfiler
- `getTaxID(species)` — pkg=clusterProfiler
- `getTaxInfo(species, source="stringdb")` — pkg=clusterProfiler
- `Gff2GeneTable(gffFile, compress=TRUE)` — pkg=clusterProfiler
- `go2ont(goid)` — pkg=clusterProfiler
- `go2term(goid)` — pkg=clusterProfiler
- `gofilter(x, level=4)` — pkg=clusterProfiler
- `groupGO(gene, OrgDb, keyType="ENTREZID", ont="CC", level=2, readable=FALSE)` — pkg=clusterProfiler
- `GSEA(geneList, exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", gson=NULL, TERM2GENE, TERM2NAME=NA, verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)` — pkg=clusterProfiler
- `gseGO(geneList, ont="BP", OrgDb, keyType="ENTREZID", exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)` — pkg=clusterProfiler
- `gseKEGG(geneList, organism='hsa', keyType='kegg', exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, use_internal_data=FALSE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)` — pkg=clusterProfiler
- `gseMKEGG(geneList, organism='hsa', keyType='kegg', exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, nPerm=1000, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=1e5, pvalThreshold=0.1, seed=FALSE, ...)` — pkg=clusterProfiler
- `gsePC(geneList, eps=1e-10, ...)` — pkg=clusterProfiler
- `gseWP(geneList, organism, eps=1e-10, ...)` — pkg=clusterProfiler
- `gson_GO(OrgDb, keytype='ENTREZID', ont="BP")` — pkg=clusterProfiler
- `gson_GO_local(data, ont=c("ALL", "BP", "CC", "MF"), species=NULL, ...)` — pkg=clusterProfiler
- `gson_KEGG(species, KEGG_Type="KEGG", keyType="kegg")` — pkg=clusterProfiler
- `gson_KEGG_mapper(file, format=c("BLAST","Ghost","Kofam"), type=c("pathway","module"), species=NULL, ...)` — pkg=clusterProfiler
- `gson_KO(?)` — pkg=clusterProfiler
- `gson_WP(organism)` — pkg=clusterProfiler
- `idType(OrgDb="org.Hs.eg.db")` — pkg=clusterProfiler
- `interpret(x, context=NULL, n_pathways=20, model=NULL, task="interpretation", prior=NULL, add_ppi=FALSE, gene_fold_change=NULL, max_tokens=8192, temperature=0.3, verbose=FALSE)` — pkg=clusterProfiler
- `interpret_agent(x, context=NULL, n_pathways=50, model=NULL, add_ppi=FALSE, gene_fold_change=NULL, max_tokens=8192, temperature=0.3, verbose=FALSE)` — pkg=clusterProfiler
- `interpret_hierarchical(x_minor, x_major, mapping, model=NULL, task="cell_type", max_tokens=8192, temperature=0.3)` — pkg=clusterProfiler
- `ko2name(ko)` — pkg=clusterProfiler
- `merge_result(enrichResultList)` — pkg=clusterProfiler
- `mnseGO(seed_list, networks, couplings, ont="BP", OrgDb, keyType="ENTREZID", mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)` — pkg=clusterProfiler
- `mnseKEGG(seed_list, networks, couplings, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, use_internal_data=FALSE, ...)` — pkg=clusterProfiler
- `mnseMKEGG(seed_list, networks, couplings, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)` — pkg=clusterProfiler
- `mnseWP(seed_list, networks, couplings, organism, mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)` — pkg=clusterProfiler
- `nseGO(geneList, network, ont="BP", OrgDb, keyType="ENTREZID", mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)` — pkg=clusterProfiler
- `nseKEGG(geneList, network, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, use_internal_data=FALSE, ...)` — pkg=clusterProfiler
- `nseMKEGG(geneList, network, organism="hsa", keyType="kegg", mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)` — pkg=clusterProfiler
- `nseWP(geneList, network, organism, mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)` — pkg=clusterProfiler
- `plotGOgraph(x, firstSigNodes=10, useInfo="all", sigForAll=TRUE, useFullNames=TRUE, ...)` — pkg=clusterProfiler
- `read.gmt.pc(gmtfile, output="data.frame")` — pkg=clusterProfiler
- `search_kegg_organism(str, by="scientific_name", ignore.case=FALSE, use_internal_data=TRUE)` — pkg=clusterProfiler
- `uniprot_get(taxID)` — pkg=clusterProfiler

### Generic (4)
- `as.data.frame(x, ...)` — pkg=clusterProfiler
- `dim(x)` — pkg=clusterProfiler
- `plot(x, layout="nicely", ...)` — pkg=clusterProfiler
- `print(x, ...)` — pkg=clusterProfiler

### S4method (1)
- `simplify(?)` — pkg=clusterProfiler

### Reexport (94)
- `%<>%(lhs, rhs)` — pkg=magrittr
- `%>%(lhs, rhs)` — pkg=magrittr
- `%||%(lhs, rhs)` — pkg=rlang
- `.data(?)` — pkg=rlang
- `aes(x, y)` — pkg=ggplot2
- `Agent(description, name, model)` — pkg=aisdk
- `aggregate_enrichment(?)` — pkg=enrichit
- `aggregate_omics(?)` — pkg=enrichit
- `arrange(.data, ...)` — pkg=dplyr
- `bayes_enrich(?)` — pkg=enrichit
- `bayes_summary(?)` — pkg=enrichit
- `browseURL(?)` — pkg=utils
- `buildGOmap(gostats)` — pkg=GOSemSim
- `ChatSession(agent)` — pkg=aisdk
- `check_installed(?)` — pkg=rlang
- `citation(?)` — pkg=utils
- `cnetplot(x, layout, showCategory, color_category, size_category, color_item, size_item, color_edge, size_edge, categorySizeBy, node_label, node_label_size, foldChange, fc_threshold, hilight, hilight_alpha, categorySize, colorEdge, circular, pie, split, includeAll)` — pkg=enrichplot
- `dlply(?)` — pkg=plyr
- `dotplot(object, x, color, showCategory, size, split, font.size, title, label_format, orderBy, decreasing, xlim, ylim)` — pkg=enrichplot
- `download_yulab_file(url, destfile)` — pkg=yulab.utils
- `emapplot(x, showCategory, color, layout, cex_category, cex_line, min_edge, group_category)` — pkg=enrichplot
- `filter(.data, ..., .preserve=FALSE)` — pkg=dplyr
- `formula(?)` — pkg=stats
- `gather(?)` — pkg=tidyr
- `geneID(x)` — pkg=enrichit
- `geneInCategory(x)` — pkg=enrichit
- `generate_object(session, schema)` — pkg=aisdk
- `geom_label(?)` — pkg=ggplot2
- `geom_point(?)` — pkg=ggplot2
- `get_cache(dir)` — pkg=yulab.utils
- `get_cache_item(key)` — pkg=yulab.utils
- `get_fun_from_pkg(pkg, fun)` — pkg=yulab.utils
- `get_organism(db)` — pkg=GOSemSim
- `ggplot(data, mapping)` — pkg=ggplot2
- `ggtitle(?)` — pkg=ggplot2
- `GOBPCHILDREN(?)` — pkg=GO.db
- `GOCCCHILDREN(?)` — pkg=GO.db
- `godata(ont, organism)` — pkg=GOSemSim
- `GOMFCHILDREN(?)` — pkg=GO.db
- `goplot(x, showCategory, color, size)` — pkg=enrichplot
- `GOTERM(?)` — pkg=GO.db
- `group_by(.data, ..., .add=FALSE, .drop=FALSE)` — pkg=dplyr
- `gseaplot(x, geneSetID, by, type, color, title)` — pkg=enrichplot
- `gsfilter(?)` — pkg=enrichit
- `gson(gsid2gene, gsid2name)` — pkg=gson
- `harmonize_ids(?)` — pkg=enrichit
- `head(x, n=6L, ...)` — pkg=utils
- `heatplot(x, showCategory, foldChange)` — pkg=enrichplot
- `installed.packages(?)` — pkg=utils
- `is(?)` — pkg=methods
- `is.installed(pkg)` — pkg=yulab.utils
- `keys(x)` — pkg=AnnotationDbi
- `keytypes(x)` — pkg=AnnotationDbi
- `ldply(?)` — pkg=plyr
- `llply(?)` — pkg=plyr
- `load_OrgDb(OrgDb)` — pkg=yulab.utils
- `mgoSim(GO1, GO2)` — pkg=GOSemSim
- `modifyList(?)` — pkg=utils
- `mutate(.data, ...)` — pkg=dplyr
- `n(?)` — pkg=dplyr
- `na.omit(?)` — pkg=stats
- `new(?)` — pkg=methods
- `Ontology(object)` — pkg=AnnotationDbi
- `packageDescription(?)` — pkg=utils
- `quos(?)` — pkg=rlang
- `qvalue(?)` — pkg=qvalue
- `read.blast2go(file)` — pkg=GOSemSim
- `read.gaf(file)` — pkg=GOSemSim
- `read.gmt(gmtfile, output="data.frame")` — pkg=gson
- `read.gmt.wp(gmtfile)` — pkg=gson
- `read.table(?)` — pkg=utils
- `rename(.data, ...)` — pkg=dplyr
- `ridgeplot(x, showCategory, label_format)` — pkg=enrichplot
- `scale_color_manual(values)` — pkg=ggplot2
- `select(.data, ...)` — pkg=dplyr
- `select_features_for_ora(?)` — pkg=enrichit
- `separate(?)` — pkg=tidyr
- `setNames(?)` — pkg=stats
- `setReadable(?)` — pkg=enrichit
- `slice(.data, ..., .preserve=FALSE)` — pkg=dplyr
- `stack(?)` — pkg=utils
- `str(?)` — pkg=utils
- `summarise(.data, ...)` — pkg=dplyr
- `sym(?)` — pkg=rlang
- `tail(x, n=6L, ...)` — pkg=utils
- `theme_void(?)` — pkg=ggplot2
- `toTable(x)` — pkg=AnnotationDbi
- `user_dir(appname)` — pkg=yulab.utils
- `yread(file)` — pkg=yulab.utils
- `yread_tsv(file)` — pkg=yulab.utils
- `z_array(items)` — pkg=aisdk
- `z_enum(values)` — pkg=aisdk
- `z_object(fields)` — pkg=aisdk
- `z_string(?)` — pkg=aisdk

## createKEGGdb (?) — 0 symbols

## enrichit (0.2.5) — 36 symbols

### Function (30)
- `aggregate_enrichment(res_list, method=c("brown", "fisher", "stouffer"), ...)` — pkg=enrichit
- `aggregate_omics(x, method=c("fisher", "stouffer", "brown", "mea..., input=c("pvalue", "signed_score"), feature_type="gene", conflict_policy=c("keep_all", "strict", "penalty"), ...)` — pkg=enrichit
- `as_enrichResult(x, geneSets=NULL, gene=NULL, universe=NULL, ontology="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", pAdjustMethod="BH", ...)` — pkg=enrichit
- `as_gseaResult(x, geneList, geneSets=NULL, setType="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", exponent=1, scoreType="std", pAdjustMethod="BH", ...)` — pkg=enrichit
- `bayes_enrich(x, candidate=c("top", "significant", "all"), n_terms=200, by="p.adjust", prior=0.1, false_positive=0.01, false_negative=0.1, n_iter=5000, burnin=1000, thin=1, posterior_cutoff=0.5, seed=NULL, verbose=FALSE)` — pkg=enrichit
- `bayes_summary(x, active=FALSE, n=Inf)` — pkg=enrichit
- `classify_omics_pattern(merged_res, single_res, p_cutoff=0.05, by="p.adjust")` — pkg=enrichit
- `collapse_multilayer_scores(x, collapse=c("weighted_mean", "sum", "mean", "ma..., layer_weights=NULL, output_space=c("union", "gene"), mapping=NULL, target_layer=NULL)` — pkg=enrichit
- `EXTID2NAME(OrgDb, geneID, keytype, toType="SYMBOL")` — pkg=enrichit
- `extract_mnsea_subnetwork(res, pathway_id=NULL, include_couplings=TRUE, include_isolated=TRUE)` — pkg=enrichit
- `geneID(x)` — pkg=enrichit
- `geneInCategory(x)` — pkg=enrichit
- `get_mnsea_contribution(res, pathway_id=NULL, level=c("pathway", "feature"))` — pkg=enrichit
- `get_omics_contribution(res, agg, pathway_id=NULL)` — pkg=enrichit
- `gsea(geneList, gene_sets, weight=NULL, minGSSize=10, maxGSSize=500, nPerm=1000, exponent=1.0, method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, eps=1e-10, sampleSize=101, seed=FALSE, nPermSimple=1000, scoreType="std", verbose=TRUE)` — pkg=enrichit
- `gsea_gson(geneList, gson, weight=NULL, nPerm=1000, exponent=1.0, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, seed=FALSE, verbose=TRUE, ...)` — pkg=enrichit
- `gseaScores(geneList, geneSet, exponent=1, fortify=FALSE)` — pkg=enrichit
- `gsfilter(x, by="GSSize", min=NA, max=NA)` — pkg=enrichit
- `harmonize_ids(x, mapping, from="protein", to="gene", collapse=c("max_abs", "mean", "min_p"))` — pkg=enrichit
- `mnsea(seed_list, networks, couplings, gene_sets, mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)` — pkg=enrichit
- `mnsea_gson(seed_list, networks, couplings, gson, mode=c("evidence", "signed"), layer_weights=NULL, collapse=c("weighted_mean", "sum", "mean", "ma..., target_layer=NULL, output_space=c("union", "gene"), p=0.5, interlayer_strength=1, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, verbose=TRUE, ...)` — pkg=enrichit
- `nsea(geneList, network, gene_sets, mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, significance=c("whole_pipeline", "internal"), nPerm=1000, seed=NULL, exponent=1, verbose=TRUE, ...)` — pkg=enrichit
- `nsea_gson(geneList, network, gson, mode=c("evidence", "signed"), p=0.5, specific_weight=FALSE, minGSSize=10, maxGSSize=500, threshold=1e-9, maxIter=100, significance=c("whole_pipeline", "internal"), nPerm=1000, seed=NULL, exponent=1, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, ...)` — pkg=enrichit
- `ora(gene, gene_sets, universe, weight=NULL)` — pkg=enrichit
- `ora_gson(gene, pvalueCutoff, pAdjustMethod="BH", universe=NULL, weight=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, gson)` — pkg=enrichit
- `prepare_multilayer_network(networks, couplings, directed=FALSE, intra_normalize="column", inter_normalize="column", interlayer_strength=1, layer_order=names(networks))` — pkg=enrichit
- `prepare_network(network, directed=FALSE, normalize="column")` — pkg=enrichit
- `propagate_multilayer(seed_list, network, mode=c("evidence", "signed"), p=0.5, threshold=1e-9, maxIter=100, layer_weights=NULL, target_layer=NULL)` — pkg=enrichit
- `select_features_for_ora(x, cutoff=0.05, by=c("pvalue", "score"), ...)` — pkg=enrichit
- `setReadable(x, OrgDb, keyType="auto", toType="SYMBOL")` — pkg=enrichit

### Generic (4)
- `as.data.frame(x, ...)` — pkg=enrichit
- `dim(x)` — pkg=enrichit
- `head(x, n=6L, ...)` — pkg=enrichit
- `tail(x, n=6L, ...)` — pkg=enrichit

### S4method (2)
- `show(?)` — pkg=enrichit
- `summary(?)` — pkg=enrichit

## enrichplot (1.99.7) — 51 symbols

### Function (45)
- `as_enrichResult(?)` — pkg=enrichplot
- `as_gseaResult(?)` — pkg=enrichplot
- `autofacet(by='row', scales="free", levels=NULL)` — pkg=enrichplot
- `cnetplot(x, layout=igraph::layout_with_kk, showCategory=5, color_category="#E5C494", size_category=1, color_item="#B3B3B3", size_item=1, color_edge="grey", size_edge=.5, categorySizeBy=~itemNum, node_label="all", node_label_size=NULL, foldChange=NULL, fc_threshold=NULL, hilight="none", hilight_alpha=.3, pathway_id=NULL, layer=NULL, include_couplings=TRUE, ...)` — pkg=enrichplot
- `color_palette(colors)` — pkg=enrichplot
- `consensusmap(x, fill_var=c("NES", "delta_NES")` — pkg=enrichplot
- `dotplot(object, x="geneRatio", color="p.adjust", showCategory=10, size=NULL, split=NULL, font.size=12, title="", orderBy="x", label_format=30, decreasing=TRUE, layer=NULL, colorBy="p.adjust", by="geneRatio", includeAll=TRUE, group=FALSE, shape=FALSE, facet=NULL, strip_width=15, ...)` — pkg=enrichplot
- `dotplot2(object, x="FoldEnrichment", vars=NULL, label="auto", ...)` — pkg=enrichplot
- `emapplot(x, layout=igraph::layout_with_kk, coords=NULL, showCategory=30, color="p.adjust", size_category=1, min_edge=.2, color_edge="grey", size_edge=.5, group=NULL, group_legend=TRUE, node_label="category", node_label_size=5, pie="equal", layer=NULL, label_format=30, clusterFunction=stats::kmeans, nWords=4, nCluster=NULL, show_category_size_legend=TRUE, edge_filter="threshold", top_k=5, target_density=.1, edge_diagnostic=FALSE, ...)` — pkg=enrichplot
- `emapplot_edge_density(pair_sim, min_edge=.2, edge_filter="threshold", top_k=5, target_density=.1, dense_threshold=.2)` — pkg=enrichplot
- `facet_grid(?)` — pkg=enrichplot
- `fortify_mnsea_contribution(x, level=c("pathway", "feature"), pathway_id=NULL, layer=NULL, ...)` — pkg=enrichplot
- `fortify_mnsea_subnetwork(x, pathway_id=NULL, layer=NULL, include_couplings=TRUE, include_isolated=FALSE, ...)` — pkg=enrichplot
- `geneID(?)` — pkg=enrichplot
- `geneInCategory(?)` — pkg=enrichplot
- `geom_cnet_label(?)` — pkg=enrichplot
- `geom_gsea_gene(genes, mapping=NULL, geom=ggplot2::geom_text, ..., geneSet=NULL)` — pkg=enrichplot
- `get_enrichplot_color(n=2)` — pkg=enrichplot
- `ggtable(d, p=NULL)` — pkg=enrichplot
- `ggtitle(?)` — pkg=enrichplot
- `goplot(x, showCategory=10, color="p.adjust", layout=igraph::layout_with_sugiyama, geom="text", ID="Description", ...)` — pkg=enrichplot
- `gseadist(x, IDs, type='density')` — pkg=enrichplot
- `gseaplot(x, geneSetID, by="all", title="", color='black', color.line="green", color.vline="#FA5860", layer=NULL, ...)` — pkg=enrichplot
- `gseaplot2(x, geneSetID, title="", color="green", base_size=11, rel_heights=c(1.5, .5, 1), subplots=1:3, pvalue_table=FALSE, pvalue_table_columns=c("NES", "p.adjust"), pvalue_table_rownames="Description", ES_geom="line", layer=NULL)` — pkg=enrichplot
- `gsearank(x, geneSetID, title="", output="plot", layer=NULL)` — pkg=enrichplot
- `gseaScores(?)` — pkg=enrichplot
- `heatplot(x, showCategory=30, showTop=NULL, symbol="rect", foldChange=NULL, pvalue=NULL, label_format=30, pathway_id=NULL, layer=NULL, value=c("score", "abs_score", "share", "con...)` — pkg=enrichplot
- `hplot(x, geneSetID, layer=NULL)` — pkg=enrichplot
- `import_enrichr(x, db=1, gene=NULL, universe=NULL, ontology="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", pAdjustMethod="BH", ...)` — pkg=enrichplot
- `import_fgsea(x, stats, geneSets=NULL, setType="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", exponent=1, scoreType="std", pAdjustMethod="BH", ...)` — pkg=enrichplot
- `import_gprofiler2(x, gene=NULL, ontology="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", pAdjustMethod="BH", ...)` — pkg=enrichplot
- `import_webgestalt(x, gene=NULL, universe=NULL, ontology="UNKNOWN", organism="UNKNOWN", keytype="UNKNOWN", pAdjustMethod="BH", ...)` — pkg=enrichplot
- `manhattanplot(x, color="p.adjust", showCategory=5, size="Count", split=NULL, font.size=12, title="", label_format=30, colorBy="p.adjust", includeAll=TRUE, facet="Cluster", strip_width=15, ...)` — pkg=enrichplot
- `mechanismflow(x, reference=NULL, flow_var=c("NES", "delta_NES", "leading_edge_s...)` — pkg=enrichplot
- `phaseplot(x, reference=NULL, selected_layer=NULL, reference_layer=NULL, x_axis=NULL, size_var=c("leading_edge_size", "leading_edge_...)` — pkg=enrichplot
- `plot_list(?)` — pkg=enrichplot
- `pmcplot(query, period, proportion=TRUE, data=NULL)` — pkg=enrichplot
- `rewireplot(x, ...)` — pkg=enrichplot
- `ridgeplot(x, showCategory=30, fill="p.adjust", core_enrichment=TRUE, label_format=30, orderBy="NES", decreasing=FALSE, stat="density_ridges", layer=NULL)` — pkg=enrichplot
- `set_enrichplot_color(colors=get_enrichplot_color(2), type="color", name=NULL, .fun=NULL, reverse=TRUE, transform='identity', ...)` — pkg=enrichplot
- `ssplot(x, showCategory=30, drfun=NULL, dr.params=list(), node_label="group", min_edge=.2, size_edge=.5, edge_filter="threshold", top_k=5, target_density=.1, edge_diagnostic=FALSE, layer=NULL, pie="equal", ...)` — pkg=enrichplot
- `theme_dose(?)` — pkg=enrichplot
- `treeplot(x, ...)` — pkg=enrichplot
- `upsetplot(x, n=10, type="boxplot", layer=NULL, value=c("score", "abs_score"), core_enrichment=FALSE, ...)` — pkg=enrichplot
- `volplot(x, color="zScore", xintercept=1, yintercept=2, showCategory=5, label_format=30, font.size=12, size=5)` — pkg=enrichplot

### Generic (5)
- `as.data.frame(x, ...)` — pkg=enrichplot
- `barplot(height, x="Count", color="p.adjust", showCategory=8, font.size=12, title="", label_format=30, by="geneRatio", includeAll=TRUE, ...)` — pkg=enrichplot
- `fortify(model, data, showCategory=5, by="Count", order=FALSE, drop=FALSE, split=NULL, includeAll=TRUE, level=c("result", "pathway"), layer=NULL, ...)` — pkg=enrichplot
- `ggplot_add(object, plot, ...)` — pkg=enrichplot
- `gsInfo(object, geneSetID, layer=NULL, ...)` — pkg=enrichplot

### S4method (1)
- `pairwise_termsim(?)` — pkg=enrichplot

## epiSeeker (1.1.2) — 49 symbols

### Function (41)
- `.(..., .env=parent.frame())` — pkg=epiSeeker
- `annotateSeq(peak, tssRegion=c(-3000, 3000), TxDb=NULL, level="transcript", assignGenomicAnnotation=TRUE, genomicAnnotationPriority=c("Promoter", "5UTR", "3UTR", "Exon",..., annoDb=NULL, addFlankGeneInfo=FALSE, flankDistance=5000, sameStrand=FALSE, ignoreOverlap=FALSE, ignoreUpstream=FALSE, ignoreDownstream=FALSE, overlap="TSS", verbose=TRUE, columns=c("ENTREZID", "ENSEMBL", "SYMBOL", "G...)` — pkg=epiSeeker
- `as.GRanges(x)` — pkg=epiSeeker
- `bmData(value1=NULL, value2=NULL, pos=NULL, chr=NULL, gr=NULL, sampleNames=NULL, valueNames=NULL, ...)` — pkg=epiSeeker
- `combine_csAnno(x, ...)` — pkg=epiSeeker
- `downloadGEObedFiles(genome, destDir=getwd())` — pkg=epiSeeker
- `downloadGSMbedFiles(GSM, destDir=getwd())` — pkg=epiSeeker
- `dropAnno(csAnno, distanceToTSS_cutoff=10000)` — pkg=epiSeeker
- `enrichAnnoOverlap(queryPeak, targetPeak, TxDb=NULL, pAdjustMethod="BH", chainFile=NULL, distanceToTSS_cutoff=NULL)` — pkg=epiSeeker
- `enrichPeakOverlap(queryPeak, targetPeak, TxDb=NULL, pAdjustMethod="BH", nShuffle=1000, chainFile=NULL, pool=TRUE, mc.cores=detectCores() - 1, verbose=TRUE)` — pkg=epiSeeker
- `getAnnoStat(x)` — pkg=epiSeeker
- `getBioRegion(TxDb=NULL, upstream=1000, downstream=1000, by="gene", type="start_site")` — pkg=epiSeeker
- `getBmMatrix(region, input, BSgenome, cover_depth=TRUE, base=NULL, motif=NULL, position_bias=NULL)` — pkg=epiSeeker
- `getGEOgenomeVersion(?)` — pkg=epiSeeker
- `getGEOInfo(genome, simplify=TRUE)` — pkg=epiSeeker
- `getGEOspecies(?)` — pkg=epiSeeker
- `getMotifMatrix(region, pwm, ref_obj, by="name")` — pkg=epiSeeker
- `getPromoters(TxDb=NULL, upstream=1000, downstream=1000, by="gene")` — pkg=epiSeeker
- `getSampleFiles(?)` — pkg=epiSeeker
- `getTagMatrix(peak, upstream=0, downstream=0, windows=NULL, type=NULL, by=NULL, TxDb=NULL, weightCol=NULL, nbin=NULL, verbose=TRUE, ignore_strand=FALSE)` — pkg=epiSeeker
- `grange2mt(gr_list, weightCol=NULL)` — pkg=epiSeeker
- `makeBmDataFromData(data, sampleNames=NULL)` — pkg=epiSeeker
- `makeBmDataFromFiles(name, sampleNames=NULL, variablesNames=NULL)` — pkg=epiSeeker
- `parse_peak(peak_str)` — pkg=epiSeeker
- `plotAnnoBar(x, xlab="", ylab="Percentage(%)` — pkg=epiSeeker
- `plotAnnoPie(x, ndigit=2, cex=0.8, col=NA, legend.position="rightside", pie3D=FALSE, radius=0.8, ...)` — pkg=epiSeeker
- `plotAnnoPie.csAnno(x, ndigit=2, cex=0.8, col=NA, legend.position="rightside", pie3D=FALSE, radius=0.8, ...)` — pkg=epiSeeker
- `plotBmProf(df, motif_color=NULL, title=NULL, xlim=NULL, interactive=FALSE, width_svg=10, height_svg=6, highlight=NULL, highlight_color="#c6c3c3", highlight_alpha=0.2, xlab="Genomic Region(5'->3')", ylab=NULL, second_ylab=NULL, switch_y_value=TRUE, legend_lab_motif=NULL, legend_lab_value2=NULL, strip_placement="outside", angle_of_facet_label=360, alpha=0.6, y_ticks_length=0.25, x_ticks_length=0.25, auto_x_axis=TRUE, strip_border=FALSE, facet_label_text_size=10, axis_title_text_size=17, title_text_size=20, right_y_axis_text_size=10, left_y_axis_text_size=10, x_axis_text_size=10, depth_heatmap=TRUE, nrow=NULL, ncol=NULL, panel_spacing=1, legend_box_spacing=3, legend_position="right")` — pkg=epiSeeker
- `plotCov(peak, weightCol=NULL, facet_level=NULL, highlight=NULL, highlight_color="#c6c3c3", highlight_alpha=0.2, xlab="Chromosome Size (bp)", ylab="", interactive=FALSE, width_svg=10, height_svg=6, title="ChIP Peaks over Chromosomes", x_text_size=10, y_text_size=10, facet_label_text_size=10, chrs=NULL, xlim=NULL, facet_var=NULL, facet_scales="free", lower=1, fill_color="black", add_cluster_tree=FALSE, cluster_dist_method="euclidean", cluster_hclust_methond="complete", legend_position=NULL, add_coaccess=FALSE, curvature=0.3, coaccess_top_n=NULL, coaccess_cor_threshold=NULL, design=NULL, coaccess_legend_pos=c(0.9, 0.5), coaccess_legend_text_size=10, coaccess_legend_title_size=12)` — pkg=epiSeeker
- `plotDistToTSS(x, distanceColumn="distanceToTSS", xlab="", ylab="Binding sites (%)` — pkg=epiSeeker
- `plotGeneTrack(txdb, chr, start_pos, end_pos, xlab="", ylab="", x_text_size=10, y_text_size=10, select_gene="all", palette=NULL, fromType="ENTREZID", highlight=NULL, highlight_color="#c6c3c3", highlight_alpha=0.2, OrgDb=NULL, show_legend=FALSE, auto_x_axis=TRUE)` — pkg=epiSeeker
- `plotMotifProf(df, legend_lab="motif", y_lab="motif score", x_lab=NULL, interactive=FALSE, width_svg=10, height_svg=6)` — pkg=epiSeeker
- `plotPeakHeatmap(tagMatrix, plot_prof=TRUE, xlab="", ylab="", palette=NULL, title=NULL, facet_label_text_size=12, nrow=NULL, ncol=NULL, conf=NULL, statistic_method="mean", missingDataAsZero=TRUE, facet="none", free_y=TRUE, height_proportion=4, ...)` — pkg=epiSeeker
- `plotPeakProf(tagMatrix, xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", conf=NULL, title="", facet="none", free_y=TRUE, statistic_method="mean", missingDataAsZero=TRUE, ...)` — pkg=epiSeeker
- `readPeakFile(peakfile, as="GRanges", ...)` — pkg=epiSeeker
- `rel(?)` — pkg=epiSeeker
- `seq2gene(seq, tssRegion, flankDistance, TxDb, sameStrand=FALSE)` — pkg=epiSeeker
- `shuffle(peak.gr, TxDb)` — pkg=epiSeeker
- `vennpie(x, r=0.2, cex=1.2, col=NULL)` — pkg=epiSeeker
- `vennplot(Sets, ...)` — pkg=epiSeeker
- `vennplot.peakfile(files, labels=NULL)` — pkg=epiSeeker

### Generic (6)
- `arrange(.data, .by_group=FALSE, ...)` — pkg=epiSeeker
- `as.data.frame(x, row.names=NULL, optional=FALSE, ...)` — pkg=epiSeeker
- `filter(.data, .by=NULL, .preserve=FALSE, ...)` — pkg=epiSeeker
- `mutate(.data, .by=NULL, .keep=c("all", "used", "unused", "none"), .before=NULL, .after=NULL, ...)` — pkg=epiSeeker
- `rename(.data, ...)` — pkg=epiSeeker
- `subset(x, subset, ...)` — pkg=epiSeeker

### S4method (2)
- `show(?)` — pkg=epiSeeker
- `upsetplot(?)` — pkg=epiSeeker

## ggbreak (?) — 0 symbols

## ggimage (?) — 0 symbols

## ggmsa (1.19.2) — 34 symbols

### Function (30)
- `adjust_ally(tree, node, sub=FALSE, seq_colname="mol_seq")` — pkg=ggmsa
- `assign_dms(x, dms)` — pkg=ggmsa
- `available_colors(?)` — pkg=ggmsa
- `available_fonts(?)` — pkg=ggmsa
- `available_msa(?)` — pkg=ggmsa
- `extract_seq(tree_adjust, seq_colname="mol_seq")` — pkg=ggmsa
- `facet_msa(field)` — pkg=ggmsa
- `geom_GC(show.legend=FALSE)` — pkg=ggmsa
- `geom_helix(helix_data, color_by="length", overlap=FALSE, ...)` — pkg=ggmsa
- `geom_msa(data, font="helvetical", mapping=NULL, color="Chemistry_AA", custom_color=NULL, char_width=0.9, none_bg=FALSE, by_conservation=FALSE, position_highlight=NULL, seq_name=NULL, border=NULL, consensus_views=FALSE, use_dot=FALSE, disagreement=TRUE, ignore_gaps=FALSE, ref=NULL, position="identity", show.legend=FALSE, dms=FALSE, position_color=FALSE, ...)` — pkg=ggmsa
- `geom_msaBar(?)` — pkg=ggmsa
- `geom_seed(seed, star=FALSE)` — pkg=ggmsa
- `geom_seqlogo(font="DroidSansMono", color="Chemistry_AA", adaptive=TRUE, top=TRUE, custom_color=NULL, show.legend=FALSE, ...)` — pkg=ggmsa
- `gghelix(helix_data, color_by="length", overlap=FALSE)` — pkg=ggmsa
- `ggmaf(data, ref, block_start=NULL, block_end=NULL, facet_field=NULL, heights=c(0.4,0.6), facet_heights=NULL)` — pkg=ggmsa
- `ggmsa(msa, start=NULL, end=NULL, font="helvetical", color="Chemistry_AA", custom_color=NULL, char_width=0.9, none_bg=FALSE, by_conservation=FALSE, position_highlight=NULL, seq_name=NULL, border=NULL, consensus_views=FALSE, use_dot=FALSE, disagreement=TRUE, ignore_gaps=FALSE, ref=NULL, show.legend=FALSE)` — pkg=ggmsa
- `ggSeqBundle(msa, line_width=0.3, line_thickness=0.3, line_high=0, spline_shape=0.3, size=0.5, alpha=0.2, bundle_color=c("#2ba0f5","#424242"), lev_molecule=c("-", "A", "V", "L", "I", "P", "F", ...)` — pkg=ggmsa
- `merge_seq(previous_seq, gap, subsequent_seq, adjust_name=TRUE)` — pkg=ggmsa
- `read_maf(multiple_alignment_format)` — pkg=ggmsa
- `readSSfile(file, type=NULL)` — pkg=ggmsa
- `reset_pos(seq_df)` — pkg=ggmsa
- `seqdiff(fasta, reference=1)` — pkg=ggmsa
- `seqlogo(msa, start=NULL, end=NULL, font="DroidSansMono", color="Chemistry_AA", adaptive=FALSE, top=FALSE, custom_color=NULL)` — pkg=ggmsa
- `simplify_hdata(hdata, sim_msa)` — pkg=ggmsa
- `simplot(file, query, window=200, step=20, group=FALSE, id, sep, sd=FALSE, smooth=FALSE, smooth_params=list(method = "loess", se = FALSE))` — pkg=ggmsa
- `theme_msa(?)` — pkg=ggmsa
- `tidy_hdata(gap, inter, previous_seq, subsequent_seq)` — pkg=ggmsa
- `tidy_maf_df(maf_df, ref)` — pkg=ggmsa
- `tidy_msa(msa, start=NULL, end=NULL)` — pkg=ggmsa
- `treeMSA_plot(p_tree, tidymsa_df, ancestral_node="none", sub=FALSE, panel="MSA", font=NULL, color="Chemistry_AA", seq_colname=NULL, ...)` — pkg=ggmsa

### Generic (2)
- `diff(x, ...)` — pkg=ggmsa
- `ggplot_add(object, plot, ...)` — pkg=ggmsa

### S4method (2)
- `plot(?)` — pkg=ggmsa
- `show(?)` — pkg=ggmsa

## ggsc (1.11.2) — 24 symbols

### Function (23)
- `%<+%(?)` — pkg=ggsc
- `aes(?)` — pkg=ggsc
- `draw_key_bgpoint(data, params, size)` — pkg=ggsc
- `geom_bgpoint(mapping=NULL, data=NULL, stat="identity", position="identity", ..., na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, gap_colour='white', gap_alpha=1, bg_line_width=.3, gap_line_width=.1, pointsize=NULL)` — pkg=ggsc
- `geom_scattermore2(mapping=NULL, data=NULL, stat="identity", position="identity", ..., na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, interpolate=FALSE, pointsize=0, pixels=c(512, 512), gap_colour='white', gap_alpha=1, bg_line_width=.3, gap_line_width=.1)` — pkg=ggsc
- `plot_lisa_feature(spe, lisa.res, features=NULL, assay.type='logcounts', geom=geom_bgpoint, pointsize=2, hlpointsize=1.8, clustertype='High', hlcolor=c('black'), gap_line_width=.1, bg_line_width=.3, facet_name=NULL, reduction=NULL, image.plot=FALSE, label_wrap_width=30, ncol=6, ...)` — pkg=ggsc
- `sc_dim(object, dims=c(1,2)` — pkg=ggsc
- `sc_dim_count(sc_dim_plot)` — pkg=ggsc
- `sc_dim_geom_ellipse(geom=stat_ellipse, mapping=NULL, level=0.95, ...)` — pkg=ggsc
- `sc_dim_geom_feature(object, features, dims=c(1,2), ncol=3, ..., .fun=function(.data) dplyr::filter(.data, ...)` — pkg=ggsc
- `sc_dim_geom_label(geom=ggplot2::geom_text, mapping=NULL, ...)` — pkg=ggsc
- `sc_dim_geom_sub(mapping=NULL, subset, .column="ident", ...)` — pkg=ggsc
- `sc_dim_sub(subset, .column="ident")` — pkg=ggsc
- `sc_dot(object, features, group.by=NULL, split.by=NULL, cols=c("lightgrey", "blue")` — pkg=ggsc
- `sc_feature(object, features, dims=c(1, 2)` — pkg=ggsc
- `sc_geom_annot(data=NULL, mapping=NULL, pointsize=2, pixels=c(512, 512), gap_colour="white", gap_alpha=1, bg_line_width=0.3, gap_line_width=0.1, show.legend=NA, na.rm=FALSE, ...)` — pkg=ggsc
- `sc_geom_point(mapping=NULL, ...)` — pkg=ggsc
- `sc_spatial(object, features=NULL, slot="data", plot.pie=FALSE, pie.radius.scale=.3, image.plot=TRUE, image.first.operation='rotate', image.rotate.degree=NULL, image.mirror.axis='v', remove.point=FALSE, mapping=NULL, ncol=6, density=FALSE, grid.n=100, joint=FALSE, joint.fun=prod, common.legend=TRUE, pointsize=5, geom=sc_geom_point, reduction=NULL, dims=NULL, ...)` — pkg=ggsc
- `sc_violin(object, features, cells=NULL, slot="data", .fun=NULL, mapping=NULL, ncol=3, geom=geom_violin, ...)` — pkg=ggsc
- `scale_bg_color_manual(..., values, aesthetics="bg_colour", breaks=waiver(), na.value="grey50")` — pkg=ggsc
- `scale_bg_colour_discrete(...)` — pkg=ggsc
- `scale_bg_colour_manual(..., values, aesthetics="bg_colour", breaks=waiver(), na.value="grey50")` — pkg=ggsc
- `theme(?)` — pkg=ggsc

### Generic (1)
- `ggplot_add(object, plot, object_name, ...)` — pkg=ggsc

## ggtangle (?) — 0 symbols

## ggtree (4.3.1) — 139 symbols

### Function (137)
- `%+>%(?)` — pkg=ggtree
- `%<%(?)` — pkg=ggtree
- `%<+%(?)` — pkg=ggtree
- `%>%(?)` — pkg=ggtree
- `add_colorbar(p, color, x=NULL, ymin=NULL, ymax=NULL, font.size=4)` — pkg=ggtree
- `aes(?)` — pkg=ggtree
- `arrow(?)` — pkg=ggtree
- `as.polytomy(tree, feature, fun)` — pkg=ggtree
- `as_tanglegram(x, y=NULL, assoc=NULL, layout="rectangular", ladderize=TRUE, preserve_layers=TRUE, ...)` — pkg=ggtree
- `as_tanglegram.cophylo(x, ..., layout="rectangular", ladderize=TRUE, preserve_layers=TRUE)` — pkg=ggtree
- `as_tanglegram.default(x, y=NULL, assoc=NULL, layout="rectangular", ladderize=TRUE, preserve_layers=TRUE, ...)` — pkg=ggtree
- `as_tanglegram.tanglegram(x, ...)` — pkg=ggtree
- `collapse(x=NULL, node, mode="none", clade_name=NULL, height=NULL, ...)` — pkg=ggtree
- `Date2decimal(x)` — pkg=ggtree
- `decimal2Date(x)` — pkg=ggtree
- `expand(tree_view=NULL, node)` — pkg=ggtree
- `facet_data(tree_view, panel)` — pkg=ggtree
- `facet_labeller(p, label)` — pkg=ggtree
- `facet_plot(p, mapping=NULL, data, geom, panel, ...)` — pkg=ggtree
- `facet_widths(p, widths)` — pkg=ggtree
- `flip(tree_view=NULL, node1, node2)` — pkg=ggtree
- `fortify(model, data, layout="rectangular", ladderize=TRUE, right=FALSE, branch.length="branch.length", mrsd=NULL, as.Date=FALSE, yscale="none", root.position=0, hang=.1, gap=0.08, mirror=TRUE, optimize=isTRUE(model$params$optimize), optimize_side=model$params$optimize_side %||% "right", ...)` — pkg=ggtree
- `geom_aline(mapping=NULL, linetype="dotted", linewidth=1, ...)` — pkg=ggtree
- `geom_balance(node, fill="steelblue", color='white', alpha=.5, extend=0, extendto=NULL)` — pkg=ggtree
- `geom_cladelab(node=NULL, label=NULL, data=NULL, mapping=NULL, geom="text", parse=FALSE, ...)` — pkg=ggtree
- `geom_cladelabel(node, label, offset=0, offset.text=0, extend=0, align=FALSE, barsize=0.5, fontsize=3.88, angle=0, geom="text", hjust=0, color=NULL, fill=NA, family="sans", parse=FALSE, horizontal=TRUE, ...)` — pkg=ggtree
- `geom_cladelabel2(node, label, offset=0, offset.text=0, offset.bar=0, align=FALSE, barsize=0.5, fontsize=3.88, hjust=0, geom="text", color=NULL, family="sans", parse=FALSE, horizontal=TRUE, ...)` — pkg=ggtree
- `geom_facet(mapping=NULL, data, geom, panel, ...)` — pkg=ggtree
- `geom_highlight(data=NULL, mapping=NULL, node=NULL, type="auto", to.bottom=FALSE, ...)` — pkg=ggtree
- `geom_hilight(data=NULL, mapping=NULL, node=NULL, type="auto", to.bottom=FALSE, ...)` — pkg=ggtree
- `geom_inset(insets, width=.1, height=.1, hjust=0, vjust=0, x="node", reverse_x=FALSE, reverse_y=FALSE)` — pkg=ggtree
- `geom_label(?)` — pkg=ggtree
- `geom_label2(mapping=NULL, data=NULL, ..., stat="identity", position="identity", family="sans", parse=FALSE, nudge_x=0, nudge_y=0, label.padding=unit(0.25, "lines"), label.r=unit(0.15, "lines"), label.size=0.25, na.rm=TRUE, show.legend=NA, inherit.aes=TRUE)` — pkg=ggtree
- `geom_label2_interactive(...)` — pkg=ggtree
- `geom_motif(mapping, data, on, label, align='centre', ...)` — pkg=ggtree
- `geom_nodelab(mapping=NULL, nudge_x=0, nudge_y=0, geom="text", hjust=0.5, node="internal", ...)` — pkg=ggtree
- `geom_nodelab2(mapping=NULL, nudge_x=0, nudge_y=0, geom="text", hjust=0.5, ...)` — pkg=ggtree
- `geom_nodepoint(mapping=NULL, data=NULL, position="identity", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, ...)` — pkg=ggtree
- `geom_point(?)` — pkg=ggtree
- `geom_point2(mapping=NULL, data=NULL, stat="identity", position="identity", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, ...)` — pkg=ggtree
- `geom_point2_interactive(...)` — pkg=ggtree
- `geom_range(range, center="auto", ...)` — pkg=ggtree
- `geom_rootedge(rootedge=NULL, data=NULL, ...)` — pkg=ggtree
- `geom_rootpoint(mapping=NULL, data=NULL, position="identity", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, ...)` — pkg=ggtree
- `geom_segment2(mapping=NULL, data=NULL, stat="identity", position="identity", lineend="butt", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, nudge_x=0, arrow=NULL, arrow.fill=NULL, ...)` — pkg=ggtree
- `geom_segment2_interactive(...)` — pkg=ggtree
- `geom_strip(taxa1, taxa2, label, offset=0, offset.text=0, align=TRUE, barsize=0.5, extend=0, fontsize=3.88, angle=0, geom="text", hjust=0, color='black', fill=NA, family="sans", parse=FALSE, ...)` — pkg=ggtree
- `geom_striplab(taxa1=NULL, taxa2=NULL, label=NULL, data=NULL, mapping=NULL, geom="text", parse=FALSE, ...)` — pkg=ggtree
- `geom_tanglelink(data=NULL, mapping=NULL, left=NULL, right=NULL, geom=c("curve", "segment"), curvature=0.15, ...)` — pkg=ggtree
- `geom_taxalink(data=NULL, mapping=NULL, taxa1=NULL, taxa2=NULL, offset=NULL, outward="auto", ...)` — pkg=ggtree
- `geom_text(?)` — pkg=ggtree
- `geom_text2(mapping=NULL, data=NULL, ..., stat="identity", position="identity", family="sans", parse=FALSE, na.rm=TRUE, show.legend=NA, inherit.aes=TRUE, nudge_x=0, nudge_y=0, check_overlap=FALSE)` — pkg=ggtree
- `geom_text2_interactive(...)` — pkg=ggtree
- `geom_tiplab(mapping=NULL, hjust=0, align=FALSE, linetype="dotted", linesize=0.5, geom="text", offset=0, as_ylab=FALSE, ...)` — pkg=ggtree
- `geom_tiplab2(mapping=NULL, hjust=0, ...)` — pkg=ggtree
- `geom_tippoint(mapping=NULL, data=NULL, position="identity", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, ...)` — pkg=ggtree
- `geom_tree(mapping=NULL, data=NULL, layout="rectangular", multiPhylo=FALSE, continuous="none", position="identity", ...)` — pkg=ggtree
- `geom_tree2(layout="rectangular", ...)` — pkg=ggtree
- `geom_treescale(x=NULL, y=NULL, width=NULL, offset=NULL, offset.label=NULL, label=NULL, color="black", linesize=0.5, fontsize=3.88, family="sans")` — pkg=ggtree
- `geom_zoom_clade(node, xexpand=NULL)` — pkg=ggtree
- `GeomHilightEncircle(?)` — pkg=ggtree
- `GeomInteractiveCurvelink(?)` — pkg=ggtree
- `GeomInteractiveHilightEncircle(?)` — pkg=ggtree
- `GeomInteractiveHilightRect(?)` — pkg=ggtree
- `GeomInteractiveLabelGGtree(?)` — pkg=ggtree
- `GeomInteractivePointGGtree(?)` — pkg=ggtree
- `GeomInteractiveSegmentGGtree(?)` — pkg=ggtree
- `GeomInteractiveTextGGtree(?)` — pkg=ggtree
- `get.path(phylo, from, to)` — pkg=ggtree
- `get_clade_position(treeview, node)` — pkg=ggtree
- `get_heatmap_column_position(treeview, by="bottom")` — pkg=ggtree
- `get_taxa_name(tree_view=NULL, node=NULL)` — pkg=ggtree
- `ggdensitree(data=NULL, mapping=NULL, layout="slanted", tip.order='mode', align.tips=TRUE, jitter=0, ...)` — pkg=ggtree
- `ggdoubletree(x, y=NULL, assoc=NULL, layout="rectangular", ladderize=TRUE, mirror=TRUE, optimize=FALSE, optimize_side=c("right", "both", "left"), gap=0.08, preserve_layers=TRUE, ...)` — pkg=ggtree
- `ggexpand(ratio, direction=1, side='hv')` — pkg=ggtree
- `ggplot(?)` — pkg=ggtree
- `ggsave(?)` — pkg=ggtree
- `ggtree(tr, mapping=NULL, layout="rectangular", open.angle=0, mrsd=NULL, as.Date=FALSE, yscale="none", yscale_mapping=NULL, ladderize=TRUE, right=FALSE, branch.length="branch.length", root.position=0, xlim=NULL, layout.params=list(as.graph = TRUE), hang=.1, ...)` — pkg=ggtree
- `ggtree_set_interactive(?)` — pkg=ggtree
- `ggtree_unset_interactive(?)` — pkg=ggtree
- `gheatmap(p, data, offset=0, width=1, low="green", high="red", color="white", colnames=TRUE, colnames_position="bottom", colnames_angle=0, colnames_level=NULL, colnames_offset_x=0, colnames_offset_y=0, font.size=4, family="", hjust=0.5, legend_title="value", custom_column_labels=NULL)` — pkg=ggtree
- `groupClade(.data, .node, group_name="group", ...)` — pkg=ggtree
- `groupOTU(.data, .node, group_name="group", ...)` — pkg=ggtree
- `guide_legend(?)` — pkg=ggtree
- `gzoom(phy, focus, subtree=FALSE, widths=c(.3, .7), tree_view, xmax_adjust=0, object)` — pkg=ggtree
- `hexpand(ratio, direction=1)` — pkg=ggtree
- `identify(?)` — pkg=ggtree
- `inset(tree_view, insets, width, height, hjust=0, vjust=0, x="node", reverse_x=FALSE, reverse_y=FALSE)` — pkg=ggtree
- `label_pad(label, justify="right", pad="\u00B7")` — pkg=ggtree
- `layout_circular(?)` — pkg=ggtree
- `layout_dendrogram(?)` — pkg=ggtree
- `layout_fan(angle=180)` — pkg=ggtree
- `layout_inward_circular(xlim=NULL)` — pkg=ggtree
- `layout_rectangular(?)` — pkg=ggtree
- `margin(?)` — pkg=ggtree
- `MRCA(.data, .node1, .node2=NULL, ...)` — pkg=ggtree
- `msaplot(p, fasta, offset=0, width=1, color=NULL, window=NULL, bg_line=TRUE, height=0.8)` — pkg=ggtree
- `multiplot(..., plotlist=NULL, ncol, widths=rep_len(1, ncol), labels=NULL, label_size=5)` — pkg=ggtree
- `nodebar(data, cols, color, alpha=1, position="stack")` — pkg=ggtree
- `nodeid(tree, label)` — pkg=ggtree
- `nodelab(tree, id)` — pkg=ggtree
- `nodepie(data, cols, color, alpha=1, outline.color="transparent", outline.size=0)` — pkg=ggtree
- `open_tree(treeview, angle)` — pkg=ggtree
- `plot_list(?)` — pkg=ggtree
- `range_format(x, trans=NULL)` — pkg=ggtree
- `read.tree(?)` — pkg=ggtree
- `revts(treeview)` — pkg=ggtree
- `rotate(tree_view=NULL, node)` — pkg=ggtree
- `rotate_tree(treeview, angle)` — pkg=ggtree
- `rtree(?)` — pkg=ggtree
- `scale_color(object, by, ...)` — pkg=ggtree
- `scale_color_manual(?)` — pkg=ggtree
- `scale_color_subtree(group)` — pkg=ggtree
- `scale_colour_manual(?)` — pkg=ggtree
- `scale_colour_subtree(group)` — pkg=ggtree
- `scale_fill_manual(?)` — pkg=ggtree
- `scale_x_continuous(?)` — pkg=ggtree
- `scale_x_ggtree(breaks=waiver(), labels=waiver())` — pkg=ggtree
- `scale_x_range(?)` — pkg=ggtree
- `scaleClade(tree_view=NULL, node, scale=1, vertical_only=TRUE)` — pkg=ggtree
- `set_hilight_legend(p, color, label, alpha=1)` — pkg=ggtree
- `StatBalance(?)` — pkg=ggtree
- `td_filter(?)` — pkg=ggtree
- `td_mutate(?)` — pkg=ggtree
- `td_unnest(?)` — pkg=ggtree
- `theme(?)` — pkg=ggtree
- `theme_dendrogram(bgcolor="white", fgcolor="black", ...)` — pkg=ggtree
- `theme_inset(legend.position="none", ...)` — pkg=ggtree
- `theme_tree(bgcolor="white", ...)` — pkg=ggtree
- `theme_tree2(bgcolor="white", fgcolor="black", ...)` — pkg=ggtree
- `unit(?)` — pkg=ggtree
- `vexpand(ratio, direction=1)` — pkg=ggtree
- `viewClade(tree_view=NULL, node, xmax_adjust=0)` — pkg=ggtree
- `xlim(?)` — pkg=ggtree
- `xlim_expand(xlim, panel)` — pkg=ggtree
- `xlim_tree(xlim)` — pkg=ggtree
- `zoomClade(tree_view=NULL, node, xexpand=NULL)` — pkg=ggtree

### Generic (2)
- `ggplot_add(object, plot, object_name, ...)` — pkg=ggtree
- `offspring(.data, .node, tiponly=FALSE, self_include=FALSE, ...)` — pkg=ggtree

## ggtreeExtra (1.23.1) — 18 symbols

### Function (18)
- `%>%(?)` — pkg=ggtreeExtra
- `fruit_plot(p, data=NULL, geom, mapping, offset=0.03, pwidth=0.2, position="auto", ...)` — pkg=ggtreeExtra
- `geom_fruit(mapping, data=NULL, geom, offset=0.03, pwidth=0.2, position="auto", inherit.aes=FALSE, grid.params=NULL, axis.params=list( axis="none", text.angle=0, text..., ...)` — pkg=ggtreeExtra
- `geom_fruit_list(fruit, ...)` — pkg=ggtreeExtra
- `ggplot_add(object, plot, object_name, ...)` — pkg=ggtreeExtra
- `position_dodgex(?)` — pkg=ggtreeExtra
- `position_dodgex2(?)` — pkg=ggtreeExtra
- `position_identityx(?)` — pkg=ggtreeExtra
- `position_jitterdodgex(jitter.width=NULL, jitter.height=0, dodge.width=0.75, hexpand=NA, vexpand=NA, seed=NA)` — pkg=ggtreeExtra
- `position_jitterx(width=NULL, height=NULL, hexpand=NA, vexpand=NA, seed=NA)` — pkg=ggtreeExtra
- `position_points_jitterx(width=0, height=0.2, yoffset=0, hexpand=NA, adjust_vlines=FALSE, seed=NULL)` — pkg=ggtreeExtra
- `position_points_sinax(rel_min=0.02, rel_max=0.98, seed=NULL, hexpand=NA)` — pkg=ggtreeExtra
- `position_raincloudx(width=0, height=0.4, ygap=0.05, hexpand=NA, adjust_vlines=FALSE, seed=NULL)` — pkg=ggtreeExtra
- `position_stackx(vjust=1, hexpand=NA, vexpand=NA, reverse=FALSE)` — pkg=ggtreeExtra
- `PositionJitterdodgex(?)` — pkg=ggtreeExtra
- `PositionJitterx(?)` — pkg=ggtreeExtra
- `td_filter(?)` — pkg=ggtreeExtra
- `td_unnest(?)` — pkg=ggtreeExtra

## gson (?) — 0 symbols

## ivolcano (0.0.7) — 16 symbols

### Function (14)
- `geom_ivolcano_gene(top_n=10, label_mode="separate", fontface="italic", label_sig_only=TRUE, filter=NULL)` — pkg=ivolcano
- `geom_ivolcano_line(linetype="longdash", color='grey40', linewidth=0.5)` — pkg=ivolcano
- `idotplot(object, x="GeneRatio", color="p.adjust", showCategory=10, size="Count", label_format=30, trigger=c("click", "hover"), title="", ...)` — pkg=ivolcano
- `ivolcano(data, logFC_col="logFC", pval_col="adj.P.Val", gene_col="gene", title="Volcano Plot", interactive=TRUE, onclick_fun=NULL, pval_cutoff=0.05, logFC_cutoff=1, pval_cutoff2=NULL, logFC_cutoff2=NULL, size_by="none", point_size=list(base = 2, medium = 4, large = 6), threshold_line=list(color = "black", linetype = "das..., tooltip_cols=NULL, tooltip_labels=NULL, top_n=10, label_mode="separate", fontface="italic", label_sig_only=TRUE, filter=NULL)` — pkg=ivolcano
- `ivolcano_point(data, logFC_col="logFC", pval_col="adj.P.Val", gene_col="gene", title="Volcano Plot", interactive=TRUE, onclick_fun=NULL, pval_cutoff=0.05, logFC_cutoff=1, pval_cutoff2=NULL, logFC_cutoff2=NULL, size_by="none", point_size=list(base = 2, medium = 4, large = 6), tooltip_cols=NULL, tooltip_labels=NULL)` — pkg=ivolcano
- `onclick_ensembl(gene)` — pkg=ivolcano
- `onclick_fanyi(gene_summary, cols)` — pkg=ivolcano
- `onclick_genecards(gene)` — pkg=ivolcano
- `onclick_hgnc(gene)` — pkg=ivolcano
- `onclick_ncbi(gene)` — pkg=ivolcano
- `onclick_pubmed(gene)` — pkg=ivolcano
- `onclick_uniprot(gene)` — pkg=ivolcano
- `pathway_app(enrichment, gene_data, pathway_col="Description", pathway_gene_col="geneID", pathway_p_col="p.adjust", pathway_ratio_col="GeneRatio", gene_col="gene", gene_effect_col="logFC", gene_p_col="adj.P.Val", show_pathways=NULL, gene_id_case=c("asis", "upper", "lower"), pval_cutoff=0.05, logFC_cutoff=1, launch=FALSE, app_title="Pathway-gene explorer")` — pkg=ivolcano
- `scale_color_figureya(mode=c("classic", "advanced"), na.value="grey80", guide="none", ...)` — pkg=ivolcano

### Generic (2)
- `ggplot_add(object, plot, ...)` — pkg=ivolcano
- `print(x, ...)` — pkg=ivolcano

## meshes (1.39.3) — 8 symbols

### Function (8)
- `enrichMeSH(gene, MeSHDb, database='gendoo', category='C', pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, meshdbVersion=NULL)` — pkg=meshes
- `geneID(?)` — pkg=meshes
- `geneInCategory(?)` — pkg=meshes
- `geneSim(geneID1, geneID2=NULL, measure="Wang", combine="BMA", semData)` — pkg=meshes
- `get_organism(?)` — pkg=meshes
- `gseMeSH(geneList, MeSHDb, database='gendoo', category='C', nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, seed=FALSE, ...)` — pkg=meshes
- `meshdata(MeSHDb=NULL, database, category, computeIC=FALSE)` — pkg=meshes
- `meshSim(meshID1, meshID2, measure="Wang", semData)` — pkg=meshes

## scMSGNN (0.3.0) — 4 symbols

### Generic (4)
- `ensure_tensor(x, dtype=torch::torch_float32(), device=NULL, ...)` — pkg=scMSGNN
- `scMSGNN_Annotate(object, markers, assay=NULL, n_background=100, slot="data", ...)` — pkg=scMSGNN
- `scMSGNN_CorrectBatch(object, features=NULL, k_neighbors=20, k_scales=NULL, sign_k=2, hidden_dims=c(128, 64), epochs=50, lr=0.001, batch_size=256, device="cpu", adj_matrix=NULL, pathway_mask=NULL, adj_lambda=1.0, batch=NULL, batch_lambda=1.0, ...)` — pkg=scMSGNN
- `scMSGNN_Run(object, features=NULL, k_neighbors=20, k_scales=NULL, sign_k=2, hidden_dims=c(128, 64), epochs=50, lr=0.001, batch_size=256, device="cpu", adj_matrix=NULL, pathway_mask=NULL, adj_lambda=1.0, ...)` — pkg=scMSGNN

## scholar (1.0.0) — 30 symbols

### Function (30)
- `author_position(?)` — pkg=scholar
- `compare_scholar_careers(?)` — pkg=scholar
- `compare_scholars(?)` — pkg=scholar
- `format_publications(scholar.profile, author.name=NULL)` — pkg=scholar
- `get_article_cite_history(?)` — pkg=scholar
- `get_article_scholar_url(?)` — pkg=scholar
- `get_citation_history(?)` — pkg=scholar
- `get_coauthors(id, n_coauthors=5, n_deep=1)` — pkg=scholar
- `get_complete_authors(id, pubid, delay=.4, initials=TRUE)` — pkg=scholar
- `get_journalrank(?)` — pkg=scholar
- `get_num_articles(?)` — pkg=scholar
- `get_num_distinct_journals(?)` — pkg=scholar
- `get_num_top_journals(?)` — pkg=scholar
- `get_oldest_article(?)` — pkg=scholar
- `get_profile(?)` — pkg=scholar
- `get_publication_abstract(?)` — pkg=scholar
- `get_publication_data_extended(?)` — pkg=scholar
- `get_publication_date(?)` — pkg=scholar
- `get_publication_metrics(?)` — pkg=scholar
- `get_publication_url(?)` — pkg=scholar
- `get_publications(?)` — pkg=scholar
- `get_publications_all_authors(?)` — pkg=scholar
- `get_scholar_id(?)` — pkg=scholar
- `get_scholar_metrics(?)` — pkg=scholar
- `get_scholar_resp(url, attempts_left=5)` — pkg=scholar
- `plot_coauthors(network, size_labels=5)` — pkg=scholar
- `predict_h_index(?)` — pkg=scholar
- `search_scholar_ids(?)` — pkg=scholar
- `set_scholar_mirror(mirror=NULL)` — pkg=scholar
- `tidy_id(id)` — pkg=scholar

## sclet (1.0.1) — 208 symbols

### Function (208)
- `ActiveIdent(object)` — pkg=sclet
- `ActiveIdent<-(?)` — pkg=sclet
- `AggregateExpression(object, group_by, assay.type="counts", fun="sum")` — pkg=sclet
- `as.SCE(object, ...)` — pkg=sclet
- `as.Seurat(object, ...)` — pkg=sclet
- `assay(?)` — pkg=sclet
- `AuditAnalysisChain(sce, features, raw_layer="counts", integrated_layer=NULL, ...)` — pkg=sclet
- `BatchRemover(sce, batch=NULL, HVG=NULL, nHVG=5000, assay.type="logcounts", PARAM=NULL, restrict=NULL, correct.all=FALSE, name="batchcorrect")` — pkg=sclet
- `CellDimPlot(object, group.by=NULL, reduction=NULL, ...)` — pkg=sclet
- `CellRankSummary(object, id=NULL)` — pkg=sclet
- `CellStatPlot(object, group.by=NULL, split.by=NULL, position="fill", ...)` — pkg=sclet
- `colData(?)` — pkg=sclet
- `colData<-(?)` — pkg=sclet
- `CommandLog(object, details=FALSE)` — pkg=sclet
- `DefaultAssay(object)` — pkg=sclet
- `DefaultAssay<-(?)` — pkg=sclet
- `DefaultGraph(object)` — pkg=sclet
- `DefaultGraph<-(?)` — pkg=sclet
- `DefaultLayer(object)` — pkg=sclet
- `DefaultLayer<-(?)` — pkg=sclet
- `DefaultReduction(object)` — pkg=sclet
- `DefaultReduction<-(?)` — pkg=sclet
- `DEtestPlot(object, id=NULL, p_val_cutoff=0.05, logfc_cutoff=0.25, ...)` — pkg=sclet
- `DimPlot(object, reduction=NULL, ...)` — pkg=sclet
- `ElbowPlot(object)` — pkg=sclet
- `EnrichmentPlot(object, id=NULL, showCategory=10, ...)` — pkg=sclet
- `FeatureDimPlot(object, features, layer=NULL, reduction=NULL, ...)` — pkg=sclet
- `FeatureScatter(object, feature1, feature2)` — pkg=sclet
- `FindAllMarkers(object, min.pct=0.01, logfc.threshold=0.1, return.thresh=0.01, only.pos=FALSE, base=2, pseudocount.use=1, assay=NULL, layer=NULL, ...)` — pkg=sclet
- `FindClusters(object, resolution=0.5)` — pkg=sclet
- `FindMarkerPathways(sce, altExp_name="PathwayScores", group.by=NULL, assay="scores", ...)` — pkg=sclet
- `FindMarkers(object, ident.1=NULL, ident.2=NULL, min.pct=0.01, logfc.threshold=0.1, base=2, pseudocount.use=1, assay=NULL, layer=NULL, ...)` — pkg=sclet
- `FindMarkers_pseudobulk(object, design, contrast, ...)` — pkg=sclet
- `FindNeighbors(object, dims, reduction=NULL, k=10)` — pkg=sclet
- `FindVariableFeatures(object, nfeatures=2000, method="scran", ...)` — pkg=sclet
- `gene_summary_table(gene, gene_col="gene", orgDb="org.Hs.eg.db", keyType="SYMBOL", cluster_col, output="html", browse=TRUE)` — pkg=sclet
- `genecurve_plot(sce, assay_name="logcounts", features, lineaegs=NULL, pseudotime.data="slingPseudotime", method=c("smooth","gam"), point=FALSE, line.size=0.8, alpha=0.5, size=1, ncol=NULL, se=TRUE)` — pkg=sclet
- `get_analysis_context(object, element=NULL)` — pkg=sclet
- `get_annotation(object, element=NULL, id=NULL)` — pkg=sclet
- `get_batch(object, element=NULL)` — pkg=sclet
- `get_cci(object, id=NULL)` — pkg=sclet
- `get_cellchat(object, element=NULL, id=NULL)` — pkg=sclet
- `get_cellphonedb(object, element=NULL, id=NULL)` — pkg=sclet
- `get_cellrank(object, element=NULL, id=NULL)` — pkg=sclet
- `get_colocalization(object, element=NULL)` — pkg=sclet
- `get_detest(object, id=NULL)` — pkg=sclet
- `get_enrichment(object, id=NULL)` — pkg=sclet
- `get_geneset_scoring(object, element=NULL, id=NULL)` — pkg=sclet
- `get_graph(object, name=NULL, element=NULL)` — pkg=sclet
- `get_hvg(object, element=NULL)` — pkg=sclet
- `get_integration(object, element=NULL, id=NULL)` — pkg=sclet
- `get_mapping(object, element=NULL, id=NULL)` — pkg=sclet
- `get_milo(object, element=NULL, id=NULL)` — pkg=sclet
- `get_nichenet(object, element=NULL, id=NULL)` — pkg=sclet
- `get_perturbation(object, element=NULL, id=NULL)` — pkg=sclet
- `get_perturbation_priority(object, element=NULL)` — pkg=sclet
- `get_program(object, program, source=c("auto", "geneset_scoring", "scenic"), id=NULL, assay=NULL)` — pkg=sclet
- `get_rare_cells(object, element=NULL)` — pkg=sclet
- `get_scenic(object, element=NULL, id=NULL)` — pkg=sclet
- `get_spatial(object, element=NULL, id=NULL)` — pkg=sclet
- `get_spatial_niche(object, element=NULL)` — pkg=sclet
- `get_supercell(object, element=NULL, id=NULL)` — pkg=sclet
- `get_trajectory(object, element=NULL, id=NULL)` — pkg=sclet
- `get_velocity(object, element=NULL, id=NULL)` — pkg=sclet
- `GroupHeatmap(object, features, group.by=NULL, layer=NULL, ...)` — pkg=sclet
- `has_annotation(object, id=NULL)` — pkg=sclet
- `has_batch(object)` — pkg=sclet
- `has_cci(object, id=NULL)` — pkg=sclet
- `has_cellchat(object, id=NULL)` — pkg=sclet
- `has_cellphonedb(object, id=NULL)` — pkg=sclet
- `has_cellrank(object)` — pkg=sclet
- `has_colocalization(object)` — pkg=sclet
- `has_detest(object, id=NULL)` — pkg=sclet
- `has_enrichment(object, id=NULL)` — pkg=sclet
- `has_geneset_scoring(object, id=NULL)` — pkg=sclet
- `has_graph(object, name=NULL)` — pkg=sclet
- `has_hvg(object)` — pkg=sclet
- `has_integration(object, id=NULL)` — pkg=sclet
- `has_mapping(object, id=NULL)` — pkg=sclet
- `has_milo(object, id=NULL)` — pkg=sclet
- `has_multimodal_adt(sce)` — pkg=sclet
- `has_multimodal_atac(sce)` — pkg=sclet
- `has_nichenet(object, id=NULL)` — pkg=sclet
- `has_perturbation(object)` — pkg=sclet
- `has_perturbation_priority(object)` — pkg=sclet
- `has_program(object, program, source=c("auto", "geneset_scoring", "scenic"), id=NULL)` — pkg=sclet
- `has_rare_cells(object)` — pkg=sclet
- `has_scenic(object, id=NULL)` — pkg=sclet
- `has_spatial(object)` — pkg=sclet
- `has_spatial_niche(object)` — pkg=sclet
- `has_supercell(object, id=NULL)` — pkg=sclet
- `has_trajectory(object, id=NULL)` — pkg=sclet
- `has_velocity(object, id=NULL)` — pkg=sclet
- `Idents(object)` — pkg=sclet
- `LayerData(object, layer=NULL)` — pkg=sclet
- `Layers(object)` — pkg=sclet
- `lineage_plot(sce, dims=c(1, 2), group, reduction="UMAP", lineages=NULL, cells=NULL, slot="data", mapping=NULL, geom=sc_geom_point, linewidth=0.9, ...)` — pkg=sclet
- `logNormCounts(?)` — pkg=sclet
- `NormalizeData(object, scale.factor=10000, assay="counts")` — pkg=sclet
- `PercentageFeatureSet(object, pattern=NULL, feature=NULL)` — pkg=sclet
- `PipelineSummary(object)` — pkg=sclet
- `plot_cci_arrow(object, cell_a, cell_b, group, id=NULL, pval_thresh=0.05, top_n=NULL, layer="logcounts")` — pkg=sclet
- `plot_cci_bubble(object, sources=NULL, targets=NULL, id=NULL, pval_thresh=0.05, type=c("interaction", "summary", "facet"), top_n=NULL)` — pkg=sclet
- `plot_cci_chord(object, signaling=NULL, id=NULL, pval_thresh=0.05, ...)` — pkg=sclet
- `plot_cci_network(object, signaling=NULL, id=NULL, pval_thresh=0.05, layout="circle", edge_width_scale=1)` — pkg=sclet
- `plot_cci_sigmoid(object, id=NULL, pval_thresh=0.05, top_n=NULL)` — pkg=sclet
- `plot_cell_dim(object, group.by=NULL, reduction=NULL, ...)` — pkg=sclet
- `plot_cell_stat(object, group.by=NULL, split.by=NULL, position="fill", ...)` — pkg=sclet
- `plot_detest(object, id=NULL, p_val_cutoff=0.05, logfc_cutoff=0.25, ...)` — pkg=sclet
- `plot_dim_scatter(object, reduction=NULL, ...)` — pkg=sclet
- `plot_enrichment(object, id=NULL, showCategory=10, ...)` — pkg=sclet
- `plot_fate_driver_trends(object, lineage=NULL, features=NULL, top_n=6, layer=NULL, x=c("auto", "pseudotime", "fate_probabi..., id=NULL, alpha=0.15, point_size=0.4, line_size=0.6, se=FALSE, ncol=NULL)` — pkg=sclet
- `plot_fate_probability(object, fate=NULL, reduction=NULL, id=NULL, point_size=0.5, alpha=0.9)` — pkg=sclet
- `plot_fate_terminal_states(object, reduction=NULL, id=NULL, point_size=0.5, alpha=0.9, na_color="grey80")` — pkg=sclet
- `plot_feature_dim(object, features, layer=NULL, reduction=NULL, ...)` — pkg=sclet
- `plot_genecurve(sce, assay_name="logcounts", features, lineaegs=NULL, pseudotime.data="slingPseudotime", method=c("smooth","gam"), point=FALSE, line.size=0.8, alpha=0.5, size=1, ncol=NULL, se=TRUE)` — pkg=sclet
- `plot_group_heatmap(object, features, group.by=NULL, layer=NULL, ...)` — pkg=sclet
- `plot_lineage(sce, dims=c(1, 2), group, reduction="UMAP", lineages=NULL, cells=NULL, slot="data", mapping=NULL, geom=sc_geom_point, linewidth=0.9, ...)` — pkg=sclet
- `plot_list(?)` — pkg=sclet
- `plot_perturbation_ranking(object, n=20, fill_color="steelblue")` — pkg=sclet
- `plot_program_activity(object, program, source=c("auto", "geneset_scoring", "scenic"), reduction=NULL, id=NULL, assay=NULL, point_size=0.6, low="grey90", high="firebrick")` — pkg=sclet
- `plot_program_dotplot(object, programs, source=c("auto", "geneset_scoring", "scenic"), group.by=NULL, id=NULL, low="#2166AC", high="#B2182B")` — pkg=sclet
- `plot_program_heatmap(object, programs, source=c("auto", "geneset_scoring", "scenic"), group.by=NULL, id=NULL, assay=NULL, scale_rows=TRUE, low="#2166AC", mid="white", high="#B2182B")` — pkg=sclet
- `plot_projection(query, ref, reduction="UMAP", group.by=NULL, ...)` — pkg=sclet
- `plot_pseudo_heatmap(sce, features, assay_name="logcounts", pseudotime.data="slingPseudotime", lineage=NULL, scale=TRUE, sort=TRUE, cluster_columns=FALSE, cluster_rows=FALSE)` — pkg=sclet
- `plot_pseudotime(sce, reduction=NULL, pseudotime.data="slingPseudotime", lineage=NULL, ...)` — pkg=sclet
- `plot_reference_label_confidence(object, id=NULL, labels_col=NULL, score_col=NULL, type=c("violin", "boxplot"), sort_by_score=TRUE, point_size=0.5, jitter_width=0.15)` — pkg=sclet
- `plot_reference_label_transfer_heatmap(object, group.by=NULL, id=NULL, labels_col=NULL, normalize=c("row", "column", "none"), show_text=TRUE, digits=2, low="white", high="#B2182B")` — pkg=sclet
- `plot_scenic_activity(object, regulon, reduction=NULL, id=NULL, assay="AUC", point_size=0.6, low="grey90", high="firebrick")` — pkg=sclet
- `plot_spatial_composition(object, n=15, scale_rows=TRUE, low="#2166AC", high="#B2182B")` — pkg=sclet
- `plot_spatial_deconvolution(object, n=20, fill_color="darkgreen")` — pkg=sclet
- `plot_top_velocity_genes(object, id=NULL, assay=NULL, n=20, fill="steelblue")` — pkg=sclet
- `plot_trajectory_overview(object, id=NULL, reduction=NULL, group=NULL, panels=c("lineage", "velocity", "terminal_st...)` — pkg=sclet
- `plot_velocity(sce, reduction=NULL, group.by=NULL, id=NULL, ...)` — pkg=sclet
- `plot_velocity_fate_correlation(object, fate=NULL, velocity_id=NULL, trajectory_id=NULL, assay=NULL, point_size=0.8, alpha=0.8)` — pkg=sclet
- `plot_velocity_latent_time(object, reduction=NULL, id=NULL, point_size=0.6, low="grey90", high="firebrick")` — pkg=sclet
- `plot_velocity_magnitude(object, reduction=NULL, id=NULL, assay=NULL, point_size=0.6, low="grey90", high="navy")` — pkg=sclet
- `plotColData(?)` — pkg=sclet
- `ProjectionPlot(query, ref, reduction="UMAP", group.by=NULL, ...)` — pkg=sclet
- `pseudo_heatmap(sce, features, assay_name="logcounts", pseudotime.data="slingPseudotime", lineage=NULL, scale=TRUE, sort=TRUE, cluster_columns=FALSE, cluster_rows=FALSE)` — pkg=sclet
- `pseudo_plot(sce, reduction=NULL, pseudotime.data="slingPseudotime", lineage=NULL, ...)` — pkg=sclet
- `QCMetrics(object)` — pkg=sclet
- `Read10X(data.dir, backend=c("memory", "HDF5"), ...)` — pkg=sclet
- `ReadH5AD(file, ...)` — pkg=sclet
- `refit_milo(milo, design_df, bad_hood, formula, contrasts, glmm=TRUE, glmm.solver="Fisher", REML=TRUE, max.iters=50, fail.on.error=FALSE, fdr.weighting="graph-overlap", norm.method="TMM", BPPARAM=NULL, old_results=NULL, seed=2025, ...)` — pkg=sclet
- `register_multimodal_adt(sce, name="ADT")` — pkg=sclet
- `register_multimodal_atac(sce, name="ATAC")` — pkg=sclet
- `RenameIdents(object, new_ids)` — pkg=sclet
- `rowData(?)` — pkg=sclet
- `rowData<-(?)` — pkg=sclet
- `RunCCI(object, method=c("CellChat", "CellPhoneDB", "NicheNet"), keep_object=FALSE, ...)` — pkg=sclet
- `RunCellChat(sce, group=NULL, assay_name=NULL, layer=NULL, species="human", db_item=c("Secreted Signaling"), type="triMean", trim=0.1, min.cells=10, name="cellchat", return=c("cellchat", "sce", "both"), keep_object=FALSE)` — pkg=sclet
- `RunCellFate(sce, method=c("CellRank"), reduction="PCA", cluster_key=ActiveIdent(sce), velocity_id=NULL, backend=c("basilisk", "reticulate"), python=NULL, name="cellfate", ...)` — pkg=sclet
- `RunCellPhoneDB(sce, group=NULL, assay_name=NULL, layer=NULL, species="human", name="cellphonedb", threads=4, iterations=1000, pvalue=0.05, ...)` — pkg=sclet
- `RunCellRank(sce, reduction="PCA", cluster_key=ActiveIdent(sce), velocity_id=NULL, backend=c("basilisk", "reticulate"), python=NULL, name="cellrank", ...)` — pkg=sclet
- `RunDecontX(sce, assay="counts", ...)` — pkg=sclet
- `RunDEtest(object, ident.1=NULL, ident.2=NULL, name="detest", ...)` — pkg=sclet
- `RunDiffusionMap(sce, n_components=50, reduction=NULL, ...)` — pkg=sclet
- `RunDoubletFinder(sce, ...)` — pkg=sclet
- `RunEnrichment(object, id=NULL, p_val_cutoff=0.05, logfc_cutoff=0.25, db=c("GO", "KEGG"), orgDb="org.Hs.eg.db", keyType="SYMBOL", ont="BP", name="enrichment", ...)` — pkg=sclet
- `RunExplorer(object, ...)` — pkg=sclet
- `RunGeneSetScoring(sce, gene_sets=NULL, features=NULL, method=c("UCell", "AUCell", "GSVA"), assay_use="counts", ncores=1, name="Score", as_altExp=FALSE, ...)` — pkg=sclet
- `RunGRN(sce, tfs_path, motif_annotations_path, database_paths, assay_use="counts", method=c("SCENIC"), name="grn", ...)` — pkg=sclet
- `RunImputation(sce, method="ALRA", assay="logcounts", ...)` — pkg=sclet
- `RunInSilicoPerturbation(sce, target_gene, perturbation_value=0.0, base_grn_path, cluster_key=ActiveIdent(sce), reduction="PCA", ...)` — pkg=sclet
- `RunIntegration(object, method=c("fastMNN", "Harmony", "scVI"), batch=NULL, features=NULL, layer=NULL, reduction=NULL, name=NULL, ...)` — pkg=sclet
- `RunKEGG(sce, species="hsa", method="UCell", find_markers=TRUE, group.by=NULL, name="KEGG", ...)` — pkg=sclet
- `RunKNNPredict(object, ref, labels=NULL, features=NULL, layer=NULL, k=5, name="knn_map", ...)` — pkg=sclet
- `RunMilo(sce, sample_col, condition_col, covariates=NULL, contrasts=NULL, k1=10, k2=10, d1=30, d2=30, d3=30, prop=0.1, overlap=1, per_contrast=TRUE, is_refined=TRUE, refinement_scheme="graph", adjustment="BH", glmm=FALSE, random_effect=NULL, glmm_solver="Fisher", REML=TRUE, max.iters=50, fail.on.error=FALSE, BPPARAM=NULL, seed=2025, name="milo", ...)` — pkg=sclet
- `RunMultimodalWorkflow(sce, register_adt=TRUE, register_atac=TRUE, name="multimodal")` — pkg=sclet
- `RunNicheNet(sce, group=NULL, receiver, sender="all", genes_oi=NULL, ligand_target_matrix, lr_network, weighted_networks, assay_name=NULL, layer=NULL, name="nichenet", top_n_ligands=20, exprs_pct=0.10)` — pkg=sclet
- `RunPCA(object, subset_row=NULL, exprs_values=NULL, layer=NULL, ncomponents=50, ...)` — pkg=sclet
- `RunPerturbationPriority(sce, condition_col, group_col=NULL, layer=NULL, assay=NULL, name="augur", ...)` — pkg=sclet
- `RunPhenotypeAssociation(sce, bulk_matrix, phenotype_data, family="cox", ...)` — pkg=sclet
- `RunProgramWorkflow(sce, gene_sets=NULL, scoring_method=c("UCell", "AUCell", "GSVA"), assay_use="counts", scoring_as_altExp=FALSE, run_scenic=c("auto", "never", "always"), tfs_path=NULL, motif_annotations_path=NULL, database_paths=NULL, name="program_workflow")` — pkg=sclet
- `RunRareCellDetection(sce, method=c("density"), reduction="PCA", dims=1:20, k=20, q_threshold=0.25, rare_threshold=10, name="rareq")` — pkg=sclet
- `RunReferenceMapping(object, ref, labels=NULL, method=c("SingleR", "KNN", "Symphony"), assay.type=NULL, layer=NULL, features=NULL, k=5, vars=NULL, name="mapping", ...)` — pkg=sclet
- `RunReferenceWorkflow(object, ref, labels=NULL, method=c("SingleR", "KNN", "Symphony"), assay.type=NULL, layer=NULL, features=NULL, k=5, vars=NULL, name="reference_workflow", ...)` — pkg=sclet
- `RunRegVelo(sce, grn, regulators=NULL, spliced_assay="spliced", unspliced_assay="unspliced", reduction=NULL, name="regvelo", max_epochs=1500L, lam=1, lam2=0, batch_size=NULL, seed=0L, backend=c("basilisk", "reticulate"), python=NULL, ...)` — pkg=sclet
- `RunSCENIC(sce, tfs_path, motif_annotations_path, database_paths, assay_use="counts", num_workers=1L, seed=123L, name="scenic", output_dir=NULL, save_intermediate=FALSE, resume=FALSE)` — pkg=sclet
- `RunSingleR(object, ref=NULL, labels=NULL, assay.type=NULL, layer=NULL, name="singler", ...)` — pkg=sclet
- `RunSlingshot(sce, group, reduction="UMAP", start_cluster=NULL, end_cluster=NULL, reverse=FALSE, align_start=FALSE, seed=2025, name="slingshot")` — pkg=sclet
- `RunSpatialColocalization(sce, features=NULL, method=c("SVP"), name="colocalization", ...)` — pkg=sclet
- `RunSpatialDeconvolution(sce_spatial, sce_ref, ref_group_key, ref_batch_key=NULL, max_epochs=250L, name="spatial_deconv", ...)` — pkg=sclet
- `RunSpatialNiche(sce, features=NULL, method=c("SVP"), name="spatial_niche", ...)` — pkg=sclet
- `RunSpatialWorkflow(sce, sce_ref=NULL, ref_group_key=NULL, run_deconvolution=TRUE, run_colocalization=FALSE, run_niche=FALSE, name="spatial_workflow", ...)` — pkg=sclet
- `RunStandardPipeline(object, nfeatures=2000, npcs=50, dims=1:30, resolution=0.8, ...)` — pkg=sclet
- `RunStatePriorityWorkflow(sce, condition_col=NULL, group_col=NULL, run_perturbation_priority=TRUE, run_rare_cell_detection=FALSE, name="state_priority", ...)` — pkg=sclet
- `RunSuperCell(object, assay="logcounts", layer=NULL, nHVG=2000, hvg_method="scran", cellname="Barcode", gamma=20, k.knn=5, name="supercell")` — pkg=sclet
- `RunSymphonyMapping(object, ref, labels=NULL, vars=NULL, k=5, layer=NULL, name="symphony_map", ...)` — pkg=sclet
- `RunTrajectoryWorkflow(sce, group=NULL, reduction=NULL, run_diffusion_map=TRUE, run_slingshot=TRUE, run_velocity=c("auto", "never", "always"), run_fate=c("auto", "never", "always"), diffusion_components=50, velocity_mode=c("deterministic", "stochastic", "dyn..., start_cluster=NULL, end_cluster=NULL, name="trajectory_workflow")` — pkg=sclet
- `RunUMAP(object, dims=NULL, reduction=NULL, layer=NULL)` — pkg=sclet
- `RunVelocity(sce, mode=c("deterministic", "stochastic", "dyn..., use.dimred=NULL, subset.row=NULL, subset_row=NULL, name="velocity", ...)` — pkg=sclet
- `ScaleData(object, features=NULL, assay="logcounts")` — pkg=sclet
- `sce_merge(sce_list, combineVarParams=list(equiweight = TRUE, ncells = NULL))` — pkg=sclet
- `sclet_copilot(sce, question, model=NULL)` — pkg=sclet
- `Status(object, details=FALSE)` — pkg=sclet
- `subset_cell(x, feature="nFeature_RNA", method='mad', n=3)` — pkg=sclet
- `subset_feature(x, mincell, peek=TRUE)` — pkg=sclet
- `SummarizeContextForLLM(sce)` — pkg=sclet
- `TopVelocityGenes(object, id=NULL, assay=NULL, n=20, decreasing=TRUE)` — pkg=sclet
- `VariableFeaturePlot(object, label=NULL, method=NULL)` — pkg=sclet
- `VariableFeatures(object, method="scran", ...)` — pkg=sclet
- `VelocityFateCorrelation(object, velocity_id=NULL, trajectory_id=NULL, assay=NULL, method=c("spearman", "pearson", "kendall"))` — pkg=sclet
- `VelocityMagnitude(object, id=NULL, assay=NULL, margin=c("cell", "gene"), name=NULL, store=FALSE)` — pkg=sclet
- `VelocityPlot(sce, reduction=NULL, group.by=NULL, id=NULL, ...)` — pkg=sclet
- `VlnPlot(object, features, ncol="auto")` — pkg=sclet
- `WriteH5AD(object, file, ...)` — pkg=sclet

## seqmagick (0.1.9) — 30 symbols

### Function (30)
- `bam2DNAStringSet(bamfile, refseq)` — pkg=seqmagick
- `bam2DNAStringSet2(bamfile, refseq)` — pkg=seqmagick
- `bs_aln(x, method='muscle', ...)` — pkg=seqmagick
- `bs_consensus(x, type="DNA", r=1)` — pkg=seqmagick
- `bs_filter(x, pattern, by='description', ignore.case=FALSE)` — pkg=seqmagick
- `bs_hamming(x, count_indel=FALSE, ...)` — pkg=seqmagick
- `bs_rename(x, mapping, position=NULL, sep=NULL, mode="replace")` — pkg=seqmagick
- `clw_read(file, type="auto")` — pkg=seqmagick
- `consensus(x, type="DNA")` — pkg=seqmagick
- `download_genbank(acc, db="nuccore", format="genbank", outfile=NULL)` — pkg=seqmagick
- `fa_combine(file1, file2, outfile=NULL, type="interleaved")` — pkg=seqmagick
- `fa_filter(fasfile, pattern, by='description', ignore.case=FALSE, outfile=NULL, type="interleaved")` — pkg=seqmagick
- `fa_read(file, type="auto")` — pkg=seqmagick
- `fa_rename(fasfile, mapping_file, position=NULL, sep=NULL, mode="replace", outfile)` — pkg=seqmagick
- `fa_summary(x)` — pkg=seqmagick
- `fa_to_interleaved(file, outfile)` — pkg=seqmagick
- `fa_to_sequential(file, outfile)` — pkg=seqmagick
- `fa_write(x, outfile, type="interleaved")` — pkg=seqmagick
- `fas2phy(fasfile, outfile="out.phy", type="sequential")` — pkg=seqmagick
- `gb_read(file)` — pkg=seqmagick
- `get_id(x, sep=" ", position)` — pkg=seqmagick
- `mega_read(?)` — pkg=seqmagick
- `ncbi_fa_read(acc, db="nuccore", type="auto")` — pkg=seqmagick
- `phy2fas(phyfile, outfile="out.fas", type="interleaved")` — pkg=seqmagick
- `phy_read(file)` — pkg=seqmagick
- `phy_write(x, outfile, type="sequential")` — pkg=seqmagick
- `renameTXT(txt_file, name_file, sep="_", split=TRUE)` — pkg=seqmagick
- `replaceInside(fasfile, from="-", to="N", outfile=NULL)` — pkg=seqmagick
- `seqlen(fasfile)` — pkg=seqmagick
- `sth_read(file, type="auto")` — pkg=seqmagick

## tidytree (?) — 0 symbols

## tigeR (1.0.0) — 64 symbols

### Function (64)
- `ABIS(SE, sig_matrix)` — pkg=tigeR
- `bind_meta(SE, isList)` — pkg=tigeR
- `bind_mtr(SE, isList)` — pkg=tigeR
- `browse_BE(SE)` — pkg=tigeR
- `browse_biomk(SE, feature, colors=NULL, PT_drop=FALSE, lg.pos=c(0.7,0.14))` — pkg=tigeR
- `build_CellType_Ref(Seurat_obj, logfc.threshold=0.1, min.pct=0.1, only.pos=TRUE)` — pkg=tigeR
- `build_Model(SE, Model, feature_genes, rmBE=FALSE, response_NR=TRUE, PT_drop=TRUE, mtr, meta, ...)` — pkg=tigeR
- `cell_name_filter(mtr)` — pkg=tigeR
- `cell_name_standardization(SE)` — pkg=tigeR
- `CIBERSORT(SE, sig_matrix, perm=0, QN=TRUE, style='elegant', group_color=c("#5f96e8CC", "#ee822fCC"))` — pkg=tigeR
- `compare_biomk(SE=NULL, Signature=NULL, method="Average_mean", PT_drop=TRUE, show.val=TRUE, val.size=2)` — pkg=tigeR
- `compare_roc(ROC, lg.label=c("NB","SVM","RF","CC","ADB","LGB","L..., line.col=c("black", "#F89B9B", "#4DB867", "#C6...)` — pkg=tigeR
- `ConsensusTME(SE, cancer="SKCM", ...)` — pkg=tigeR
- `count2tpm(counts)` — pkg=tigeR
- `data_standardization(SE, type)` — pkg=tigeR
- `Dataloader(pick=NULL, use_source="Web Server")` — pkg=tigeR
- `dataPreprocess(exp_mtr, Signature=NULL, turn2HL=TRUE, meta=NULL, returnSE=FALSE)` — pkg=tigeR
- `dataPreprocess_SE(SE, Signature=NULL, turn2HL=TRUE)` — pkg=tigeR
- `dataProcess(SE, Signature, rmBE, response_NR, turn2HL)` — pkg=tigeR
- `dataProcess_SE(SE, Signature, rmBE, response_NR, turn2HL)` — pkg=tigeR
- `deconv_TME(SE, method, ...)` — pkg=tigeR
- `diff_biomk(SE, gene, type, method='Average_mean', PT_drop=TRUE, p.pos=c(0.2,0.7), p.round=2, log_sc=TRUE, textcol="black", panelcol="black")` — pkg=tigeR
- `diff_gene(SE)` — pkg=tigeR
- `diff_TME(SE, feature=NULL, style="elegant", group_color=c("#5f96e8CC", "#ee822fCC"))` — pkg=tigeR
- `draw_bar(mtr, feature)` — pkg=tigeR
- `EPIC(SE, sig_matrix=NULL, ...)` — pkg=tigeR
- `ESTIMATE(SE)` — pkg=tigeR
- `extract_label(datasetNames)` — pkg=tigeR
- `extract_mtr(datasetNames)` — pkg=tigeR
- `fpkm2tpm(SE)` — pkg=tigeR
- `fraction_pie(mtr, feature, rows=1, pie_scale=0.9, color="white", label_radius=NULL, label_show_ratio=FALSE, label_threshold=0.04, fontsize=1.5, ...)` — pkg=tigeR
- `gini_gene(SE, length.out=NULL)` — pkg=tigeR
- `Immunotherapy_Response_Batch(SE, geneSet=NULL, method=NULL, PT_drop=TRUE)` — pkg=tigeR
- `integrate_analysis(SE, geneSet=NULL, method=NULL, PT_drop=TRUE)` — pkg=tigeR
- `IPS(SE, project=NULL, plot=FALSE)` — pkg=tigeR
- `ipsmap(x)` — pkg=tigeR
- `IRS_grading(exp_mtr)` — pkg=tigeR
- `load_from_ExperimentHub(pick)` — pkg=tigeR
- `load_from_WebServer(pick)` — pkg=tigeR
- `mapbw(x, my_palette2)` — pkg=tigeR
- `mapcolors(x, my_palette)` — pkg=tigeR
- `max_min_normalization(exp_mtr)` — pkg=tigeR
- `MCPCounter(SE, featuresType="HUGO_symbols", ...)` — pkg=tigeR
- `MCPcounter.estimate(expression, featuresType, probesets, genes)` — pkg=tigeR
- `merge_SE(SE)` — pkg=tigeR
- `pred_response(SE=NULL, exp_mtr=NULL, meta=NULL, threshold=0.8, positive="R", Signature=NULL, method="Average_mean", PT_drop=TRUE, show.val=TRUE, sort_by="rankscore", group_by="rankscore", show.Observed=TRUE, text_col="black", rankscore=TRUE, ZS=TRUE)` — pkg=tigeR
- `quanTIseq(SE, tumor=TRUE, arrays=FALSE, scale_mrna=FALSE, ...)` — pkg=tigeR
- `remove_BE(SE, method)` — pkg=tigeR
- `response_filter(response)` — pkg=tigeR
- `response_prediction(SE=NULL, exp_mtr=NULL, meta=NULL, threshold, positive="R", Signature=NULL, method="Average_mean", PT_drop=TRUE)` — pkg=tigeR
- `response_standardize(V)` — pkg=tigeR
- `roc_biomk(SE, Signature, method=NULL, rmBE=FALSE, response_NR=TRUE, PT_drop=TRUE, auc.pos=c(0.3,0.42), auc.round=3, textcol="black", panelcol="black")` — pkg=tigeR
- `score_biomk(SE=NULL, exp_mtr=NULL, meta=NULL, Signature=NULL, method="Average_mean", PT_drop=TRUE)` — pkg=tigeR
- `score_biomk_SE(SE=NULL, exp_mtr=NULL, meta=NULL, Signature=NULL, method="Average_mean", PT_drop=TRUE)` — pkg=tigeR
- `surv_biomk(SE, gene, method='Average_mean', style='elegant', conf.int=FALSE, val.pos=c(0.03,0.2), lg=NULL, lg.pos=c(0.6,0.9), lg.text="precise", p.round=4, PT_drop=TRUE, drop_zero=FALSE)` — pkg=tigeR
- `surv_styling(df, style, conf.int, gene, method, val.pos, lg, lg.pos, lg.text, p.round)` — pkg=tigeR
- `test_Model(Model, SE=NULL, mtr=NULL, meta=NULL, PT_drop=TRUE)` — pkg=tigeR
- `test_Model.default(Model, SE, PT_drop=TRUE)` — pkg=tigeR
- `test_Model.matrix(mtr, meta, Model)` — pkg=tigeR
- `tGE8_grading(exp_mtr)` — pkg=tigeR
- `TIMER(SE, sig_matrix=NULL, type="SKCM")` — pkg=tigeR
- `TIMER_SE(SE, type="SKCM")` — pkg=tigeR
- `to1(SE, by_row=TRUE)` — pkg=tigeR
- `xCell(SE, signatures=NULL, genes=NULL, spill=NULL, rnaseq=TRUE, file.name=NULL, scale=TRUE, alpha=0.5, save.raw=FALSE, parallel.sz=4, parallel.type='SOCK', cell.types.use=NULL)` — pkg=tigeR

## treeio (1.37.1) — 78 symbols

### Function (77)
- `%<>%(?)` — pkg=treeio
- `%>%(?)` — pkg=treeio
- `.data(?)` — pkg=treeio
- `ancestor(?)` — pkg=treeio
- `as.phylo(x, branch.length, label, ...)` — pkg=treeio
- `as.treedata(tree, boot=NULL, branch.length, label, type="ml", ...)` — pkg=treeio
- `as_tibble(?)` — pkg=treeio
- `child(?)` — pkg=treeio
- `drop.tip(?)` — pkg=treeio
- `edgeNum2nodeNum(jp, edgeNum)` — pkg=treeio
- `find.hclust(x, graph.mst=FALSE, weights=NULL, hclust.method='average', ...)` — pkg=treeio
- `full_join(?)` — pkg=treeio
- `get.data(?)` — pkg=treeio
- `get.fields(?)` — pkg=treeio
- `get.placements(tree, by="best", ...)` — pkg=treeio
- `get.tree(x, ...)` — pkg=treeio
- `get.treetext(?)` — pkg=treeio
- `getNodeNum(tree)` — pkg=treeio
- `inner_join(?)` — pkg=treeio
- `is.ggtree(x)` — pkg=treeio
- `is.rooted(?)` — pkg=treeio
- `isTip(?)` — pkg=treeio
- `label_branch_paml(tree, node, label)` — pkg=treeio
- `mask(tree_object, field, site, mask_site=FALSE)` — pkg=treeio
- `merge_tree(obj1, obj2)` — pkg=treeio
- `MRCA(?)` — pkg=treeio
- `Nnode(edge)` — pkg=treeio
- `Nnode2(tree)` — pkg=treeio
- `nodeid(?)` — pkg=treeio
- `nodelab(?)` — pkg=treeio
- `Ntip(edge)` — pkg=treeio
- `offspring(?)` — pkg=treeio
- `parent(?)` — pkg=treeio
- `raxml2nwk(infile, outfile="raxml.tree")` — pkg=treeio
- `read.astral(file)` — pkg=treeio
- `read.beast(file, threads=1, verbose=FALSE)` — pkg=treeio
- `read.beast.newick(file, threads=1, verbose=FALSE)` — pkg=treeio
- `read.codeml(rstfile, mlcfile, tree="mlc", type="Joint")` — pkg=treeio
- `read.codeml_mlc(mlcfile)` — pkg=treeio
- `read.fasta(fasta, type="auto")` — pkg=treeio
- `read.hyphy(nwk, ancseq, tip.fasfile=NULL)` — pkg=treeio
- `read.hyphy.seq(file)` — pkg=treeio
- `read.iqtree(file)` — pkg=treeio
- `read.jplace(file)` — pkg=treeio
- `read.jtree(file)` — pkg=treeio
- `read.mcmctree(file, force.ultrametric=FALSE)` — pkg=treeio
- `read.mega(?)` — pkg=treeio
- `read.mega_tabular(file)` — pkg=treeio
- `read.mrbayes(file, threads=1, verbose=FALSE)` — pkg=treeio
- `read.newick(file, node.label="label", ...)` — pkg=treeio
- `read.nextstrain.json(x)` — pkg=treeio
- `read.nexus(?)` — pkg=treeio
- `read.nhx(treetext, phylo)` — pkg=treeio
- `read.paml_rst(rstfile, type="Joint")` — pkg=treeio
- `read.phylip(file)` — pkg=treeio
- `read.phylip.seq(file)` — pkg=treeio
- `read.phylip.tree(file)` — pkg=treeio
- `read.phyloxml(file)` — pkg=treeio
- `read.r8s(file)` — pkg=treeio
- `read.raxml(file=NULL, text=NULL)` — pkg=treeio
- `read.tree(?)` — pkg=treeio
- `read.treeqza(treeqza, node.label="label", ...)` — pkg=treeio
- `read.treetime(file)` — pkg=treeio
- `rename_taxa(tree, data, key=1, value=2)` — pkg=treeio
- `rescale_tree(tree_object, branch.length)` — pkg=treeio
- `root(?)` — pkg=treeio
- `rootnode(?)` — pkg=treeio
- `rtree(?)` — pkg=treeio
- `spt(x, from, to, weights=NULL, ...)` — pkg=treeio
- `tibble(?)` — pkg=treeio
- `treedata(?)` — pkg=treeio
- `write.beast(treedata, file="", append=FALSE, digits=10, tree.prefix="")` — pkg=treeio
- `write.beast.newick(treedata, file="", append=FALSE, digits=10, tree.prefix="")` — pkg=treeio
- `write.jplace(x, outfile)` — pkg=treeio
- `write.jtree(treedata, file="")` — pkg=treeio
- `write.nexus(?)` — pkg=treeio
- `write.tree(?)` — pkg=treeio

### Generic (1)
- `print(x, ...)` — pkg=treeio

## wikiprofiler (0.1.7) — 9 symbols

### Function (9)
- `ggsave(?)` — pkg=wikiprofiler
- `read.wp(file)` — pkg=wikiprofiler
- `wp_bgfill(p, value, high="red", low="blue", legend=TRUE, legend_x=0.001, legend_y=0.94)` — pkg=wikiprofiler
- `wp_comparefill(p, value, control, mode=c("difference", "log2_ratio"), pseudocount=1, high="red", low="blue", legend=TRUE, legend_x=0.001, legend_y=0.94)` — pkg=wikiprofiler
- `wp_map(data, value_col=NULL, symbol_col=NULL, id_col=NULL, mapping=NULL, mapping_from=NULL, mapping_to=NULL, aggregator=c("mean", "median", "max_abs", "first..., na.rm=TRUE)` — pkg=wikiprofiler
- `wp_render(pathway, value=NULL, control=NULL, n=NULL, id_col="ID", name_col=NULL, dir=NULL, file_ext="png", filename_template="{id}", width=NULL, height=NULL, shadowtext=FALSE, bg.r=2, bg.col="white", mode=c("difference", "log2_ratio"), pseudocount=1, high="red", low="blue", legend=TRUE, legend_x=0.001, legend_y=0.94)` — pkg=wikiprofiler
- `wp_shadowtext(p, bg.r=2, bg.col="white")` — pkg=wikiprofiler
- `wpplot(ID)` — pkg=wikiprofiler
- `wpsave(p, file, width=NULL, height=NULL, ...)` — pkg=wikiprofiler

## yulab.utils (?) — 0 symbols
