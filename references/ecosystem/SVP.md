# SVP — 1.5.1

> 数据源：github.com/YuLab-SMU/SVP@devel
> 49 个已知符号

## Function (47)

- `as_tbl_df(x, listn=NULL, diag=TRUE, rmrd=TRUE, flag.clust=FALSE, dist.method='euclidean', hclust.method='average')`
- `cal_lisa_f1(data, lisa.res, type='High', group.by, rm.group.nm=NULL, ...)`
- `cluster.assign(?)`
- `extract_weight_adj(?)`
- `fast_cor(x, y=NULL, combine=FALSE, method=c('pearson', 'spearman', 'bicorr'), alternative=c("two.sided", "less", "greater"), add.pvalue=FALSE, p.adjust.method='BH')`
- `fscoreDf(?)`
- `fscoreDf<-(?)`
- `fscoreDfNames(?)`
- `fscoreDfNames<-(?)`
- `fscoreDfs(x)`
- `fscoreDfs<-(?)`
- `gsvaExp(?)`
- `gsvaExp<-(?)`
- `gsvaExpNames(?)`
- `gsvaExpNames<-(?)`
- `gsvaExps(?)`
- `gsvaExps<-(?)`
- `imgData(?)`
- `imgData<-(?)`
- `LISAResult(x, type=NULL, features=NULL, ...)`
- `LISAsce(data, lisa.res, gsvaexp.name="LISA", ...)`
- `mainGsvaExpName(x)`
- `mainGsvaExpName<-(?)`
- `plot_heatmap_globalbv(globalbv, moran.t=NULL, moran.l=NULL, lisa.t=NULL, lisa.l=NULL, max.point.size=4.5, font.size=2.5, limits.size=NULL, limits.colour=NULL, dist.method="euclidean", hclust.method="average", threshold=0.05)`
- `pred.cell.signature(?)`
- `runCORR(data, features1=NULL, features2=NULL, assay.type="logcounts", method=c("spearman", "pearson", "bicorr")`
- `runDetectMarker(?)`
- `runDetectSVG(?)`
- `runENCODE(data, group.by, rm.group.nm=NULL, ...)`
- `runGLOBALBV(data, features1=NULL, features2=NULL, assay.type="logcounts", sample_id='all', method=c("lee")`
- `runKldSVG(?)`
- `runLISA(data, features, assay.type="logcounts", sample_id='all', method=c("localG", "localmoran")`
- `runLOCALBV(data, features1=NULL, features2=NULL, assay.type="logcounts", sample_id='all', bv.method=c("locallee", "localmoran")`
- `runMCA(?)`
- `runSGSA(?)`
- `runWKDE(?)`
- `spatialCoords(?)`
- `spatialCoords<-(?)`
- `spatialCoordsNames(?)`
- `spatialCoordsNames<-(?)`
- `svDf(?)`
- `svDf<-(?)`
- `svDfNames(?)`
- `svDfNames<-(?)`
- `svDfs(x)`
- `svDfs<-(?)`
- `SVPExperiment(..., gsvaExps=list())`

## S4method (2)

- `coerce(?)`
- `show(?)`
