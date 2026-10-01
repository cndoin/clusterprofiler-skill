#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cp_plan.py —— 一句话需求 -> clusterProfiler 流程建议（离线规则，不联网、不调用 LLM）

用法：
  python cp_plan.py "做 GO 富集分析"
  python cp_plan.py "GSEA 跑 KEGG 多组学比较" --json
  python cp_plan.py --list

输出的是「该按什么顺序调哪些函数」，不是可直接跑的完整脚本；
完整模板在 references/workflows.md。
"""
import os, sys, json, argparse

PLANS = [
    {
        "id": "go-ora",
        "title": "GO 过表示分析（ORA，enrichGO）",
        "keys": ["go", "ora", "基因本体", "bp", "cc", "mf", "ontology", "过表示",
                 "go富集", "go分析", "gobp", "gocc", "gomf"],
        "steps": [
            "library(clusterProfiler)",
            "gene <- bitr(deg$gene_id, fromType='SYMBOL', toType='ENTREZID', OrgDb=org.Hs.eg.db)$ENTREZID",
            "ego <- enrichGO(gene = gene, OrgDb = org.Hs.eg.db, keyType = 'ENTREZID',",
            "                ont = 'BP', pAdjustMethod = 'BH', pvalueCutoff = 0.01,",
            "                qvalueCutoff = 0.05, readable = TRUE)",
            "dotplot(ego, showCategory = 20) + theme(axis.text.y = element_text(size=8))",
            "barplot(ego, showCategory = 15)",
            "cnetplot(ego, categorySize = 'pvalue', foldChange = deg$log2fc)",
            "emapplot(pairwise_termsim(ego))",
        ],
        "notes": ["keyType 必须与输入 ID 类型匹配（ENTREZID / SYMBOL / ENSEMBL ...）",
         "OrgDb 选 species 对应的 Annotation 包（人 org.Hs.eg.db / 鼠 org.Mm.eg.db ...）",
         "ont='ALL' 会把 BP/CC/MF 合并跑一遍，结果可拆开看",
         "readable=TRUE 会自动把 ENTREZID 转回 SYMBOL，但要求 OrgDb 可用"],
    },
    {
        "id": "kegg-ora",
        "title": "KEGG 通路 ORA（enrichKEGG）",
        "keys": ["kegg", "kegg通路", "kegg富集", "pathway", "信号通路"],
        "steps": [
            "library(clusterProfiler)",
            "gene <- bitr_kegg(deg$gene_id, fromType='ncbi-geneid', toType='kegg', organism='hsa')$kegg",
            "ek <- enrichKEGG(gene = gene, organism = 'hsa', keyType = 'kegg',",
            "                  pAdjustMethod = 'BH', pvalueCutoff = 0.05)",
            "dotplot(ek, showCategory = 15)",
            "cnetplot(ek, categorySize = 'pvalue')",
            "browseKEGG(ek, category = 'Apoptosis')    # 在浏览器里看 pathway 图",
        ],
        "notes": ["organism 三字母代码：人 hsa / 鼠 mmu / 斑马鱼 dre ... 4000+ 种支持",
         "kegg 需要联网（api.kegg.jp），离线要 build local GSON：gson_KEGG('hsa')",
         "organism 也可以传 GSON 对象（4.21+ 新功能），offline-friendly",
         "国内网络常卡；失败时用 search_kegg_organism() 查正确代码"],
    },
    {
        "id": "wikipathways-ora",
        "title": "WikiPathways ORA（enrichWP）",
        "keys": ["wikipathways", "wiki", "wp", "wikipathway", "wikipathway富集"],
        "steps": [
            "library(clusterProfiler)",
            "ewp <- enrichWP(gene, organism = 'Homo sapiens')",
            "dotplot(ewp, showCategory = 15)",
        ],
        "notes": ["organism 用 WikiPathways 自己的名字（Homo sapiens / Mus musculus ...）",
         "要查可用 organism：get_wp_organisms()",
         "WikiPathways 每月更新，部分通路不一定在 KEGG 里"],
    },
    {
        "id": "module-kegg-ora",
        "title": "KEGG Module ORA（enrichMKEGG）",
        "keys": ["kegg module", "module", "kegg模块", "mKEGG", "mkegg"],
        "steps": [
            "library(clusterProfiler)",
            "emk <- enrichMKEGG(gene = gene, organism = 'hsa')",
            "dotplot(emk, showCategory = 15)",
        ],
        "notes": ["KEGG Module 是比 pathway 更小的功能单元（pathway 内的子模块）",
         "数据源：KO（KEGG Orthology），与 enrichKEGG 互补",
         ],
    },
    {
        "id": "pathwaycommons-ora",
        "title": "PathwayCommons ORA（enrichPC）",
        "keys": ["pathwaycommons", "pathway commons", "pc", "pathwaycommons富集"],
        "steps": [
            "library(clusterProfiler)",
            "epc <- enrichPC(gene, pathway = 'reactome')    # 或 'nci_pathway' / 'biocarta' ...",
            "dotplot(epc, showCategory = 15)",
        ],
        "notes": ["pathway 选 'reactome_pathway' / 'nci_pathway' / 'biocarta' / 'pid' / 'humancyc' / 'wikipathways'",
         "PathwayCommons 收录 5000+ 通路（汇聚多源）"],
    },
    {
        "id": "gsea-go",
        "title": "GSEA / GO（gseGO）",
        "keys": ["gsea", "gsea go", "gsea-go", "基因集富集", "gobp gsea"],
        "steps": [
            "library(clusterProfiler)",
            "gl <- deg$log2fc; names(gl) <- deg$gene_id",
            "gl <- sort(gl, decreasing = TRUE)",
            "ggo <- gseGO(gl, OrgDb = org.Hs.eg.db, ont = 'BP', keyType = 'SYMBOL',",
            "             minGSSize = 15, maxGSSize = 500, pvalueCutoff = 0.05,",
            "             pAdjustMethod = 'BH', verbose = FALSE)",
            "gseaplot(ggo, geneSetID = 1:3)",
            "dotplot(ggo, showCategory = 10, split = 'sign')",
            "ridgeplot(ggo, showCategory = 5)",
        ],
        "notes": ["gl 必须是有名字的有序数值向量（log2FC / t-stat / 显著性指标都可以）",
         "minGSSize/maxGSSize 控制基因集过滤范围，按数据调",
         "nPerm 参数控制置换次数（默认 1000）；想精确一点调到 10000",
         "keyType 与 names(gl) 的 ID 类型必须一致"],
    },
    {
        "id": "gsea-kegg",
        "title": "GSEA / KEGG（gseKEGG）",
        "keys": ["gsea-kegg", "kegg gsea", "gsea kegg", "gseKEGG"],
        "steps": [
            "library(clusterProfiler)",
            "gl <- sort(setNames(deg$log2fc, deg$entrez), decreasing = TRUE)",
            "gk <- gseKEGG(gl, organism = 'hsa', minGSSize = 15, pvalueCutoff = 0.05)",
            "gseaplot(gk, geneSetID = gk$ID[1:3])",
        ],
        "notes": ["names 必须是 ENTREZID（kegg 用）",
         "同样可以传 GSON 给 organism 走离线模式（4.21+）"],
    },
    {
        "id": "msigdb-gsea",
        "title": "MSigDB 集合 GSEA（GSEA() 通用入口）",
        "keys": ["msigdb", "hallmark", "gsea 通用", "通用 gsea", "gsea 集合",
                 "h", "c2", "c5", "immunologic", "motif", "oncogenic"],
        "steps": [
            "library(clusterProfiler)",
            "library(msigdbr)         # 提供 MSigDB 全量注释",
            "gmt <- msigdbr(species = 'Homo sapiens', category = 'H') |>",
            "       dplyr::select(gs_name, entrez_gene)",
            "gl <- sort(setNames(deg$log2fc, deg$entrez), decreasing = TRUE)",
            "ge <- GSEA(gl, TERM2GENE = gmt, pvalueCutoff = 0.05)",
            "dotplot(ge, showCategory = 10)",
        ],
        "notes": ["msigdbr 把 MSigDB 全部集合（hallmark / c1-c7）提供成 R 可用的 tibble",
         "category = 'H'（hallmark 50 组）/ 'C2'（curated）/ 'C5'（GO gene sets）",
         "subcategory 可细选（如 'C2.CP:KEGG'）"],
    },
    {
        "id": "compare-cluster",
        "title": "多组比较（compareCluster）",
        "keys": ["compare", "comparison", "比较", "多组", "comparecluster", "多个样本",
                 "多组学", "分组比较"],
        "steps": [
            "library(clusterProfiler)",
            "ck <- compareCluster(entrez ~ cluster, data = deg, fun = 'enrichGO',",
            "                     OrgDb = org.Hs.eg.db, ont = 'BP')",
            "dotplot(ck, showCategory = 5)",
            "cnetplot(ck, showCategory = 5)",
        ],
        "notes": ["fun 可换 'enrichKEGG' / 'enrichWP' / 'enrichMKEGG' / 'enricher' / 'gseGO'",
         "data 必须含 ID 列（formula 左侧）和分组列（formula 右侧）",
         "cluster 列因子水平顺序决定出图分组顺序",
         "结果用 as.data.frame(ck) 可拆成每组单独看"],
    },
    {
        "id": "id-convert",
        "title": "基因 ID 转换（bitr / bitr_kegg）",
        "keys": ["id", "转换", "id转换", "bitr", "bitr_kegg", "symbol", "entrez",
                 "ensembl", "id mapping", "基因id", "idmap", "idmap"],
        "steps": [
            "library(clusterProfiler)",
            "idmap <- bitr(deg$gene_id, fromType = 'SYMBOL', toType = c('ENTREZID','ENSEMBL'),",
            "               OrgDb = org.Hs.eg.db)",
            "idmap_kegg <- bitr_kegg(deg$gene_id, fromType = 'ncbi-geneid',",
            "                         toType = 'kegg', organism = 'hsa')",
        ],
        "notes": ["toType 可以是单个或向量，会一次性多列输出",
         "bitr 依赖 OrgDb；bitr_kegg 走 KEGG API（需要联网）",
         "同一物种的 OrgDb 必须装（人 org.Hs.eg.db / 鼠 org.Mm.eg.db ...）"],
    },
    {
        "id": "david-ora",
        "title": "DAVID 注释服务 ORA（enrichDAVID）",
        "keys": ["david", "david富集", "david 注释", "enrichdavid"],
        "steps": [
            "library(clusterProfiler)",
            "ed <- enrichDAVID(gene = gene, idType = 'ENTREZ_GENE_ID',",
            "                  listType = 'Gene',",
            "                  uploadKb = 25, # 选最近一次的 DAVID release",
            "                  davidUser = 'your@email.com')    # 注册 DAIVD 后会发 token",
        ],
        "notes": ["需要先注册 DAVID 账号（免费）：https://david.ncifcrf.gov/",
         "davidUser 是注册邮箱，DAVID 会往该邮箱发 confirmation",
         "如果上传失败，去 DAVID 网站手动提交基因 list，把 result 文件读进 R",
         "DAVID 是老牌工具，但 2022 年起功能受限；新项目建议用 enrichKEGG/enrichGO"],
    },
    {
        "id": "id-type",
        "title": "查看 / 设置 enrichResult 的 keyType（idType）",
        "keys": ["idtype", "keytype", "查看类型", "id 类型", "keytype 设置"],
        "steps": [
            "library(clusterProfiler)",
            "idType(ego)            # 看当前 keyType（ENTREZID / SYMBOL / UNKNOWN）",
            "x <- setReadable(ego, OrgDb = org.Hs.eg.db, keyType = 'ENTREZID')",
            "idType(x)              # 现在是 SYMBOL",
        ],
        "notes": ["UNKNOWN 表示 clusterProfiler 没识别出来（输入向量没名字或没 keytype 信息）",
         "setReadable() 会把 result 里的 geneID 列从 ENTREZID 转成 SYMBOL",
         "setReadable 适用于 enrichResult / gseaResult / compareClusterResult"],
    },
    {
        "id": "nsea",
        "title": "网络感知 GSEA（NSEA，nseaGO / nseKEGG）",
        "keys": ["nsea", "网络拓扑", "拓扑感知", "nse", "网状", "nseKEGG", "网络gsea",
                 "network gsea"],
        "steps": [
            "library(clusterProfiler); library(enrichit)",
            "g <- build_kegg_graph('hsa')      # 或 build_go_graph('BP', org.Hs.eg.db)",
            "nse <- nseGO(gl, OrgDb = org.Hs.eg.db, ont = 'BP', graph = g)",
            "dotplot(nse, showCategory = 10)",
        ],
        "notes": ["NSEA 在 GSEA 基础上加 PPI / pathway 网络拓扑信息",
         "graph 用 igraph 对象（STRING / KEGG / 自定义网络都行）",
         "速度比普通 GSEA 慢，基因 / 节点多时慎用"],
    },
    {
        "id": "mnsea",
        "title": "多层网络 GSEA（mnseaGO / mnseKEGG）",
        "keys": ["mnsea", "多层网络", "multi-layer", "multi layer", "multiplex",
                 "mnse"],
        "steps": [
            "library(clusterProfiler); library(enrichit)",
            "g1 <- build_kegg_graph('hsa'); g2 <- build_string_graph('9606')",
            "mnet <- merge_graphs(g1, g2)",
            "mnse <- mnseGO(gl, OrgDb = org.Hs.eg.db, ont = 'BP', graphs = list(g1, g2))",
            "dotplot(mnse, showCategory = 10)",
        ],
        "notes": ["用于整合多个网络层（pathway / PPI / coexpression ...）",
         "传 graphs=list(g1, g2, ...) 而不是单个 graph",
         "输出额外列可追溯每层贡献度"],
    },
    {
        "id": "bayes",
        "title": "贝叶斯 term 选择（bayes_enrich）",
        "keys": ["bayes", "贝叶斯", "bayes_enrich", "bayesian", "term选择",
                 "term selection"],
        "steps": [
            "library(clusterProfiler); library(enrichit)",
            "ego <- enrichGO(gene, OrgDb = org.Hs.eg.db, ont = 'BP')",
            "be <- bayes_enrich(ego, candidate = 'top', n_terms = 200, n_perm = 5000)",
            "bayes_summary(be, active = TRUE, n = 30)",
        ],
        "notes": ["贝叶斯 term 选择是 ORA p-value 之外的二次筛选",
         "prior / false_positive / false_negative 三个概率参数必须 in (0,1)",
         "burnin 与 thin 控制 MCMC 收敛；CPU 紧就调小"],
    },
    {
        "id": "merge-result",
        "title": "合并多组富集结果（merge_result）",
        "keys": ["merge", "合并", "合并结果", "merge_result", "combine"],
        "steps": [
            "library(clusterProfiler)",
            "m <- merge_result(list(A = ego1, B = ego2, T = ego3))",
            "dotplot(m, showCategory = 10)",
        ],
        "notes": ["输入是 list(enrichResult)；按 GO/KEGG ID 合并",
         "输出仍是一个 enrichResult，可用同一套 dotplot/cnetplot"],
    },
    {
        "id": "gson-offline",
        "title": "离线 GO/KEGG 数据库（GSON）",
        "keys": ["gson", "离线", "offline", "离线 kegg", "离线 go", "build_gson",
                 "本地 gson", "gson_go", "gson_kegg"],
        "steps": [
            "library(clusterProfiler)",
            "# GO 本地（按 organism + ontology）",
            "gson <- gson_GO(org.Hs.eg.db, ont = 'BP')",
            "# KEGG 本地",
            "gson_kegg <- gson_KEGG('hsa', KEGG_Type = 'KEGG', keyType = 'kegg')",
            "# 给 enrichGO / enrichKEGG 用",
            "ego <- enrichGO(gene, gson = gson)",
            "ek <- enrichKEGG(gene, organism = gson_kegg)",
        ],
        "notes": ["GSON 把 GO.db / KEGG 缓存成单一变量，下次无需联网",
         "KEGG GSON 体积较大（200-500MB），保存为 RDS 复用",
         "offline 后 batch 跑几十次分析非常快"],
    },
    {
        "id": "ppi",
        "title": "蛋白互作网络（getPPI / STRING）",
        "keys": ["ppi", "蛋白互作", "string", "string-db", "getppi", "network"],
        "steps": [
            "library(clusterProfiler)",
            "g <- getPPI(ego, ID = 1)             # igraph 对象",
            "plot(g)",
            "df <- getPPI(ego, output = 'data.frame')",
        ],
        "notes": ["getPPI 走 STRING 数据库 API（https://string-db.org）",
         "需要联网；taxID 自动从 enrichResult@organism 推",
         "required_score 控制阈值（默认 NULL，按网络类型 default）"],
    },
    {
        "id": "llm-interpret",
        "title": "LLM 自动解读富集结果（interpret）",
        "keys": ["llm", "interpret", "解读", "gpt", "openai", "ai 解读",
                 "automatic interpretation", "interpretation"],
        "steps": [
            "library(clusterProfiler)",
            "interpret(ego, organism = 'Homo sapiens',",
            "          provider = 'openai', model = 'gpt-4o',",
            "          api_key = Sys.getenv('OPENAI_API_KEY'))",
            "# 输出 markdown 解释 + 图形",
            "# 批量：interpret_agent(ego_list, ...)",
        ],
        "notes": ["interpret 用 LLM（aisdk 后端）解释 GO/KEGG 生物学意义",
         "需配置 OPENAI_API_KEY（或走 ollama 本地模型）",
         "interpret_hierarchical 在层级里把概念聚合",
         "cost 用 4o + 100 GO 通路约 $0.1-0.3；本地 ollama 免费"],
    },
    {
        "id": "uniprot",
        "title": "Uniprot ID 转换（uniprot_get）",
        "keys": ["uniprot", "uniprot_get", "蛋白质 id", "protein id"],
        "steps": [
            "library(clusterProfiler)",
            "u <- uniprot_get('P53', from = 'GENENAME', to = 'ACC')",
        ],
        "notes": ["Uniprot API 是 POST 请求，比 bitr 慢",
         "适用蛋白组学 ID 转换场景"],
    },
]


def score(plan, q):
    ql = q.lower()
    s = 0
    for k in plan["keys"]:
        if k.lower() in ql:
            s += max(2, len(k))
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", help="一句话需求")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    if a.list:
        for p in PLANS:
            print("%-20s %s" % (p["id"], p["title"]))
        return 0
    if not a.query:
        ap.print_help()
        return 2

    ranked = sorted(((score(p, a.query), p) for p in PLANS),
                    key=lambda x: -x[0])
    hits = [(s, p) for s, p in ranked if s > 0]
    if not hits:
        sys.stderr.write("没有匹配到已知流程，试试 --list 看支持哪些，或换个说法\n")
        return 1

    if a.json:
        print(json.dumps([{"id": p["id"], "title": p["title"], "score": s,
                           "steps": p["steps"], "notes": p["notes"]}
                          for s, p in hits[:3]], ensure_ascii=False, indent=2))
        return 0

    print("需求: %s" % a.query)
    print()
    for s, p in hits[:3]:
        print("== %s  （匹配度 %d）" % (p["title"], s))
        for i, st in enumerate(p["steps"], 1):
            print("   %d. %s" % (i, st))
        if p["notes"]:
            print("   注意:")
            for nt in p["notes"]:
                print("     - %s" % nt)
        print()
    print("完整代码模板见 references/workflows.md；写完后必须跑 tools/cp_lint.py 校验。")
    return 0


if __name__ == "__main__":
    sys.exit(main())