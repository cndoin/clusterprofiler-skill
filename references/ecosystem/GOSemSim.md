# GOSemSim — 2.39.3

> 数据源：github.com/YuLab-SMU/GOSemSim@devel
> 18 个已知符号

## Function (18)

- `buildGOmap(TERM2GENE)`
- `clusterSim(cluster1, cluster2, semData, measure="Wang", drop="IEA", combine="BMA")`
- `combineScores(SimScores, combine)`
- `geneSim(gene1, gene2, semData, measure="Wang", drop="IEA", combine="BMA")`
- `get_organism(object)`
- `godata(OrgDb=NULL, annoDb=NULL, keytype="ENTREZID", ont, computeIC=TRUE, processTCSS=FALSE, cutoff=NULL)`
- `goSim(GOID1, GOID2, semData, measure="Wang")`
- `load_OrgDb(?)`
- `mclusterSim(clusters, semData, measure="Wang", drop="IEA", combine="BMA", BPPARAM=NULL)`
- `mgeneSim(genes, semData, measure="Wang", drop="IEA", combine="BMA", verbose=TRUE, BPPARAM=NULL)`
- `mgoSim(GO1, GO2, semData, measure="Wang", combine="BMA")`
- `parse_gff(file, asis=FALSE, add_indirect_GO=FALSE)`
- `read.blast2go(file, add_indirect_GO=FALSE)`
- `read.gaf(file, asis=FALSE, add_indirect_GO=FALSE)`
- `set_auto_update(x=TRUE)`
- `tcss_cutoff(OrgDb=NULL, keytype="ENTREZID", ont, combine_method="max", ppidata)`
- `termSim(t1, t2, semData, method=c("Wang", "Resnik", "Rel", "Jiang", "...)`
- `wangMethod_internal(ID1, ID2, ont="BP")`
