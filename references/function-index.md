# clusterProfiler 函数分类索引

版本：clusterProfiler 4.21.2。用于快速定位「该用哪个函数」；签名查 `api-signatures.md`。

| 模块 | 函数 |
| --- | --- |
| **ora** 过表示分析 ORA（GO / KEGG / WikiPathways / Module / PathwayCommons / DAVID / 通用 enricher） | `compareCluster`, `enrichDAVID`, `enricher`, `enrichGO`, `enrichKEGG`, `enrichMKEGG`, `enrichPC`, `enrichWP` |
| **gsea** GSEA / NSEA / 拓扑感知 / 贝叶斯 | `GSEA`, `gseGO`, `gseKEGG`, `gseMKEGG`, `gsePC`, `gseWP`, `mnseGO`, `mnseKEGG`, `mnseMKEGG`, `mnseWP`, `nseGO`, `nseKEGG`, `nseMKEGG`, `nseWP` |
| **id** 基因 ID 转换与位点注释 | `bitr`, `bitr_kegg`, `get_wp_organisms`, `getTaxID`, `getTaxInfo`, `Gff2GeneTable`, `go2ont`, `go2term`, `idType`, `ko2name` |
| **db** 数据库 / GSON / KEGG 下载 | `append_kegg_category`, `download_KEGG`, `gson_GO`, `gson_GO_local`, `gson_KEGG`, `gson_KEGG_mapper`, `gson_KO`, `gson_WP`, `read.gmt.pc`, `search_kegg_organism` |
| **go** GO 工具（groupGO / gofilter / dropGO / buildGOmap） | `add_go_level`, `dropGO`, `gofilter`, `groupGO` |
| **manip** 结果操作（merge_result / simplify） | `as.data.frame`, `dim`, `geneID`, `geneInCategory`, `merge_result`, `simplify` |
| **viz** 可视化（dotplot/cnetplot/emapplot/gseaplot/heatmap/ridgeplot/goplot） | `browseKEGG`, `plot`, `plotGOgraph` |
| **external** 外部数据（PPI / Uniprot / Taxa） | `get_ppi`, `get_ppi_network`, `getPPI`, `uniprot_get` |
| **llm** LLM 解读（interpret / interpret_agent / interpret_hierarchical） | `interpret`, `interpret_agent`, `interpret_hierarchical`, `print` |
| **dplyr** dplyr 风格 S3 method（arrange/filter/group_by/mutate/...） | `arrange`, `filter`, `group_by`, `mutate`, `n`, `rename`, `select`, `slice`, `summarise` |
| **reexport** 第三方包 re-export（enrichplot/dplyr/magrittr/...） | `%<>%`, `%>%`, `%||%`, `aes`, `Agent`, `aggregate_enrichment`, `aggregate_omics`, `as_enrichResult`, `as_gseaResult`, `bayes_enrich`, `bayes_summary`, `browseURL`, `build_go_graph`, `build_kegg_graph`, `build_string_graph`, `buildGOmap`, `ChatSession`, `citation`, `classify_omics_pattern`, `cnetplot`, `collapse_multilayer_scores`, `dlply`, `dotplot`, `download_yulab_file`, `emapplot`, `extract_mnsea_subnetwork`, `formula`, `gather`, `generate_object`, `geom_label`, `geom_point`, `get_cache`, `get_cache_item`, `get_fun_from_pkg`, `get_mnsea_contribution`, `get_omics_contribution`, `get_organism`, `ggplot`, `ggtitle`, `godata`, `goplot`, `gsea`, `gseaplot`, `gseaScores`, `gsfilter`, `gson`, `harmonize_ids`, `head`, `heatplot`, `installed.packages`, `is`, `is.installed`, `keys`, `keytypes`, `ldply`, `llply`, `load_OrgDb`, `mgoSim`, `modifyList`, `new`, `Ontology`, `ora`, `packageDescription`, `prepare_multilayer_network`, `prepare_network`, `propagate_multilayer`, `read.blast2go`, `read.gaf`, `read.gmt`, `read.gmt.wp`, `read.table`, `ridgeplot`, `scale_color_manual`, `select_features_for_ora`, `separate`, `setNames`, `setReadable`, `stack`, `str`, `tail`, `theme_void`, `toTable`, `user_dir`, `yread`, `yread_tsv`, `z_array`, `z_enum`, `z_object`, `z_string` |

