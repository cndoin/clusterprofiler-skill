# treeio — 1.37.1

> 数据源：YuLab-SMU/treeio @ devel
> 115 个已知符号

## Function (46)

- `edgeNum2nodeNum(jp, edgeNum)`
- `find.hclust(x, graph.mst=FALSE, weights=NULL, hclust.method='average', ...)`
- `get.placements(tree, by="best", ...)`
- `get.tree(x, ...)`
- `get.treetext(?)`
- `getNodeNum(tree)`
- `is.ggtree(x)`
- `label_branch_paml(tree, node, label)`
- `mask(tree_object, field, site, mask_site=FALSE)`
- `merge_tree(obj1, obj2)`
- `Nnode2(tree)`
- `raxml2nwk(infile, outfile="raxml.tree")`
- `read.astral(file)`
- `read.beast(file, threads=1, verbose=FALSE)`
- `read.beast.newick(file, threads=1, verbose=FALSE)`
- `read.codeml(rstfile, mlcfile, tree="mlc", type="Joint")`
- `read.codeml_mlc(mlcfile)`
- `read.fasta(fasta, type="auto")`
- `read.hyphy(nwk, ancseq, tip.fasfile=NULL)`
- `read.hyphy.seq(file)`
- `read.iqtree(file)`
- `read.jplace(file)`
- `read.jtree(file)`
- `read.mcmctree(file, force.ultrametric=FALSE)`
- `read.mega(?)`
- `read.mega_tabular(file)`
- `read.mrbayes(file, threads=1, verbose=FALSE)`
- `read.newick(file, node.label="label", ...)`
- `read.nextstrain.json(x)`
- `read.nhx(treetext, phylo)`
- `read.paml_rst(rstfile, type="Joint")`
- `read.phylip(file)`
- `read.phylip.seq(file)`
- `read.phylip.tree(file)`
- `read.phyloxml(file)`
- `read.r8s(file)`
- `read.raxml(file=NULL, text=NULL)`
- `read.treeqza(treeqza, node.label="label", ...)`
- `read.treetime(file)`
- `rename_taxa(tree, data, key=1, value=2)`
- `rescale_tree(tree_object, branch.length)`
- `spt(x, from, to, weights=NULL, ...)`
- `write.beast(treedata, file="", append=FALSE, digits=10, tree.prefix="")`
- `write.beast.newick(treedata, file="", append=FALSE, digits=10, tree.prefix="")`
- `write.jplace(x, outfile)`
- `write.jtree(treedata, file="")`

## Generic (1)

- `print(x, ...)`

## Reexport (68)

- `%<>%(lhs, rhs)`
- `%>%(lhs, rhs)`
- `.compressTipLabel(?)`
- `.data(?)`
- `.hasSlot(?)`
- `.uncompressTipLabel(?)`
- `ancestor(?)`
- `as.AAbin.character(?)`
- `as.dist(?)`
- `as.DNAbin(?)`
- `as.DNAbin.character(?)`
- `as.phylo(x, branch.length, label, ...)`
- `as.treedata(tree, boot=NULL, branch.length, label, type="ml", ...)`
- `as_tibble(?)`
- `branching.times(?)`
- `check_installed(?)`
- `checkLabel(?)`
- `child(?)`
- `drop.tip(?)`
- `enexpr(?)`
- `filter(?)`
- `fromJSON(?)`
- `full_join(?)`
- `get.data(?)`
- `get.fields(?)`
- `get_tree_data(?)`
- `group_by(?)`
- `hclust(?)`
- `inner_join(?)`
- `is(?)`
- `is.rooted(?)`
- `is.ultrametric(?)`
- `isTip(?)`
- `mclapply(?)`
- `missingArg(?)`
- `MRCA(?)`
- `mutate(?)`
- `mutate_if(?)`
- `n(?)`
- `new(?)`
- `Nnode(edge)`
- `nodeid(?)`
- `nodelab(?)`
- `Ntip(edge)`
- `offspring(?)`
- `parent(?)`
- `quo_name(?)`
- `read.FASTA(?)`
- `read.nexus(?)`
- `read.tree(?)`
- `rename(?)`
- `reorder.phylo(?)`
- `root(?)`
- `rootnode(?)`
- `rtree(?)`
- `select(?)`
- `setGeneric(?)`
- `setNames(?)`
- `slot(?)`
- `summarize(?)`
- `tibble(?)`
- `toJSON(?)`
- `trans(?)`
- `treedata(?)`
- `use_perl(?)`
- `write.nexus(?)`
- `write.tree(?)`
- `yulab_msg(?)`
