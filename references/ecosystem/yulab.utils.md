# yulab.utils — 0.2.5

> 数据源：YuLab-SMU/yulab.utils @ master
> 89 个已知符号

## Function (66)

- `as_chunked_array(?)`
- `auto_set_regexpr_style(?)`
- `Biocpkg(pkg)`
- `c2(?)`
- `cache_list_items(?)`
- `cache_load(path)`
- `cache_save(path)`
- `cache_size(?)`
- `check_directory(?)`
- `check_file(?)`
- `check_input(?)`
- `check_packages(?)`
- `check_pkg(?)`
- `check_range(?)`
- `combinations(n)`
- `CRANpkg(pkg)`
- `download_yulab_file(destfile, urls, gzfile=FALSE, appname=NULL)`
- `exec(command)`
- `get_cache(?)`
- `get_cache_element(item, elements, default=NULL, prune_expired=TRUE)`
- `get_cache_item(item)`
- `get_dependencies(pkg, repo=c("CRAN", "BioC"))`
- `get_fun_from_pkg(pkg, fun)`
- `Githubpkg(user, pkg)`
- `has_internet(site="https://www.baidu.com/")`
- `initial_cache(?)`
- `initial_cache_item(item)`
- `install_zip(file, subdir=NULL, args="--no-build-vignettes")`
- `install_zip_gh(repo, ref="HEAD", subdir=NULL, args="--no-build-vignettes")`
- `is.installed(packages)`
- `load_OrgDb(?)`
- `ls2df(inputList)`
- `mat2df(x)`
- `mat2list(x)`
- `mypkg(pkg, url)`
- `o(file=".")`
- `packageTitle(pkg, repo='CRAN')`
- `parse_ratio(ratio)`
- `pload(package, action="auto")`
- `prune_cache_item(item)`
- `quiet(?)`
- `rbindlist(x)`
- `read.cb(reader=read.table, ...)`
- `rm_cache(?)`
- `rm_cache_item(item)`
- `scale_range(data)`
- `scihub_dl(doi, scihub='sci-hub.tw', download=TRUE)`
- `set_PCRE(?)`
- `set_regexpr_style(style)`
- `set_TRE(?)`
- `show_in_excel(.data)`
- `str_detect(string, pattern, negate=FALSE)`
- `str_ends(string, pattern, negate=FALSE)`
- `str_extract(string, pattern)`
- `str_starts(string, pattern, negate=FALSE)`
- `str_wrap(string, width=getOption("width"))`
- `update_cache_item(item, elements, ttl=NULL)`
- `use_perl(?)`
- `user_dir(appname=NULL, appauthor=NULL, ...)`
- `with_cache(item, key, compute, ttl=NULL)`
- `yread(file, reader=readLines, params=list(), cache_dir=NULL)`
- `yread_tsv(file, reader=utils::read.delim, params=list(), cache_dir=tempdir())`
- `yulab_abort(?)`
- `yulab_inform(?)`
- `yulab_msg(pkgname=NULL, n=1)`
- `yulab_warn(?)`

## Generic (1)

- `print(x, ...)`

## Reexport (22)

- `abort(?)`
- `as_name(?)`
- `bibentry(?)`
- `capture.output(?)`
- `check_installed(?)`
- `cli_h2(?)`
- `combn(?)`
- `digest(?)`
- `download.file(?)`
- `enquo(?)`
- `getFromNamespace(?)`
- `inform(?)`
- `is(?)`
- `modifyList(?)`
- `package_dependencies(?)`
- `packageDescription(?)`
- `path_join(?)`
- `read.delim(?)`
- `read.table(?)`
- `setNames(?)`
- `user_data_dir(?)`
- `warn(?)`