## S3 method 覆盖（35 条）

形如 `generic.class`；调用时写 `generic(obj, ...)` 由 R 自动分派。

| generic | 支持的方法类 |
| --- | --- |
| `arrange` | `compareClusterResult`, `enrichResult`, `gseaResult` |
| `as.data.frame` | `compareClusterResult`, `groupGOResult` |
| `dim` | `compareClusterResult` |
| `filter` | `compareClusterResult`, `enrichResult`, `gseaResult` |
| `geneID` | `groupGOResult` |
| `geneInCategory` | `groupGOResult` |
| `group_by` | `compareClusterResult`, `enrichResult`, `gseaResult` |
| `head` | `compareClusterResult` |
| `mutate` | `compareClusterResult`, `enrichResult`, `gseaResult` |
| `plot` | `interpretation`, `interpretation_list` |
| `print` | `interpretation`, `interpretation_list` |
| `rename` | `compareClusterResult`, `enrichResult`, `gseaResult` |
| `select` | `compareClusterResult`, `enrichResult`, `gseaResult` |
| `slice` | `compareClusterResult`, `enrichResult`, `gseaResult` |
| `summarise` | `compareClusterResult`, `enrichResult`, `gseaResult` |
| `tail` | `compareClusterResult` |

## S4 method 覆盖（6 条）

形如 `setMethod("generic", signature(class="..."), function(...) {})`，用户脚本里通常不直接写它，但 S3 dispatch 实际会命中这些实现。

| generic | 支持的方法类 |
| --- | --- |
| `show` | `compareClusterResult`, `groupGOResult` |
| `simplify` | `compareClusterResult`, `enrichResult`, `gseaResult` |
| `summary` | `compareClusterResult` |

## S4 类（1）

`groupGOResult`

## 第三方包 re-export（按包汇总，18 包 / 94 函数）

- **AnnotationDbi**（4）：`Ontology`, `keys`, `keytypes`, `toTable`
- **GO.db**（4）：`GOBPCHILDREN`, `GOCCCHILDREN`, `GOMFCHILDREN`, `GOTERM`
- **GOSemSim**（6）：`buildGOmap`, `get_organism`, `godata`, `mgoSim`, `read.blast2go`, `read.gaf`
- **aisdk**（7）：`Agent`, `ChatSession`, `generate_object`, `z_array`, `z_enum`, `z_object`, `z_string`
- **dplyr**（9）：`arrange`, `filter`, `group_by`, `mutate`, `n`, `rename`, `select`, `slice`, `summarise`
- **enrichit**（10）：`aggregate_enrichment`, `aggregate_omics`, `bayes_enrich`, `bayes_summary`, `geneID`, `geneInCategory`, `gsfilter`, `harmonize_ids`, `select_features_for_ora`, `setReadable`
- **enrichplot**（7）：`cnetplot`, `dotplot`, `emapplot`, `goplot`, `gseaplot`, `heatplot`, `ridgeplot`
- **ggplot2**（7）：`aes`, `geom_label`, `geom_point`, `ggplot`, `ggtitle`, `scale_color_manual`, `theme_void`
- **gson**（3）：`gson`, `read.gmt`, `read.gmt.wp`
- **magrittr**（2）：`"%<>%"`, `"%>%"`
- **methods**（2）：`is`, `new`
- **plyr**（3）：`dlply`, `ldply`, `llply`
- **qvalue**（1）：`qvalue`
- **rlang**（5）：`"%||%"`, `.data`, `check_installed`, `quos`, `sym`
- **stats**（3）：`formula`, `na.omit`, `setNames`
- **tidyr**（2）：`gather`, `separate`
- **utils**（10）：`browseURL`, `citation`, `head`, `installed.packages`, `modifyList`, `packageDescription`, `read.table`, `stack`, `str`, `tail`
- **yulab.utils**（9）：`download_yulab_file`, `get_cache`, `get_cache_item`, `get_fun_from_pkg`, `is.installed`, `load_OrgDb`, `user_dir`, `yread`, `yread_tsv`
