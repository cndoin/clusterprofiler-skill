# SVP — 1.5.1

> 数据源：YuLab-SMU/SVP @ devel
> 120 个已知符号

## Function (31)

- `as_tbl_df(x, listn=NULL, diag=TRUE, rmrd=TRUE, flag.clust=FALSE, dist.method='euclidean', hclust.method='average')`
- `cal_lisa_f1(data, lisa.res, type='High', group.by, rm.group.nm=NULL, ...)`
- `cluster.assign(?)`
- `extract_weight_adj(?)`
- `fast_cor(x, y=NULL, combine=FALSE, method=c('pearson', 'spearman', 'bicorr'), alternative=c("two.sided", "less", "greater"), add.pvalue=FALSE, p.adjust.method='BH')`
- `fscoreDf(?)`
- `fscoreDfNames(?)`
- `fscoreDfs(x)`
- `gsvaExp(?)`
- `gsvaExpNames(?)`
- `gsvaExps(?)`
- `LISAResult(x, type=NULL, features=NULL, ...)`
- `LISAsce(data, lisa.res, gsvaexp.name="LISA", ...)`
- `mainGsvaExpName(x)`
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
- `svDf(?)`
- `svDfNames(?)`
- `svDfs(x)`
- `SVPExperiment(..., gsvaExps=list())`

## S4method (1)

- `coerce(?)`

## Reexport (88)

- `%fin%(?)`
- `.data(?)`
- `aes(x, y)`
- `as(?)`
- `assay(?)`
- `assayNames(?)`
- `bplapply(?)`
- `callNextMethod(?)`
- `case_when(?)`
- `cli_abort(?)`
- `colData(?)`
- `combn(?)`
- `coolcat(?)`
- `coord_cartesian(?)`
- `DataFrame(?)`
- `deldir(?)`
- `dist(?)`
- `element_blank(?)`
- `element_line(?)`
- `element_text(?)`
- `endoapply(?)`
- `evalCpp(?)`
- `expansion(?)`
- `findKNN(?)`
- `geom_col(?)`
- `geom_star(?)`
- `geom_text(?)`
- `geom_tile(?)`
- `ggplot(data, mapping)`
- `ggtree(?)`
- `guide_axis(?)`
- `guide_colorbar(?)`
- `guide_legend(?)`
- `guides(?)`
- `hclust(?)`
- `imgData(?)`
- `initialize(?)`
- `int_colData(?)`
- `int_elementMetadata(?)`
- `int_metadata(?)`
- `is(?)`
- `isEmpty(?)`
- `layout_dendrogram(?)`
- `List(?)`
- `margin(?)`
- `Matrix(?)`
- `mcols(?)`
- `metadata(?)`
- `new(?)`
- `p.adjust(?)`
- `phyper(?)`
- `pnorm(?)`
- `pt(?)`
- `RcppParallelLibs(?)`
- `reducedDim(?)`
- `reducedDimNames(?)`
- `reducedDims(?)`
- `rowData(?)`
- `rowVars(?)`
- `scale_fill_gradient2(?)`
- `scale_size_continuous(?)`
- `scale_starshape_manual(?)`
- `scale_x_reverse(?)`
- `scale_y_continuous(?)`
- `SerialParam(?)`
- `setClass(?)`
- `setClassUnion(?)`
- `setNames(?)`
- `show(?)`
- `SimpleList(?)`
- `SingleCellExperiment(?)`
- `sourceCpp(?)`
- `sparseMatrix(?)`
- `spatialCoords(?)`
- `spatialCoordsNames(?)`
- `SpatialExperiment(?)`
- `sym(?)`
- `td_filter(?)`
- `theme(?)`
- `theme_blinds(?)`
