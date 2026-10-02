# wikiprofiler — 0.1.7

> 数据源：YuLab-SMU/wikiprofiler @ master
> 13 个已知符号

## Function (8)

- `read.wp(file)`
- `wp_bgfill(p, value, high="red", low="blue", legend=TRUE, legend_x=0.001, legend_y=0.94)`
- `wp_comparefill(p, value, control, mode=c("difference", "log2_ratio"), pseudocount=1, high="red", low="blue", legend=TRUE, legend_x=0.001, legend_y=0.94)`
- `wp_map(data, value_col=NULL, symbol_col=NULL, id_col=NULL, mapping=NULL, mapping_from=NULL, mapping_to=NULL, aggregator=c("mean", "median", "max_abs", "first..., na.rm=TRUE)`
- `wp_render(pathway, value=NULL, control=NULL, n=NULL, id_col="ID", name_col=NULL, dir=NULL, file_ext="png", filename_template="{id}", width=NULL, height=NULL, shadowtext=FALSE, bg.r=2, bg.col="white", mode=c("difference", "log2_ratio"), pseudocount=1, high="red", low="blue", legend=TRUE, legend_x=0.001, legend_y=0.94)`
- `wp_shadowtext(p, bg.r=2, bg.col="white")`
- `wpplot(ID)`
- `wpsave(p, file, width=NULL, height=NULL, ...)`

## Reexport (5)

- `as.grob(?)`
- `ggsave(?)`
- `grid.draw(?)`
- `rasterGrob(?)`
- `read.gmt.wp(gmtfile)`
