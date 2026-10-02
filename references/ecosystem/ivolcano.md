# ivolcano — 0.0.7

> 数据源：YuLab-SMU/ivolcano @ devel
> 49 个已知符号

## Function (14)

- `geom_ivolcano_gene(top_n=10, label_mode="separate", fontface="italic", label_sig_only=TRUE, filter=NULL)`
- `geom_ivolcano_line(linetype="longdash", color='grey40', linewidth=0.5)`
- `idotplot(object, x="GeneRatio", color="p.adjust", showCategory=10, size="Count", label_format=30, trigger=c("click", "hover"), title="", ...)`
- `ivolcano(data, logFC_col="logFC", pval_col="adj.P.Val", gene_col="gene", title="Volcano Plot", interactive=TRUE, onclick_fun=NULL, pval_cutoff=0.05, logFC_cutoff=1, pval_cutoff2=NULL, logFC_cutoff2=NULL, size_by="none", point_size=list(base = 2, medium = 4, large = 6), threshold_line=list(color = "black", linetype = "das..., tooltip_cols=NULL, tooltip_labels=NULL, top_n=10, label_mode="separate", fontface="italic", label_sig_only=TRUE, filter=NULL)`
- `ivolcano_point(data, logFC_col="logFC", pval_col="adj.P.Val", gene_col="gene", title="Volcano Plot", interactive=TRUE, onclick_fun=NULL, pval_cutoff=0.05, logFC_cutoff=1, pval_cutoff2=NULL, logFC_cutoff2=NULL, size_by="none", point_size=list(base = 2, medium = 4, large = 6), tooltip_cols=NULL, tooltip_labels=NULL)`
- `onclick_ensembl(gene)`
- `onclick_fanyi(gene_summary, cols)`
- `onclick_genecards(gene)`
- `onclick_hgnc(gene)`
- `onclick_ncbi(gene)`
- `onclick_pubmed(gene)`
- `onclick_uniprot(gene)`
- `pathway_app(enrichment, gene_data, pathway_col="Description", pathway_gene_col="geneID", pathway_p_col="p.adjust", pathway_ratio_col="GeneRatio", gene_col="gene", gene_effect_col="logFC", gene_p_col="adj.P.Val", show_pathways=NULL, gene_id_case=c("asis", "upper", "lower"), pval_cutoff=0.05, logFC_cutoff=1, launch=FALSE, app_title="Pathway-gene explorer")`
- `scale_color_figureya(mode=c("classic", "advanced"), na.value="grey80", guide="none", ...)`

## Generic (1)

- `print(x, ...)`

## Reexport (34)

- `.data(?)`
- `aes(x, y)`
- `coord_cartesian(?)`
- `element_blank(?)`
- `element_text(?)`
- `fortify(?)`
- `geom_hline(?)`
- `geom_point(?)`
- `geom_point_interactive(?)`
- `geom_text_repel(?)`
- `geom_vline(?)`
- `ggplot(data, mapping)`
- `ggplot_add(object, plot, ...)`
- `girafe(?)`
- `girafeOutput(?)`
- `is(?)`
- `knit_print(?)`
- `labs(?)`
- `margin(?)`
- `modifyList(?)`
- `mutate(?)`
- `opts_hover(?)`
- `renderGirafe(?)`
- `reorder(?)`
- `scale_alpha_identity(?)`
- `scale_color_continuous(?)`
- `scale_color_manual(values)`
- `scale_colour_manual(?)`
- `scale_size_identity(?)`
- `setNames(?)`
- `sym(?)`
- `theme(?)`
- `theme_minimal(?)`
- `ylab(?)`
