# seqmagick — 0.1.9

> 数据源：github.com/YuLab-SMU/seqmagick@devel
> 30 个已知符号

## Function (30)

- `bam2DNAStringSet(bamfile, refseq)`
- `bam2DNAStringSet2(bamfile, refseq)`
- `bs_aln(x, method='muscle', ...)`
- `bs_consensus(x, type="DNA", r=1)`
- `bs_filter(x, pattern, by='description', ignore.case=FALSE)`
- `bs_hamming(x, count_indel=FALSE, ...)`
- `bs_rename(x, mapping, position=NULL, sep=NULL, mode="replace")`
- `clw_read(file, type="auto")`
- `consensus(x, type="DNA")`
- `download_genbank(acc, db="nuccore", format="genbank", outfile=NULL)`
- `fa_combine(file1, file2, outfile=NULL, type="interleaved")`
- `fa_filter(fasfile, pattern, by='description', ignore.case=FALSE, outfile=NULL, type="interleaved")`
- `fa_read(file, type="auto")`
- `fa_rename(fasfile, mapping_file, position=NULL, sep=NULL, mode="replace", outfile)`
- `fa_summary(x)`
- `fa_to_interleaved(file, outfile)`
- `fa_to_sequential(file, outfile)`
- `fa_write(x, outfile, type="interleaved")`
- `fas2phy(fasfile, outfile="out.phy", type="sequential")`
- `gb_read(file)`
- `get_id(x, sep=" ", position)`
- `mega_read(?)`
- `ncbi_fa_read(acc, db="nuccore", type="auto")`
- `phy2fas(phyfile, outfile="out.fas", type="interleaved")`
- `phy_read(file)`
- `phy_write(x, outfile, type="sequential")`
- `renameTXT(txt_file, name_file, sep="_", split=TRUE)`
- `replaceInside(fasfile, from="-", to="N", outfile=NULL)`
- `seqlen(fasfile)`
- `sth_read(file, type="auto")`
