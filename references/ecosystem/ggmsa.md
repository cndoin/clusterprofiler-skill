# ggmsa — 1.19.2

> 数据源：YuLab-SMU/ggmsa @ devel
> 122 个已知符号

## Function (30)

- `adjust_ally(tree, node, sub=FALSE, seq_colname="mol_seq")`
- `assign_dms(x, dms)`
- `available_colors(?)`
- `available_fonts(?)`
- `available_msa(?)`
- `extract_seq(tree_adjust, seq_colname="mol_seq")`
- `facet_msa(field)`
- `geom_GC(show.legend=FALSE)`
- `geom_helix(helix_data, color_by="length", overlap=FALSE, ...)`
- `geom_msa(data, font="helvetical", mapping=NULL, color="Chemistry_AA", custom_color=NULL, char_width=0.9, none_bg=FALSE, by_conservation=FALSE, position_highlight=NULL, seq_name=NULL, border=NULL, consensus_views=FALSE, use_dot=FALSE, disagreement=TRUE, ignore_gaps=FALSE, ref=NULL, position="identity", show.legend=FALSE, dms=FALSE, position_color=FALSE, ...)`
- `geom_msaBar(?)`
- `geom_seed(seed, star=FALSE)`
- `geom_seqlogo(font="DroidSansMono", color="Chemistry_AA", adaptive=TRUE, top=TRUE, custom_color=NULL, show.legend=FALSE, ...)`
- `gghelix(helix_data, color_by="length", overlap=FALSE)`
- `ggmaf(data, ref, block_start=NULL, block_end=NULL, facet_field=NULL, heights=c(0.4,0.6), facet_heights=NULL)`
- `ggmsa(msa, start=NULL, end=NULL, font="helvetical", color="Chemistry_AA", custom_color=NULL, char_width=0.9, none_bg=FALSE, by_conservation=FALSE, position_highlight=NULL, seq_name=NULL, border=NULL, consensus_views=FALSE, use_dot=FALSE, disagreement=TRUE, ignore_gaps=FALSE, ref=NULL, show.legend=FALSE)`
- `ggSeqBundle(msa, line_width=0.3, line_thickness=0.3, line_high=0, spline_shape=0.3, size=0.5, alpha=0.2, bundle_color=c("#2ba0f5","#424242"), lev_molecule=c("-", "A", "V", "L", "I", "P", "F", ...)`
- `merge_seq(previous_seq, gap, subsequent_seq, adjust_name=TRUE)`
- `read_maf(multiple_alignment_format)`
- `readSSfile(file, type=NULL)`
- `reset_pos(seq_df)`
- `seqdiff(fasta, reference=1)`
- `seqlogo(msa, start=NULL, end=NULL, font="DroidSansMono", color="Chemistry_AA", adaptive=FALSE, top=FALSE, custom_color=NULL)`
- `simplify_hdata(hdata, sim_msa)`
- `simplot(file, query, window=200, step=20, group=FALSE, id, sep, sd=FALSE, smooth=FALSE, smooth_params=list(method = "loess", se = FALSE))`
- `theme_msa(?)`
- `tidy_hdata(gap, inter, previous_seq, subsequent_seq)`
- `tidy_maf_df(maf_df, ref)`
- `tidy_msa(msa, start=NULL, end=NULL)`
- `treeMSA_plot(p_tree, tidymsa_df, ancestral_node="none", sub=FALSE, panel="MSA", font=NULL, color="Chemistry_AA", seq_colname=NULL, ...)`

## Generic (1)

- `diff(x, ...)`

## S4method (1)

- `plot(?)`

## Reexport (90)

- `%<>%(lhs, rhs)`
- `%>%(lhs, rhs)`
- `AAStringSet(?)`
- `aes(x, y)`
- `aes_(?)`
- `arrow(?)`
- `as.helix(?)`
- `as.patchwork(?)`
- `brewer.pal(?)`
- `collapseHelix(?)`
- `colorRampPalette(?)`
- `coord_cartesian(?)`
- `coord_fixed(?)`
- `DNAStringSet(?)`
- `draw_key_polygon(?)`
- `element_blank(?)`
- `element_line(?)`
- `element_text(?)`
- `expandHelix(?)`
- `fa_read(?)`
- `facet_wrap(?)`
- `gather(?)`
- `Geom(?)`
- `geom_arc(?)`
- `geom_area(?)`
- `geom_blank(?)`
- `geom_col(?)`
- `geom_facet(?)`
- `geom_line(?)`
- `geom_point(?)`
- `geom_polygon(?)`
- `geom_ribbon(?)`
- `geom_segment(?)`
- `geom_smooth(?)`
- `geom_text(?)`
- `geom_tile(?)`
- `geom_tiplab(?)`
- `geom_xspline(?)`
- `getFromNamespace(?)`
- `ggplot(data, mapping)`
- `ggplot_add(object, plot, ...)`
- `ggplot_build(?)`
- `ggplot_gtable(?)`
- `ggproto(?)`
- `ggtitle(?)`
- `globalVariables(?)`
- `gpar(?)`
- `group_by(?)`
- `group_by_(?)`
- `gTree(?)`
- `insert_top(?)`
- `labs(?)`
- `layer(?)`
- `missingArg(?)`
- `modifyList(?)`
- `n(?)`
- `new(?)`
- `packageDescription(?)`
- `plot_list(?)`
- `polygonGrob(?)`
- `read.delim(?)`
- `readBpseq(?)`
- `readBStringSet(?)`
- `readConnect(?)`
- `readDNAStringSet(?)`
- `readHelix(?)`
- `readVienna(?)`
- `RNAStringSet(?)`
- `scale_color_manual(values)`
- `scale_fill_gradientn(?)`
- `scale_fill_manual(?)`
- `scale_x_continuous(?)`
- `scale_y_continuous(?)`
- `select(?)`
- `setNames(?)`
- `show(?)`
- `summarize(?)`
- `summarize_(?)`
- `theme(?)`
- `theme_bw(?)`
