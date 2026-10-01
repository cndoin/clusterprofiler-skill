# ggtree — 4.3.1

> 数据源：github.com/YuLab-SMU/ggtree@devel
> 139 个已知符号

## Function (137)

- `%+>%(?)`
- `%<%(?)`
- `%<+%(?)`
- `%>%(?)`
- `add_colorbar(p, color, x=NULL, ymin=NULL, ymax=NULL, font.size=4)`
- `aes(?)`
- `arrow(?)`
- `as.polytomy(tree, feature, fun)`
- `as_tanglegram(x, y=NULL, assoc=NULL, layout="rectangular", ladderize=TRUE, preserve_layers=TRUE, ...)`
- `as_tanglegram.cophylo(x, ..., layout="rectangular", ladderize=TRUE, preserve_layers=TRUE)`
- `as_tanglegram.default(x, y=NULL, assoc=NULL, layout="rectangular", ladderize=TRUE, preserve_layers=TRUE, ...)`
- `as_tanglegram.tanglegram(x, ...)`
- `collapse(x=NULL, node, mode="none", clade_name=NULL, height=NULL, ...)`
- `Date2decimal(x)`
- `decimal2Date(x)`
- `expand(tree_view=NULL, node)`
- `facet_data(tree_view, panel)`
- `facet_labeller(p, label)`
- `facet_plot(p, mapping=NULL, data, geom, panel, ...)`
- `facet_widths(p, widths)`
- `flip(tree_view=NULL, node1, node2)`
- `fortify(model, data, layout="rectangular", ladderize=TRUE, right=FALSE, branch.length="branch.length", mrsd=NULL, as.Date=FALSE, yscale="none", root.position=0, hang=.1, gap=0.08, mirror=TRUE, optimize=isTRUE(model$params$optimize), optimize_side=model$params$optimize_side %||% "right", ...)`
- `geom_aline(mapping=NULL, linetype="dotted", linewidth=1, ...)`
- `geom_balance(node, fill="steelblue", color='white', alpha=.5, extend=0, extendto=NULL)`
- `geom_cladelab(node=NULL, label=NULL, data=NULL, mapping=NULL, geom="text", parse=FALSE, ...)`
- `geom_cladelabel(node, label, offset=0, offset.text=0, extend=0, align=FALSE, barsize=0.5, fontsize=3.88, angle=0, geom="text", hjust=0, color=NULL, fill=NA, family="sans", parse=FALSE, horizontal=TRUE, ...)`
- `geom_cladelabel2(node, label, offset=0, offset.text=0, offset.bar=0, align=FALSE, barsize=0.5, fontsize=3.88, hjust=0, geom="text", color=NULL, family="sans", parse=FALSE, horizontal=TRUE, ...)`
- `geom_facet(mapping=NULL, data, geom, panel, ...)`
- `geom_highlight(data=NULL, mapping=NULL, node=NULL, type="auto", to.bottom=FALSE, ...)`
- `geom_hilight(data=NULL, mapping=NULL, node=NULL, type="auto", to.bottom=FALSE, ...)`
- `geom_inset(insets, width=.1, height=.1, hjust=0, vjust=0, x="node", reverse_x=FALSE, reverse_y=FALSE)`
- `geom_label(?)`
- `geom_label2(mapping=NULL, data=NULL, ..., stat="identity", position="identity", family="sans", parse=FALSE, nudge_x=0, nudge_y=0, label.padding=unit(0.25, "lines"), label.r=unit(0.15, "lines"), label.size=0.25, na.rm=TRUE, show.legend=NA, inherit.aes=TRUE)`
- `geom_label2_interactive(...)`
- `geom_motif(mapping, data, on, label, align='centre', ...)`
- `geom_nodelab(mapping=NULL, nudge_x=0, nudge_y=0, geom="text", hjust=0.5, node="internal", ...)`
- `geom_nodelab2(mapping=NULL, nudge_x=0, nudge_y=0, geom="text", hjust=0.5, ...)`
- `geom_nodepoint(mapping=NULL, data=NULL, position="identity", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, ...)`
- `geom_point(?)`
- `geom_point2(mapping=NULL, data=NULL, stat="identity", position="identity", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, ...)`
- `geom_point2_interactive(...)`
- `geom_range(range, center="auto", ...)`
- `geom_rootedge(rootedge=NULL, data=NULL, ...)`
- `geom_rootpoint(mapping=NULL, data=NULL, position="identity", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, ...)`
- `geom_segment2(mapping=NULL, data=NULL, stat="identity", position="identity", lineend="butt", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, nudge_x=0, arrow=NULL, arrow.fill=NULL, ...)`
- `geom_segment2_interactive(...)`
- `geom_strip(taxa1, taxa2, label, offset=0, offset.text=0, align=TRUE, barsize=0.5, extend=0, fontsize=3.88, angle=0, geom="text", hjust=0, color='black', fill=NA, family="sans", parse=FALSE, ...)`
- `geom_striplab(taxa1=NULL, taxa2=NULL, label=NULL, data=NULL, mapping=NULL, geom="text", parse=FALSE, ...)`
- `geom_tanglelink(data=NULL, mapping=NULL, left=NULL, right=NULL, geom=c("curve", "segment"), curvature=0.15, ...)`
- `geom_taxalink(data=NULL, mapping=NULL, taxa1=NULL, taxa2=NULL, offset=NULL, outward="auto", ...)`
- `geom_text(?)`
- `geom_text2(mapping=NULL, data=NULL, ..., stat="identity", position="identity", family="sans", parse=FALSE, na.rm=TRUE, show.legend=NA, inherit.aes=TRUE, nudge_x=0, nudge_y=0, check_overlap=FALSE)`
- `geom_text2_interactive(...)`
- `geom_tiplab(mapping=NULL, hjust=0, align=FALSE, linetype="dotted", linesize=0.5, geom="text", offset=0, as_ylab=FALSE, ...)`
- `geom_tiplab2(mapping=NULL, hjust=0, ...)`
- `geom_tippoint(mapping=NULL, data=NULL, position="identity", na.rm=FALSE, show.legend=NA, inherit.aes=TRUE, ...)`
- `geom_tree(mapping=NULL, data=NULL, layout="rectangular", multiPhylo=FALSE, continuous="none", position="identity", ...)`
- `geom_tree2(layout="rectangular", ...)`
- `geom_treescale(x=NULL, y=NULL, width=NULL, offset=NULL, offset.label=NULL, label=NULL, color="black", linesize=0.5, fontsize=3.88, family="sans")`
- `geom_zoom_clade(node, xexpand=NULL)`
- `GeomHilightEncircle(?)`
- `GeomInteractiveCurvelink(?)`
- `GeomInteractiveHilightEncircle(?)`
- `GeomInteractiveHilightRect(?)`
- `GeomInteractiveLabelGGtree(?)`
- `GeomInteractivePointGGtree(?)`
- `GeomInteractiveSegmentGGtree(?)`
- `GeomInteractiveTextGGtree(?)`
- `get.path(phylo, from, to)`
- `get_clade_position(treeview, node)`
- `get_heatmap_column_position(treeview, by="bottom")`
- `get_taxa_name(tree_view=NULL, node=NULL)`
- `ggdensitree(data=NULL, mapping=NULL, layout="slanted", tip.order='mode', align.tips=TRUE, jitter=0, ...)`
- `ggdoubletree(x, y=NULL, assoc=NULL, layout="rectangular", ladderize=TRUE, mirror=TRUE, optimize=FALSE, optimize_side=c("right", "both", "left"), gap=0.08, preserve_layers=TRUE, ...)`
- `ggexpand(ratio, direction=1, side='hv')`
- `ggplot(?)`
- `ggsave(?)`
- `ggtree(tr, mapping=NULL, layout="rectangular", open.angle=0, mrsd=NULL, as.Date=FALSE, yscale="none", yscale_mapping=NULL, ladderize=TRUE, right=FALSE, branch.length="branch.length", root.position=0, xlim=NULL, layout.params=list(as.graph = TRUE), hang=.1, ...)`
- `ggtree_set_interactive(?)`
- `ggtree_unset_interactive(?)`

## Generic (2)

- `ggplot_add(object, plot, object_name, ...)`
- `offspring(.data, .node, tiponly=FALSE, self_include=FALSE, ...)`
