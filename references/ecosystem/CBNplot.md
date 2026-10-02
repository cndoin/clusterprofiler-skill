# CBNplot — 0.99.2

> 数据源：YuLab-SMU/CBNplot @ main
> 42 个已知符号

## Function (10)

- `bngeneplot(results, exp, expSample=NULL, algo="hc", R=20, returnNet=FALSE, algorithm.args=NULL, pathNum=NULL, convertSymbol=TRUE, expRow="ENSEMBL", interactive=FALSE, cexCategory=1, cl=NULL, showDir=FALSE, chooseDir=FALSE, scoreType="bic-g", labelSize=4, layout="nicely", clusterAlpha=0.2, strType="normal", delZeroDegree=TRUE, otherVar=NULL, otherVarName=NULL, onlyDf=FALSE, disc=FALSE, tr=NULL, remainCont=NULL, sp="hsapiens", compareRef=FALSE, compareRefType="intersection", pathDb="reactome", dep=NULL, depMeta=NULL, sizeDep=FALSE, showDepHist=TRUE, cellLineName="5637_URINARY_TRACT", showLineage=FALSE, orgDb=org.Hs.eg.db, shadowText=TRUE, bgColor="white", textColor="black", strengthPlot=FALSE, nStrength=10, strThresh=NULL, hub=NULL, seed=1)`
- `bngeneplotCustom(results, exp, expSample=NULL, algo="hc", R=20, pathNum=NULL, convertSymbol=TRUE, expRow="ENSEMBL", interactive=FALSE, cexCategory=1, cl=NULL, showDir=FALSE, chooseDir=FALSE, algorithm.args=NULL, labelSize=4, layout="nicely", strType="normal", returnNet=FALSE, otherVar=NULL, otherVarName=NULL, onlyDf=FALSE, disc=FALSE, tr=NULL, remainCont=NULL, dep=NULL, sizeDep=FALSE, orgDb=org.Hs.eg.db, cellLineName="5637_URINARY_TRACT", fontFamily="sans", strengthPlot=FALSE, nStrength=10, strThresh=NULL, hub=NULL, glowEdgeNum=NULL, nodePal=c("blue","red"), edgePal=c("blue","red"), textCol="black", titleCol="black", backCol="white", barTextCol="black", barPal=c("red","blue"), barBackCol="white", scoreType="bic-g", barLegendKeyCol="white", barAxisCol="black", barPanelGridCol="black", titleSize=24, seed=1)`
- `bngenetest(results, exp, expSample=NULL, algo="hc", Rrange=seq(2,40,2), cl=NULL, algorithm.args=NULL, pathNum=NULL, convertSymbol=TRUE, expRow="ENSEMBL", scoreType="aic-g")`
- `bnpathplot(results, exp, expSample=NULL, algo="hc", algorithm.args=NULL, expRow="ENSEMBL", cl=NULL, returnNet=FALSE, otherVar=NULL, otherVarName=NULL, qvalueCutOff=0.05, adjpCutOff=0.05, nCategory=15, R=20, interactive=FALSE, color="p.adjust", cexCategory=1, cexLine=0.5, chooseDir=FALSE, showDir=FALSE, delZeroDegree=TRUE, labelSize=4, layout="nicely", onlyDf=FALSE, disc=FALSE, tr=NULL, remainCont=NULL, shadowText=TRUE, bgColor="white", textColor="black", compareRef=FALSE, strThresh=NULL, strType="normal", hub=NULL, scoreType="bic-g", databasePal="Set2", dep=NULL, sizeDep=FALSE, orgDb=org.Hs.eg.db, edgeLink=TRUE, cellLineName="5637_URINARY_TRACT", strengthPlot=FALSE, nStrength=10, seed=1)`
- `bnpathplotCustom(results, exp, expSample=NULL, algo="hc", R=20, expRow="ENSEMBL", color="p.adjust", cexCategory=1, cl=NULL, showDir=FALSE, chooseDir=FALSE, labelSize=4, layout="nicely", strType="normal", compareRef=FALSE, disc=FALSE, tr=NULL, remainCont=NULL, qvalueCutOff=0.05, adjpCutOff=0.05, nCategory=15, cexLine=1, returnNet=FALSE, dep=NULL, sizeDep=FALSE, cellLineName="5637_URINARY_TRACT", fontFamily="sans", otherVar=NULL, otherVarName=NULL, onlyDf=FALSE, algorithm.args=NULL, strengthPlot=FALSE, nStrength=10, strThresh=NULL, hub=NULL, glowEdgeNum=NULL, nodePal=c("blue","red"), edgePal=c("blue","red"), textCol="black", backCol="white", barTextCol="black", barPal=c("red","blue"), barBackCol="white", scoreType="bic-g", barLegendKeyCol="white", orgDb=org.Hs.eg.db, barAxisCol="black", barPanelGridCol="black", seed=1)`
- `bnpathtest(results, exp, expSample=NULL, algo="hc", algorithm.args=NULL, expRow="ENSEMBL", cl=NULL, qvalueCutOff=0.05, adjpCutOff=0.05, nCategory=15, Rrange=seq(2,40,2), scoreType="aic-g")`
- `compareBNs(listOfNets)`
- `obtainPath(res, geneSymbol)`
- `queryCpDistLs(fitted, candidate, evidences, discPalette="Set2", ...)`
- `queryCpDistLw(fitted, candidate, evidence, level, point=FALSE, pointSize=5, alpha=TRUE, ...)`

## Reexport (32)

- `%>%(lhs, rhs)`
- `arrange(?)`
- `averaged.network(?)`
- `boot.strength(?)`
- `cextend(?)`
- `choose.direction(?)`
- `combn(?)`
- `convertIdentifiers(?)`
- `cpdist(?)`
- `filter(?)`
- `geom_dots(?)`
- `group_by(?)`
- `group_by_at(?)`
- `inclusion.threshold(?)`
- `map(?)`
- `melt(?)`
- `msfit(?)`
- `mutate(?)`
- `n(?)`
- `packageVersion(?)`
- `pathwayGraph(?)`
- `pathways(?)`
- `read.csv(?)`
- `reduce(?)`
- `scale_fill_ramp_continuous(?)`
- `score(?)`
- `select(?)`
- `setReadable(?)`
- `str_starts(?)`
- `summarise(?)`
- `summarize(?)`
- `undirected.arcs(?)`
