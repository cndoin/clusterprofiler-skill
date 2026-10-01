# MicrobiomeProfiler — 1.19.2

> 数据源：github.com/YuLab-SMU/MicrobiomeProfiler@devel
> 22 个已知符号

## Function (22)

- `available_datasets(include_remote=FALSE)`
- `clear_dataset_cache(dataset=NULL)`
- `dataset_cache_info(dataset=NULL)`
- `download_dataset(dataset, refresh=FALSE)`
- `enrichBugSigDB(microbe_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, refresh=FALSE)`
- `enrichCOG(gene, dtype="category", pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)`
- `enrichEggNOG(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, refresh=FALSE)`
- `enrichHMDB(metabo_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)`
- `enrichKO(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)`
- `enrichMBKEGG(metabo_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)`
- `enrichMDA(microbe_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, refresh=FALSE)`
- `enrichModule(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)`
- `enrichSMPDB(metabo_list, pvalueCutoff=0.05, pAdjustMethod="BH", universe=NULL, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2)`
- `gseCOG(geneList, dtype="category", nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)`
- `gseEggNOG(geneList, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", refresh=FALSE, seed=FALSE)`
- `gseHMDB(metabo_list, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)`
- `gseKO(geneList, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)`
- `gseMBKEGG(metabo_list, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)`
- `gseMDA(microbe_list, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, refresh=FALSE, seed=FALSE)`
- `gseModule(geneList, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)`
- `gseSMPDB(metabo_list, nPerm=1000, exponent=1, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", method="multilevel", adaptive=FALSE, minPerm=101, maxPerm=100000, pvalThreshold=0.1, verbose=TRUE, seed=FALSE)`
- `run_MicrobiomeProfiler(onStart=NULL, options=list(), enableBookmarking=NULL, uiPattern="/", ...)`
