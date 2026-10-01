#!/usr/bin/env Rscript
# preflight.R —— clusterProfiler 运行环境预检，输出 JSON
#
# 用法：
#   Rscript scripts/preflight.R            # 人读
#   Rscript scripts/preflight.R --json     # stdout 只有一个 JSON
#
# stdout 只放数据；人类提示走 stderr。
# 任何 required=TRUE 且 installed=FALSE 的项，都不要带着缺口往下跑。

args <- commandArgs(trailingOnly = TRUE)
json_only <- "--json" %in% args

esc <- function(s) {
  s <- gsub("\\\\", "\\\\\\\\", s)
  s <- gsub('"', '\\\\"', s)
  s
}
jq <- function(s) paste0('"', esc(as.character(s)), '"')

# ---------- 探测 ----------
rver <- paste(R.version$major, R.version$minor, sep = ".")
rnum <- as.numeric(paste(R.version$major,
                         strsplit(R.version$minor, "\\.")[[1]][1], sep = "."))

pkg_info <- function(p) {
  v <- tryCatch(as.character(packageVersion(p)), error = function(e) NULL)
  list(name = p, installed = !is.null(v), version = if (is.null(v)) NA else v)
}

# 包来源映射：conda / cran / bioc / github
PKG_SRC <- c(
  clusterProfiler = "bioc",
  AnnotationDbi = "bioc",
  GO.db = "bioc",
  GOSemSim = "bioc",
  DOSE = "bioc",
  ReactomePA = "bioc",
  gson = "github",
  enrichit = "github",
  enrichplot = "github",
  org.Hs.eg.db = "bioc",
  org.Mm.eg.db = "bioc",
  org.Dm.eg.db = "bioc",
  org.Dr.eg.db = "bioc",
  org.Sc.sgd.db = "bioc",
  org.At.tair.db = "bioc",
  org.Rn.eg.db = "bioc",
  org.Ce.WormBase = "bioc",
  org.Bt.eg.db = "bioc",
  org.Cf.eg.db = "bioc",
  org.Gg.eg.db = "bioc",
  org.Pt.eg.db = "bioc",
  org.Ss.eg.db = "bioc",
  org.Mmu.eg.db = "bioc",
  org.EcK12.eg.db = "bioc",
  org.Pf.plasmo.db = "bioc",
  org.Paeruginosa = "bioc",
  org.Tgondii.eg.db = "bioc",
  aisdk = "github",
  ggplot2 = "cran",
  dplyr = "cran",
  magrittr = "cran",
  rlang = "cran",
  tidyr = "cran",
  plyr = "cran",
  qvalue = "bioc",
  igraph = "cran",
  ggraph = "cran",
  igraph = "cran",
  yulab.utils = "github",
  httr = "cran",
  jsonlite = "cran",
  DOSE = "bioc",
  RDAVIDWebService = "bioc",
  msigdbr = "github"
)

# GitHub 仓库映射
PKG_GH <- c(
  clusterProfiler = "YuLab-SMU/clusterProfiler",
  gson = "GuangchuangYu/gson",
  enrichit = "YuLab-SMU/enrichit",
  enrichplot = "YuLab-SMU/enrichplot",
  aisdk = "YuLab-SMU/aisdk",
  yulab.utils = "YuLab-SMU/yulab.utils",
  msigdbr = "igordot/msigdbr"
)

install_hint <- function(pkg) {
  src <- PKG_SRC[[pkg]]
  if (is.null(src) || is.na(src)) src <- "cran"
  if (src == "bioc") {
    paste0("BiocManager::install('", pkg, "')")
  } else if (src == "github") {
    gh <- PKG_GH[[pkg]]
    if (is.null(gh)) gh <- paste0("YuLab-SMU/", pkg)
    paste0("remotes::install_github('", gh, "')")
  } else {
    paste0("install.packages('", pkg, "')")
  }
}

# 必需：clusterProfiler 主包 + GO.db + enrichit + enrichplot
core <- c("clusterProfiler", "enrichit", "enrichplot", "gson",
          "AnnotationDbi", "GO.db", "GOSemSim", "aisdk",
          "ggplot2", "dplyr", "magrittr", "rlang",
          "httr", "jsonlite", "yulab.utils")

# 可选（species-specific OrgDb / 拓展）
optional <- c("org.Hs.eg.db", "org.Mm.eg.db", "org.Dr.eg.db",
             "DOSE", "ReactomePA", "msigdbr", "igraph", "ggraph",
             "tidyr", "plyr", "qvalue", "RDAVIDWebService")

items <- list()
for (p in core) {
  info <- pkg_info(p)
  info$required <- TRUE
  items[[length(items) + 1]] <- info
}
for (p in optional) {
  info <- pkg_info(p)
  info$required <- FALSE
  items[[length(items) + 1]] <- info
}

# ---------- 系统与资源 ----------
cores <- tryCatch(parallel::detectCores(all.tests = FALSE, logical = TRUE),
                  error = function(e) NA)
