# meshes — 1.39.3

> 数据源：github.com/YuLab-SMU/meshes@devel
> 8 个已知符号

## Function (8)

- `enrichMeSH(gene, MeSHDb, database='gendoo', category='C', pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, meshdbVersion=NULL)`
- `geneID(?)`
- `geneInCategory(?)`
- `geneSim(geneID1, geneID2=NULL, measure="Wang", combine="BMA", semData)`
- `get_organism(?)`
- `gseMeSH(geneList, MeSHDb, database='gendoo', category='C', nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, eps=1e-10, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, seed=FALSE, ...)`
- `meshdata(MeSHDb=NULL, database, category, computeIC=FALSE)`
- `meshSim(meshID1, meshID2, measure="Wang", semData)`
