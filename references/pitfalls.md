# clusterProfiler 常见坑

> 每个坑都是真撞过的，不是网上拼凑。

---

## 1. 物种 / OrgDb / KEGG code 三套命名别搞混

| 来源 | 命名体系 | 例 |
| --- | --- | --- |
| `enrichKEGG` / `gseKEGG` 的 `organism` | KEGG 三字母代码 | `hsa` / `mmu` / `dre` |
| `enrichWP` 的 `organism` | Latin 学名 | `Homo sapiens` / `Mus musculus` |
| `enrichGO` / `gseGO` 的 `OrgDb` | Bioconductor 包名 | `org.Hs.eg.db` / `org.Mm.eg.db` |

把 Latin 学名喂给 `enrichKEGG` 是 LLM 写脚本时**最常犯的错**：
结果基因全部映射成 UNKNOWN，enrichResult @result 全空。

修复：

```r
# 查 KEGG 代码
search_kegg_organism("Homo sapiens")    # 找 "hsa"
# 查 WikiPathways organism
get_wp_organisms()                       # 找 "Homo sapiens"
```

---

## 2. ID 类型不一致 → result 全空

enrichGO 的 `keyType` 与输入 gene 必须是同一类，否则映射失败。

```r
gene_symbol <- c("TP53", "BRCA1", "EGFR")
ego <- enrichGO(gene_symbol, OrgDb = org.Hs.eg.db,
               keyType = "ENTREZID")     # 错！SYMBOL 当 ENTREZID
# 结果 @result 为 0 行，但 enrichGO 不报错
```

**排错**：

```r
head(geneSymbol)                    # 看 ID 是不是 ENTREZ 数字
# SYMBOL 数字开头或全大写 / 短字符
# ENTREZID 全是数字

ego <- enrichGO(gene, keyType = "SYMBOL", ...)   # 改对 keyType
# 或 bitr 先转
```

---

## 3. KEGG 网络限制

KEGG API（api.kegg.jp）在国内网络经常 timeout；第一次跑会等很久。

对策：

1. **离线 GSON**（推荐）：第一次联网下 `gson_KEGG("hsa")`，存盘，后续用
   `readRDS(...)` + `enrichKEGG(organism=gson)`。整个 KEGG 比上 GSON 大
   （~200-500MB / KEGG_Type），一次下完终身用。
2. **重试 + 超时**：cp_lint 不查，但脚本里 `tryCatch` 包一下 enrichKEGG。
3. **用 WikiPathways / ReactomePA 替代**：数据更接近 Reactome / OpenTargets。

---

## 4. OrgDb 没装 → enrichGO 报 `there is no package called 'org.Hs.eg.db'`

```r
BiocManager::install("org.Hs.eg.db")    # Bioconductor 数据包
```

**物种 OrgDb 命名规则**：
- 人 `org.Hs.eg.db`
- 鼠 `org.Mm.eg.db`
- 斑马鱼 `org.Dr.eg.db`
- 果蝇 `org.Dm.eg.db`
- 酵母 `org.Sc.sgd.db`
- 拟南芥 `org.At.tair.db`
- 大鼠 `org.Rn.eg.db`
- 线虫 `org.Ce.WormBase`
- 牛 `org.Bt.eg.db`
- 犬 `org.Cf.eg.db`
- 鸡 `org.Gg.eg.db`
- 黑猩猩 `org.Pt.eg.db`
- 猪 `org.Ss.eg.db`
- 恒河猴 `org.Mmu.eg.db`
- 大肠杆菌 `org.EcK12.eg.db`
- 疟原虫 `org.Pf.plasmo.db`
- 铜绿假单胞菌 `org.Paeruginosa`
- 弓形虫 `org.Tgondii.eg.db`

找不到时去 https://bioconductor.org/packages/release/BiocViews.html#___OrgDb
查完整列表。

---

## 5. GSEA 的 keyType 与 `names(geneList)` 不匹配

```r
gseGO(gl, OrgDb = org.Hs.eg.db, ont = "BP", keyType = "ENTREZID")
# Error: No gene can be mapped
# 因为 names(gl) 是 SYMBOL
```

修复：

```r
# 改 keyType
gseGO(gl, ..., keyType = "SYMBOL")
# 或转 ID
gl_entrez <- setNames(gl, bitr(names(gl), fromType="SYMBOL",
                               toType="ENTREZID", OrgDb=org.Hs.eg.db)$ENTREZID[match(names(gl), ...)])
```

---

## 6. compareCluster 的 fun 参数

**fun 只接受字符串**："enrichGO" / "enrichKEGG" / "enrichWP" / "enrichMKEGG"
/ "enrichPC" / "enrichDAVID" / "enricher" / "gseGO" / "gseKEGG" / "gseWP" ...