mem_gb <- tryCatch({
  if (Sys.info()[["sysname"]] == "Windows") {
    as.numeric(memory.limit()) / 1024
  } else if (file.exists("/proc/meminfo")) {
    l <- readLines("/proc/meminfo", n = 1, warn = FALSE)
    as.numeric(strsplit(l, "\\s+")[[1]][3]) / 1024 / 1024
  } else NA
}, error = function(e) NA)

wd <- getwd()
wd_writable <- tryCatch({
  tf <- file.path(wd, ".cp_preflight_write_test")
  writeLines("ok", tf); unlink(tf); TRUE
}, error = function(e) FALSE)

# ---------- 判定 ----------
hard_fail <- c()
if (isTRUE(rnum < 4.2)) hard_fail <- c(hard_fail,
   "R 版本 < 4.2.0，clusterProfiler 4.21 要求 R >= 4.2.0")
cp_ok <- FALSE
for (it in items) {
  if (it$name == "clusterProfiler" && it$installed) {
    cp_ok <- TRUE
    sv <- it$version
    parts <- as.numeric(strsplit(sv, "\\.")[[1]])
    if (length(parts) >= 2 && parts[1] < 4) {
      hard_fail <- c(hard_fail,
        paste0("clusterProfiler 版本为 ", sv, "，本技能面向 4.20+，旧版 API 差异很大"))
    }
  }
}
if (!cp_ok) hard_fail <- c(hard_fail,
  "未安装 clusterProfiler：请先 BiocManager::install('clusterProfiler')")
if (!wd_writable) hard_fail <- c(hard_fail, paste0("工作目录不可写：", wd))

# ---------- 输出 ----------
pkg_json <- paste(vapply(items, function(it) {
  hint <- if (isTRUE(it$installed)) "null" else jq(install_hint(it$name))
  sprintf('{"name":%s,"required":%s,"installed":%s,"version":%s,"install_hint":%s}',
          jq(it$name),
          if (isTRUE(it$required)) "true" else "false",
          if (isTRUE(it$installed)) "true" else "false",
          if (is.na(it$version)) "null" else jq(it$version),
          hint)
}, character(1)), collapse = ",\n    ")

issues_json <- paste(vapply(hard_fail, jq, character(1)), collapse = ",")

json <- sprintf('{
  "ok": %s,
  "r": {"version": %s, "ok": %s},
  "clusterProfiler": {"installed": %s},
  "workdir": {"path": %s, "writable": %s},
  "system": {"cores": %s, "mem_gb": %s, "os": %s},
  "packages": [
    %s
  ],
  "issues": [%s]
}',
  if (length(hard_fail)) "false" else "true",
  jq(rver), if (isTRUE(rnum >= 4.2)) "true" else "false",
  if (cp_ok) "true" else "false",
  jq(wd), if (wd_writable) "true" else "false",
  if (is.na(cores)) "null" else format(cores),
  if (is.na(mem_gb)) "null" else format(round(mem_gb, 1)),
  jq(Sys.info()[["sysname"]]),
  pkg_json, issues_json)

if (json_only) {
  cat(json, "\n")
} else {
  cat("clusterProfiler 环境预检\n", file = stderr())
  cat(sprintf("  R                  : %s %s\n", rver,
              if (isTRUE(rnum >= 4.2)) "(ok)" else "(版本过低)"), file = stderr())
  cat(sprintf("  clusterProfiler    : %s\n",
              if (cp_ok) {
                v <- items[[which(vapply(items, function(x) x$name, "") == "clusterProfiler"))]]$version
                v
              } else "未安装"), file = stderr())
  miss <- Filter(function(x) x$required && !x$installed, items)
  opt_miss <- Filter(function(x) !x$required && !x$installed, items)
  if (length(miss)) {
    cat("  缺失必需包: ", paste(vapply(miss, function(x) x$name, ""), collapse = ", "),
        "\n", file = stderr())
  }
  cat("  缺失可选包: ", paste(vapply(opt_miss, function(x) x$name, ""), collapse = ", "),
      "\n", file = stderr())
  all_miss <- c(miss, opt_miss)
  if (length(all_miss)) {
    cat("\n  --- 安装命令（按来源，可直接复制）---\n", file = stderr())
    for (it in all_miss) {
      cat(sprintf("    %s      # %s\n", install_hint(it$name),
                  if (isTRUE(it$required)) "必需" else "可选"), file = stderr())
    }
    cat("  提示：clusterProfiler 是 Bioconductor 包，优先走 BiocManager。\n", file = stderr())
  }
  cat(sprintf("  资源      : %s 核 / %s GB / %s\n", cores, round(mem_gb, 1),
              Sys.info()[["sysname"]]), file = stderr())
  cat("\n", file = stderr())
  cat("--- JSON ---\n")
  cat(json, "\n")
}

quit(status = if (length(hard_fail)) 1L else 0L, save = "no")