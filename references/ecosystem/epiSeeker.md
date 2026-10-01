# epiSeeker — 1.1.2

> 数据源：github.com/YuLab-SMU/epiSeeker@devel
> 49 个已知符号

## Function (41)

- `.(..., .env=parent.frame())`
- `annotateSeq(peak, tssRegion=c(-3000, 3000), TxDb=NULL, level="transcript", assignGenomicAnnotation=TRUE, genomicAnnotationPriority=c("Promoter", "5UTR", "3UTR", "Exon",..., annoDb=NULL, addFlankGeneInfo=FALSE, flankDistance=5000, sameStrand=FALSE, ignoreOverlap=FALSE, ignoreUpstream=FALSE, ignoreDownstream=FALSE, overlap="TSS", verbose=TRUE, columns=c("ENTREZID", "ENSEMBL", "SYMBOL", "G...)`
- `as.GRanges(x)`
- `bmData(value1=NULL, value2=NULL, pos=NULL, chr=NULL, gr=NULL, sampleNames=NULL, valueNames=NULL, ...)`
- `combine_csAnno(x, ...)`
- `downloadGEObedFiles(genome, destDir=getwd())`
- `downloadGSMbedFiles(GSM, destDir=getwd())`
- `dropAnno(csAnno, distanceToTSS_cutoff=10000)`
- `enrichAnnoOverlap(queryPeak, targetPeak, TxDb=NULL, pAdjustMethod="BH", chainFile=NULL, distanceToTSS_cutoff=NULL)`
- `enrichPeakOverlap(queryPeak, targetPeak, TxDb=NULL, pAdjustMethod="BH", nShuffle=1000, chainFile=NULL, pool=TRUE, mc.cores=detectCores() - 1, verbose=TRUE)`
- `getAnnoStat(x)`
- `getBioRegion(TxDb=NULL, upstream=1000, downstream=1000, by="gene", type="start_site")`
- `getBmMatrix(region, input, BSgenome, cover_depth=TRUE, base=NULL, motif=NULL, position_bias=NULL)`
- `getGEOgenomeVersion(?)`
- `getGEOInfo(genome, simplify=TRUE)`
- `getGEOspecies(?)`
- `getMotifMatrix(region, pwm, ref_obj, by="name")`
- `getPromoters(TxDb=NULL, upstream=1000, downstream=1000, by="gene")`
- `getSampleFiles(?)`
- `getTagMatrix(peak, upstream=0, downstream=0, windows=NULL, type=NULL, by=NULL, TxDb=NULL, weightCol=NULL, nbin=NULL, verbose=TRUE, ignore_strand=FALSE)`
- `grange2mt(gr_list, weightCol=NULL)`
- `makeBmDataFromData(data, sampleNames=NULL)`
- `makeBmDataFromFiles(name, sampleNames=NULL, variablesNames=NULL)`
- `parse_peak(peak_str)`
- `plotAnnoBar(x, xlab="", ylab="Percentage(%)`
- `plotAnnoPie(x, ndigit=2, cex=0.8, col=NA, legend.position="rightside", pie3D=FALSE, radius=0.8, ...)`
- `plotAnnoPie.csAnno(x, ndigit=2, cex=0.8, col=NA, legend.position="rightside", pie3D=FALSE, radius=0.8, ...)`
- `plotBmProf(df, motif_color=NULL, title=NULL, xlim=NULL, interactive=FALSE, width_svg=10, height_svg=6, highlight=NULL, highlight_color="#c6c3c3", highlight_alpha=0.2, xlab="Genomic Region(5'->3')", ylab=NULL, second_ylab=NULL, switch_y_value=TRUE, legend_lab_motif=NULL, legend_lab_value2=NULL, strip_placement="outside", angle_of_facet_label=360, alpha=0.6, y_ticks_length=0.25, x_ticks_length=0.25, auto_x_axis=TRUE, strip_border=FALSE, facet_label_text_size=10, axis_title_text_size=17, title_text_size=20, right_y_axis_text_size=10, left_y_axis_text_size=10, x_axis_text_size=10, depth_heatmap=TRUE, nrow=NULL, ncol=NULL, panel_spacing=1, legend_box_spacing=3, legend_position="right")`
- `plotCov(peak, weightCol=NULL, facet_level=NULL, highlight=NULL, highlight_color="#c6c3c3", highlight_alpha=0.2, xlab="Chromosome Size (bp)", ylab="", interactive=FALSE, width_svg=10, height_svg=6, title="ChIP Peaks over Chromosomes", x_text_size=10, y_text_size=10, facet_label_text_size=10, chrs=NULL, xlim=NULL, facet_var=NULL, facet_scales="free", lower=1, fill_color="black", add_cluster_tree=FALSE, cluster_dist_method="euclidean", cluster_hclust_methond="complete", legend_position=NULL, add_coaccess=FALSE, curvature=0.3, coaccess_top_n=NULL, coaccess_cor_threshold=NULL, design=NULL, coaccess_legend_pos=c(0.9, 0.5), coaccess_legend_text_size=10, coaccess_legend_title_size=12)`
- `plotDistToTSS(x, distanceColumn="distanceToTSS", xlab="", ylab="Binding sites (%)`
- `plotGeneTrack(txdb, chr, start_pos, end_pos, xlab="", ylab="", x_text_size=10, y_text_size=10, select_gene="all", palette=NULL, fromType="ENTREZID", highlight=NULL, highlight_color="#c6c3c3", highlight_alpha=0.2, OrgDb=NULL, show_legend=FALSE, auto_x_axis=TRUE)`
- `plotMotifProf(df, legend_lab="motif", y_lab="motif score", x_lab=NULL, interactive=FALSE, width_svg=10, height_svg=6)`
- `plotPeakHeatmap(tagMatrix, plot_prof=TRUE, xlab="", ylab="", palette=NULL, title=NULL, facet_label_text_size=12, nrow=NULL, ncol=NULL, conf=NULL, statistic_method="mean", missingDataAsZero=TRUE, facet="none", free_y=TRUE, height_proportion=4, ...)`
- `plotPeakProf(tagMatrix, xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", conf=NULL, title="", facet="none", free_y=TRUE, statistic_method="mean", missingDataAsZero=TRUE, ...)`
- `readPeakFile(peakfile, as="GRanges", ...)`
- `rel(?)`
- `seq2gene(seq, tssRegion, flankDistance, TxDb, sameStrand=FALSE)`
- `shuffle(peak.gr, TxDb)`
- `vennpie(x, r=0.2, cex=1.2, col=NULL)`
- `vennplot(Sets, ...)`
- `vennplot.peakfile(files, labels=NULL)`

## Generic (6)

- `arrange(.data, .by_group=FALSE, ...)`
- `as.data.frame(x, row.names=NULL, optional=FALSE, ...)`
- `filter(.data, .by=NULL, .preserve=FALSE, ...)`
- `mutate(.data, .by=NULL, .keep=c("all", "used", "unused", "none"), .before=NULL, .after=NULL, ...)`
- `rename(.data, ...)`
- `subset(x, subset, ...)`

## S4method (2)

- `show(?)`
- `upsetplot(?)`
