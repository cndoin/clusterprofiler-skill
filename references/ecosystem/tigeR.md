# tigeR — 1.0.0

> 数据源：YuLab-SMU/tigeR @ main
> 89 个已知符号

## Function (64)

- `ABIS(SE, sig_matrix)`
- `bind_meta(SE, isList)`
- `bind_mtr(SE, isList)`
- `browse_BE(SE)`
- `browse_biomk(SE, feature, colors=NULL, PT_drop=FALSE, lg.pos=c(0.7,0.14))`
- `build_CellType_Ref(Seurat_obj, logfc.threshold=0.1, min.pct=0.1, only.pos=TRUE)`
- `build_Model(SE, Model, feature_genes, rmBE=FALSE, response_NR=TRUE, PT_drop=TRUE, mtr, meta, ...)`
- `cell_name_filter(mtr)`
- `cell_name_standardization(SE)`
- `CIBERSORT(SE, sig_matrix, perm=0, QN=TRUE, style='elegant', group_color=c("#5f96e8CC", "#ee822fCC"))`
- `compare_biomk(SE=NULL, Signature=NULL, method="Average_mean", PT_drop=TRUE, show.val=TRUE, val.size=2)`
- `compare_roc(ROC, lg.label=c("NB","SVM","RF","CC","ADB","LGB","L..., line.col=c("black", "#F89B9B", "#4DB867", "#C6...)`
- `ConsensusTME(SE, cancer="SKCM", ...)`
- `count2tpm(counts)`
- `data_standardization(SE, type)`
- `Dataloader(pick=NULL, use_source="Web Server")`
- `dataPreprocess(exp_mtr, Signature=NULL, turn2HL=TRUE, meta=NULL, returnSE=FALSE)`
- `dataPreprocess_SE(SE, Signature=NULL, turn2HL=TRUE)`
- `dataProcess(SE, Signature, rmBE, response_NR, turn2HL)`
- `dataProcess_SE(SE, Signature, rmBE, response_NR, turn2HL)`
- `deconv_TME(SE, method, ...)`
- `diff_biomk(SE, gene, type, method='Average_mean', PT_drop=TRUE, p.pos=c(0.2,0.7), p.round=2, log_sc=TRUE, textcol="black", panelcol="black")`
- `diff_gene(SE)`
- `diff_TME(SE, feature=NULL, style="elegant", group_color=c("#5f96e8CC", "#ee822fCC"))`
- `draw_bar(mtr, feature)`
- `EPIC(SE, sig_matrix=NULL, ...)`
- `ESTIMATE(SE)`
- `extract_label(datasetNames)`
- `extract_mtr(datasetNames)`
- `fpkm2tpm(SE)`
- `fraction_pie(mtr, feature, rows=1, pie_scale=0.9, color="white", label_radius=NULL, label_show_ratio=FALSE, label_threshold=0.04, fontsize=1.5, ...)`
- `gini_gene(SE, length.out=NULL)`
- `Immunotherapy_Response_Batch(SE, geneSet=NULL, method=NULL, PT_drop=TRUE)`
- `integrate_analysis(SE, geneSet=NULL, method=NULL, PT_drop=TRUE)`
- `IPS(SE, project=NULL, plot=FALSE)`
- `ipsmap(x)`
- `IRS_grading(exp_mtr)`
- `load_from_ExperimentHub(pick)`
- `load_from_WebServer(pick)`
- `mapbw(x, my_palette2)`
- `mapcolors(x, my_palette)`
- `max_min_normalization(exp_mtr)`
- `MCPCounter(SE, featuresType="HUGO_symbols", ...)`
- `MCPcounter.estimate(expression, featuresType, probesets, genes)`
- `merge_SE(SE)`
- `pred_response(SE=NULL, exp_mtr=NULL, meta=NULL, threshold=0.8, positive="R", Signature=NULL, method="Average_mean", PT_drop=TRUE, show.val=TRUE, sort_by="rankscore", group_by="rankscore", show.Observed=TRUE, text_col="black", rankscore=TRUE, ZS=TRUE)`
- `quanTIseq(SE, tumor=TRUE, arrays=FALSE, scale_mrna=FALSE, ...)`
- `remove_BE(SE, method)`
- `response_filter(response)`
- `response_prediction(SE=NULL, exp_mtr=NULL, meta=NULL, threshold, positive="R", Signature=NULL, method="Average_mean", PT_drop=TRUE)`
- `response_standardize(V)`
- `roc_biomk(SE, Signature, method=NULL, rmBE=FALSE, response_NR=TRUE, PT_drop=TRUE, auc.pos=c(0.3,0.42), auc.round=3, textcol="black", panelcol="black")`
- `score_biomk(SE=NULL, exp_mtr=NULL, meta=NULL, Signature=NULL, method="Average_mean", PT_drop=TRUE)`
- `score_biomk_SE(SE=NULL, exp_mtr=NULL, meta=NULL, Signature=NULL, method="Average_mean", PT_drop=TRUE)`
- `surv_biomk(SE, gene, method='Average_mean', style='elegant', conf.int=FALSE, val.pos=c(0.03,0.2), lg=NULL, lg.pos=c(0.6,0.9), lg.text="precise", p.round=4, PT_drop=TRUE, drop_zero=FALSE)`
- `surv_styling(df, style, conf.int, gene, method, val.pos, lg, lg.pos, lg.text, p.round)`
- `test_Model(Model, SE=NULL, mtr=NULL, meta=NULL, PT_drop=TRUE)`
- `test_Model.default(Model, SE, PT_drop=TRUE)`
- `test_Model.matrix(mtr, meta, Model)`
- `tGE8_grading(exp_mtr)`
- `TIMER(SE, sig_matrix=NULL, type="SKCM")`
- `TIMER_SE(SE, type="SKCM")`
- `to1(SE, by_row=TRUE)`
- `xCell(SE, signatures=NULL, genes=NULL, spill=NULL, rnaseq=TRUE, file.name=NULL, scale=TRUE, alpha=0.5, save.raw=FALSE, parallel.sz=4, parallel.type='SOCK', cell.types.use=NULL)`

## Reexport (25)

- `%$%(?)`
- `%<>%(lhs, rhs)`
- `%>%(lhs, rhs)`
- `.data(?)`
- `assay(?)`
- `coef(?)`
- `colData(?)`
- `cor(?)`
- `current_env(?)`
- `ExperimentHub(?)`
- `fit(?)`
- `ggsurvplot(?)`
- `median(?)`
- `model.matrix(?)`
- `na.omit(?)`
- `query(?)`
- `randomForest(?)`
- `roc(?)`
- `sd(?)`
- `setNames(?)`
- `Surv(?)`
- `survfit(?)`
- `t.test(?)`
- `theme_bw(?)`
- `wilcox.test(?)`
