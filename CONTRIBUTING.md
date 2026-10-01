# 贡献指南

## 改这个技能前必读

clusterprofiler-skill 是**事实底座驱动**的 skill —— 它的全部权威来自
`tools/whitelist.json` 和 `references/*.md`，而这两个文件又来自
`tools/etl/` 链路对 `YuLab-SMU/clusterProfiler@devel` 源码的解析。

**任何手动编辑 references/api-whitelist.json 都是不安全的**，必须由
`tools/etl/rebuild.py` 重新生成。

---

## 工作流程

```
1. 改上游源码？     → 跑 python3 tools/etl/rebuild.py
2. 改工具（lint / api / plan）？  → 跑 python3 tools/selftest.py 全绿
3. 加新 fixtures？  → 先写 .R，再补 EXPECT 表，最后跑 selftest.py
4. 改 SKILL.md / references/*.md 文档？  → 跑 selftest.py 校验文档里的 R 代码块
```

---

## 加新的 fixture（自检用例）

1. 在 `tests/fixtures/` 下加 `<NN>_<descriptive_name>.R`
2. 期望表 `EXPECT` 加一行（`tools/selftest.py` 顶部 dict）：
   - `(exit_code, {"code": count, ...})` —— 期望的退出码 + 期望的错误 code 计数
   - exit_code 0 = 期望 PASS；exit_code 1 = 期望 FAIL
3. 跑 `python3 tools/selftest.py`，确认这条 fixture PASS

示例：

```python
EXPECT["06_my_fixture.R"] = (1, {"unknown-function": 1})
```

---

## 加新的 clusterProfiler 函数到 whitelist

如果上游新增了导出函数，但 `tools/whitelist.json` 还没收录：

1. 跑 `python3 tools/etl/rebuild.py --ref <新版本号>` 重新生成
2. 检查 `tools/whitelist.json` 是否包含新函数 + formals
3. 跑 `python3 tools/selftest.py`，特别是 fixtures 和文档代码块都 PASS
4. （可选）在 `tools/cp_plan.py` 里加新流程模板（如果新函数对应新场景）
5. （可选）在 `references/workflows.md` 里加新代码示例

---

## 修复 cp_lint 的 false positive / false negative

`cp_lint.py` 是基于源码 formals 做严格匹配的，所以：

- **false positive（误报 unknown-function）**：可能是第三方包函数没在
  `THIRD_PARTY_PARAMS` 里。把函数名 + 形参加进 `tools/etl/build_api.py` 的
  `THIRD_PARTY_PARAMS` dict，再 `rebuild.py` 重建。
- **false positive（误报 unknown-arg）**：把缺失的参数名加进 whitelist；
  上面同样路径。
- **false negative（漏报）**：通常是 scan_calls 的词法分析 bug，
  改 `tools/cp_lint.py` 的 `scan_calls()` 函数。常见 bug 模式：
  - 换行处没 flush 当前 ident（**已修复**：2026-10-01）
  - `<-` 后没 reset cur
  - 反引号标识符没识别

跑 `python3 tools/selftest.py` 验证修复没引入回归。

---

## 改 SKILL.md

SKILL.md 是 Agent 的常驻入口。修改时注意：

1. **description 字段**（YAML frontmatter 第一段）是 Claude Code 触发 skill 的关键字。要含：
   - skill 名（clusterProfiler）
   - 关键场景（GO / KEGG / GSEA / 多组学 / 离线 / LLM）
   - 触发短语（enrichment / gene / pathway / 富集 / 通路 / ORA / GSEA / ...）
2. **路由表（第三节）** 必须覆盖常用任务。改完跑 selftest.py 验证代码示例能 PASS。
3. **铁律（第一节）** 是基于实测的，不要随便加"通用建议"。每条铁律都要能
   在 `references/pitfalls.md` 找到对应解释。
4. **不要写**绝对路径（`/usr/local/...`）或宿主专属命令。保持通用。

---

## 跨平台 / 跨宿主义务

1. 所有路径一律**相对 skill 根目录**写（`tools/cp_lint.py` 不是 `/usr/local/bin/cp_lint`）。
2. 命令统一写 `python3`（用户在 Windows 上若没 python3，会自己换成 python）。
3. 不调用 `os.path.expanduser` 除非用户显式传 `~`。
4. 不依赖非标第三方 Python 包（只有标准库）。
5. R 脚本必须用 `\n` 换行；不要在 Windows 写 CRLF 后被解释成 shebang `\r`。

---

## 发布 / 改动后必跑

```bash
# 1. 重建事实底座
python3 tools/etl/rebuild.py

# 2. 跑全套自检
python3 tools/selftest.py

# 3. 检查 MANIFEST 是否更新（如改了文件结构）
python3 tools/pack.py    # 如果有；或手动更新 MANIFEST.md

# 4. 提交并推送（用户授权后才能 push）
git add -A && git commit -m "feat: ..." && git push
```

`selftest.py` 全绿才能提交。