# DOSE — 4.7.3

> 数据源：YuLab-SMU/DOSE @ devel
> 49 个已知符号

## Function (17)

- `clusterSim(cluster1, cluster2, ont="HDO", organism=NULL, measure="Wang", combine="BMA")`
- `doseInterpretResult(result=NULL, evidence=NULL, query=NULL, sources=NULL, parameters=list(), explanation=list())`
- `doseSim(DOID1, DOID2, measure="Wang", ont="HDO")`
- `doSim(DOID1, DOID2, measure="Wang", ont="HDO")`
- `enrichDO(gene, ont="HDO", organism=NULL, pvalueCutoff=0.05, pAdjustMethod="BH", universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, readable=FALSE)`
- `enrichNCG(gene, pvalueCutoff=0.05, pAdjustMethod="BH", universe, minGSSize=10, maxGSSize=500, qvalueCutoff=0.2, readable=FALSE)`
- `evidence(x, target_id=NULL, type=NULL, source=NULL, direction=NULL)`
- `explainDisease(x, method=c("template", "llm"), max_features=3L, provider=NULL, model=NULL, language=c("en", "zh"), style=c("brief", "research", "cautious"), generation_params=list(), llm_adapter=NULL)`
- `gene2DO(gene, organism=NULL, ont="HDO")`
- `geneSim(geneID1, geneID2=NULL, ont="HDO", organism=NULL, measure="Wang", combine="BMA")`
- `gseDO(geneList, ont="HDO", organism=NULL, exponent=1, nPerm=1000, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, method="multilevel", adaptive=FALSE, minPerm=1000, maxPerm=10000, seed=FALSE, ...)`
- `gseNCG(geneList, exponent=1, nPerm=1000, minGSSize=10, maxGSSize=500, pvalueCutoff=0.05, pAdjustMethod="BH", verbose=TRUE, method="multilevel", adaptive=FALSE, minPerm=1000, maxPerm=10000, seed=FALSE, ...)`
- `interpretDisease(x, input=c("auto", "gene", "ranked_gene", "gen..., organism=c("human", "mouse"), target=c("disease", "mouse_model", "both"), ontology="auto", id_type="auto", orthology=c("one_to_one", "all"), explain=c("none", "template", "llm"), top=50, ...)`
- `mclusterSim(clusters, ont="HDO", organism=NULL, measure="Wang", combine="BMA")`
- `rankMouseModels(gene, disease_model_file, homology_file, gene_pheno_file, top=50)`
- `simplot(sim, xlab="", ylab="", color.low="white", color.high="red", labs=TRUE, digits=2, labs.size=3, font.size=14)`
- `theme_dose(font.size=14)`

## S4method (2)

- `as.data.frame(?)`
- `summary(?)`

## Reexport (30)

- `aes(x, y)`
- `combineScores(?)`
- `element_blank(?)`
- `element_text(?)`
- `facet_grid(?)`
- `geom_text(?)`
- `geom_tile(?)`
- `get_organism(db)`
- `ggplot(data, mapping)`
- `gsea_gson(?)`
- `is(?)`
- `load_OrgDb(OrgDb)`
- `margin(?)`
- `melt(?)`
- `memoise(?)`
- `new(?)`
- `ora_gson(?)`
- `scale_fill_gradient(?)`
- `scale_x_discrete(?)`
- `scale_y_discrete(?)`
- `set_auto_update(?)`
- `setReadable(?)`
- `show(?)`
- `stack(?)`
- `termSim(?)`
- `theme(?)`
- `theme_bw(?)`
- `xlab(?)`
- `ylab(?)`
- `yulab_msg(?)`