不是 R 函数本身。所以 `fun=enrichGO`（没引号）也是合法（自动 as.character）但
`fun=function(x) ...` 是不行的。

透传：compareCluster 接受 `...` 透传给 fun。`OrgDb` / `ont` 等参数走 `...` 路径。
cp_lint 对此会降为 warning，不是 error。

---

## 7. simplify 必须有 GOSemSim

```r
ego_s <- simplify(ego)
# Error: GOSemSim ... not installed
```

修复：装 GOSemSim + 提供 semData：

```r
library(GOSemSim)
sem_data <- godata("BP", "hsapiens")
ego_s <- simplify(ego, semData = sem_data)
```

---

## 8. 中文路径 / 空格路径报错

R 在 Windows 上对 UTF-8 路径敏感，工作目录含中文 / 空格时，`saveRDS` /
`pdf()` / `read.csv()` 常失败。

```
workspace := "D:/projects/中文分析/"   # ❌
workspace := "D:/projects/cp_run/"   # ✅
```

---

## 9. interpret 的真实签名（不是 LLM 以为的）

**错误**（注释引导 cp_lint 跳过；这是反面案例）：

```r
# BAD: 以下三行全是 clusterProfiler 4.21+ 不接受的旧 API
interpret(ego, organism = "Homo sapiens",
          provider = "openai", model = "gpt-4o",
          api_key = Sys.getenv("OPENAI_API_KEY"))
# Error in interpret(...): unused argument (organism, provider, api_key)
```

**正确**：

```r
interpret(ego, model = "gpt-4o", task = "summarize")
# API key 走环境变量：Sys.setenv(OPENAI_API_KEY = "...")
# provider 不需要指定，aisdk 后端自动从环境变量选
```

LLM 的训练数据里 clusterProfiler 老版本的 interpret 接受 `organism/provider/api_key`，
新版本（≥4.20）已重写，必须按新签名调。

---

## 10. NSEA 必须传 graph

```r
nseGO(gl, OrgDb = org.Hs.eg.db, ont = "BP")
# Error: graph is required
```

```r
g <- build_kegg_graph("hsa")
nseGO(gl, OrgDb = org.Hs.eg.db, ont = "BP", graph = g)
```

`build_*_graph()` 在 enrichit 包里。

---

## 11. enrichResult 是 S4 对象

```r
ego$ID                       # 错！S4 不能用 $
ego@result$ID                # 对：直接拿 slot
as.data.frame(ego)$ID        # 对：用 S3 转换
```

`show(ego)` 看 slots：`result` / `gene` / `geneSets` / `keytype` /
`organism` / `ontology` / `universe` / `readable` / `method` / `gene2Symbol` ...

---

## 12. dotplot 报 `unused argument (split=)`

`dotplot()` 没有 `split` 参数。要分面用 ggplot2 `facet_wrap()`：

```r
dotplot(ggo, showCategory = 10) + facet_wrap(~ sign, ncol = 2)
```

---

## 13. compareCluster 的 data 必须含 formula 全部变量

```r
compareCluster(entrez ~ cluster, data = deg)
# 'entrez' 不在 deg → NA 行被丢弃，整组无结果
```

确保 `deg` 里有 `entrez` 和 `cluster` 两列。

---

## 14. 内存爆 / 跑 30+ 分钟

- 基因集大：`gsfilter(ego, by="GSSize", max=200)`
- GSEA 太慢：`nPerm=1000` 改 `nPerm=100`（显著性估计会粗糙一些）
- 大数据 NSEA：先 `prepare_network()` 缓存网络拓扑
- enrichit 后台 C++：换机器或并行 `library(BiocParallel); register(...)`

---

## 15. LLM 写 clusterProfiler 代码时最常犯的 10 个错（已实测）

| 序号 | 错误 | 正确 |
| --- | --- | --- |
| 1 | `enrichGO(fdr_method=)` | `pAdjustMethod` |
| 2 | `enrichGO2()` | `enrichGO()` |
| 3 | `compareCluster(fun="enrichGOO")` | `fun="enrichGO"` |
| 4 | `dotplot(split=...)` | 去掉 split；用 `facet_wrap` |
| 5 | `organism = "Homo sapiens"` 喂给 enrichKEGG | `organism = "hsa"` |
| 6 | `interpret(..., organism=, provider=, api_key=)` | `interpret(..., model=)` + 环境变量 |
| 7 | `simplify` 当成函数调用 | `simplify(ego)` —— 是 S4 method |
| 8 | `dotplot(width=)` | dotplot 没 width；用 `pdf()` 控制 |
| 9 | `gseGO` 不传 OrgDb | 必须传 OrgDb |
| 10 | `bitr(fromType="WRONG")` | fromType 必须是 KEYTYPE 之一 |

cp_lint 把所有这些都拦下来了。**没跑 lint 就提交 = 翻车。**