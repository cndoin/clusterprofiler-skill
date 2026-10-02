# tidytree — 0.4.8

> 数据源：YuLab-SMU/tidytree @ master
> 76 个已知符号

## Function (25)

- `ancestor(.data, .node, ...)`
- `as.treedata(tree, ...)`
- `as.ultrametric(tree, ...)`
- `child(.data, .node, type='children', ...)`
- `drop.tip(object, tip, ...)`
- `get.data(object)`
- `get.fields(object)`
- `get.treetext(object)`
- `get_tree_data(tree_object)`
- `getNodeNum(tree)`
- `groupClade(.data, .node, group_name='group', overlap='overwrite', ...)`
- `groupOTU(.data, .node, group_name='group', ...)`
- `isTip(.data, .node, ...)`
- `keep.tip(object, tip, ...)`
- `MRCA(.data, .node1, .node2=NULL, ...)`
- `node.label(x, node='internal', ...)`
- `nodeid(tree, label)`
- `nodelab(tree, id)`
- `offspring(.data, .node, tiponly=FALSE, self_include=FALSE, type='all', ...)`
- `parent(.data, .node, ...)`
- `rootnode(.data, ...)`
- `sibling(.data, .node, ...)`
- `tip.label(x, ...)`
- `tree_subset(tree, node, levels_back=5, group_node=TRUE, group_name="group", root_edge=TRUE)`
- `treedata(...)`

## Generic (2)

- `merge(x, y, ...)`
- `print(x, n=10, width=NULL, max_extra_cols=NULL, max_footer_lines=NULL, ...)`

## Reexport (49)

- `%<>%(lhs, rhs)`
- `%>%(lhs, rhs)`
- `.data(?)`
- `arrange(?)`
- `as.DNAbin(?)`
- `as.phylo(x, ...)`
- `as_tibble(x, ...)`
- `bind_rows(?)`
- `cli_warn(?)`
- `eval_select(?)`
- `extract.clade(?)`
- `filter(.data, .preserve=FALSE, keep.td=TRUE, ...)`
- `full_join(x, y, by=NULL, copy=FALSE, suffix=c("", ".y"), ...)`
- `group_by(?)`
- `head(x)`
- `inner_join(x, y, by=NULL, copy=FALSE, suffix=c("", ".y"), ...)`
- `interp(?)`
- `is(?)`
- `is.rooted(phy)`
- `isClass(?)`
- `left_join(x, y, by=NULL, copy=FALSE, suffix=c("", ".y"), keep=NULL, ...)`
- `mutate(.data, keep.td=TRUE, ...)`
- `new(?)`
- `Nnode(phy, internal.only=TRUE, ...)`
- `Ntip(phy)`
- `print.phylo(?)`
- `pull(.data, var=-1, name=NULL, ...)`
- `quo(?)`
- `read.tree(?)`
- `rename(.data, ...)`
- `representation(?)`
- `root(phy, outgroup, node=NULL, edgelabel=TRUE, ...)`
- `rtree(?)`
- `select(.data, keep.td=FALSE, ...)`
- `setClass(?)`
- `setClassUnion(?)`
- `setGeneric(?)`
- `setOldClass(?)`
- `show(?)`
- `str_wrap(?)`
- `style_subtle(?)`
- `summarise(?)`
- `summarize(?)`
- `tail(x)`
- `tibble(?)`
- `transmute(?)`
- `unnest(data, cols, ..., keep_empty=FALSE, ptype=NULL, names_sep=NULL, names_repair="check_unique")`
- `which.edge(?)`
- `yulab_msg(?)`
