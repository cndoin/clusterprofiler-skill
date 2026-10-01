# ChIPseeker — 1.49.2

> 数据源：github.com/YuLab-SMU/ChIPseeker@devel
> 48 个已知符号

## Function (40)

- `.(..., .env=parent.frame())`
- `annotatePeak(peak, tssRegion=c(-3000, 3000), TxDb=NULL, level="transcript", assignGenomicAnnotation=TRUE, genomicAnnotationPriority=c("Promoter", "5UTR", "3UTR", "Exon",..., annoDb=NULL, addFlankGeneInfo=FALSE, flankDistance=5000, sameStrand=FALSE, ignoreOverlap=FALSE, ignoreUpstream=FALSE, ignoreDownstream=FALSE, overlap="TSS", verbose=TRUE, columns=c("ENTREZID", "ENSEMBL", "SYMBOL", "G...)`
- `as.GRanges(x)`
- `combine_csAnno(x, ...)`
- `covplot(peak, weightCol=NULL, xlab="Chromosome Size (bp)", ylab="", title="ChIP Peaks over Chromosomes", chrs=NULL, xlim=NULL, lower=1, fill_color="black")`
- `downloadGEObedFiles(genome, destDir=getwd())`
- `downloadGSMbedFiles(GSM, destDir=getwd())`
- `dropAnno(csAnno, distanceToTSS_cutoff=10000)`
- `enrichAnnoOverlap(queryPeak, targetPeak, TxDb=NULL, pAdjustMethod="BH", chainFile=NULL, distanceToTSS_cutoff=NULL)`
- `enrichPeakOverlap(queryPeak, targetPeak, TxDb=NULL, pAdjustMethod="BH", nShuffle=1000, chainFile=NULL, pool=TRUE, mc.cores=detectCores()-1, verbose=TRUE)`
- `getAnnoStat(x)`
- `getBioRegion(TxDb=NULL, upstream=1000, downstream=1000, by="gene", type="start_site")`
- `getGEOgenomeVersion(?)`
- `getGEOInfo(genome, simplify=TRUE)`
- `getGEOspecies(?)`
- `getPromoters(TxDb=NULL, upstream=1000, downstream=1000, by="gene")`
- `getSampleFiles(?)`
- `getTagMatrix(peak, upstream, downstream, windows, type, by, TxDb=NULL, weightCol=NULL, nbin=NULL, verbose=TRUE, ignore_strand=FALSE)`
- `GRangesList(?)`
- `makeBioRegionFromGranges(gr, by, type, upstream=1000, downstream=1000)`
- `overlap(Sets)`
- `peak_Profile_Heatmap(peak, weightCol=NULL, TxDb=NULL, upstream=1000, downstream=1000, xlab="", ylab="", title=NULL, palette=NULL, verbose=TRUE, by="gene", type="start_site", nbin=NULL, ignore_strand=FALSE, windows_name=NULL, ncol=NULL, nrow=NULL, facet_label_text_size=12, conf, facet="row", free_y=TRUE, height_proportion=4)`
- `peakHeatmap(peak, weightCol=NULL, TxDb=NULL, upstream=1000, downstream=1000, xlab="", ylab="", title=NULL, palette=NULL, verbose=TRUE, by="gene", type="start_site", nbin=NULL, ignore_strand=FALSE, windows, ncol=NULL, nrow=NULL)`
- `peakHeatmap_multiple_Sets(peak, weightCol=NULL, TxDb=NULL, upstream=1000, downstream=1000, xlab="", ylab="", title=NULL, palette=NULL, verbose=TRUE, by="gene", type="start_site", nbin=NULL, ignore_strand=FALSE, windows_name=NULL, ncol=NULL, nrow=NULL, facet_label_text_size=12)`
- `plotAnnoBar(x, xlab="", ylab='Percentage(%)`
- `plotAnnoPie(x, ndigit=2, cex=0.8, col=NA, legend.position="rightside", pie3D=FALSE, radius=0.8, ...)`
- `plotAnnoPie.csAnno(x, ndigit=2, cex=0.8, col=NA, legend.position="rightside", pie3D=FALSE, radius=0.8, ...)`
- `plotAvgProf(tagMatrix, conf, xlim=c(-3000,3000), xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", facet="none", free_y=TRUE, origin_label, upstream=NULL, downstream=NULL, label, ...)`
- `plotAvgProf2(peak, weightCol=NULL, TxDb=NULL, upstream=1000, downstream=1000, xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", conf, facet="none", free_y=TRUE, verbose=TRUE, ignore_strand=FALSE, ...)`
- `plotDistToTSS(x, distanceColumn="distanceToTSS", xlab="", ylab="Binding sites (%)`
- `plotPeakProf(tagMatrix=NULL, peak, upstream, downstream, conf, by, type, windows_name=NULL, weightCol=NULL, TxDb=NULL, xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", facet="row", free_y=TRUE, verbose=TRUE, nbin=NULL, ignore_strand=FALSE, ...)`
- `plotPeakProf2(peak, upstream, downstream, conf, by, type, weightCol=NULL, TxDb=NULL, xlab="Genomic Region (5'->3')", ylab="Peak Count Frequency", facet="none", free_y=TRUE, verbose=TRUE, nbin=NULL, ignore_strand=FALSE, ...)`
- `readPeakFile(peakfile, as="GRanges", ...)`
- `rel(?)`
- `seq2gene(seq, tssRegion, flankDistance, TxDb, sameStrand=FALSE)`
- `shuffle(peak.gr, TxDb)`
- `tagHeatmap(tagMatrix, xlab="", ylab="", title=NULL, palette="RdBu", nrow=NULL, ncol=NULL)`
- `vennpie(x, r=0.2, cex=1.2, col=NULL)`
- `vennplot(Sets, by="gplots", ...)`
- `vennplot.peakfile(files, labels=NULL)`

## Generic (6)

- `arrange(.data, .by_group=FALSE, ...)`
- `as.data.frame(x, row.names=NULL, optional=FALSE, ...)`
- `filter(.data, .by=NULL, .preserve=FALSE, ...)`
- `mutate(.data, .by=NULL, .keep=c("all", "used", "unused", "none"), .before=NULL, .after=NULL, ...)`
- `rename(x, ...)`
- `subset(x, ...)`

## S4method (2)

- `show(?)`
- `upsetplot(?)`
