# clusterprofiler-skill · YuLab-SMU R 生物信息学生态技能

<p align="center"><img src="docs/clusterprofiler-skill.svg" alt="技能工作流程图" width="900"></p>

**38 个生态包 · 6,137 个 API 白名单键 · 离线 Python 工具 · 自检 19/19 通过**

这是一个供 AI Agent 使用的跨宿主技能，帮助编写、检查、规划和运行 YuLab-SMU 生物信息学 R 包生态中的分析。API 索引由上游 `NAMESPACE` 和 R 源码签名生成；`cp_lint.py` 在交付 R 脚本前检查函数名、已知参数、常见拼写错误、语法和全角符号。

## 功能

- `cp_lint.py`：离线检查 R 脚本，避免编造生态包函数和参数。
- `cp_api.py`：离线查询生成的真实 API 签名。
- `cp_plan.py`：根据自然语言需求推荐分析步骤和函数。
- 覆盖 38 个 YuLab-SMU 生态包，索引含 6,137 个键，其中 3,087 个解析出正式参数。
- `scripts/run_cp.R` 调用真实 R 包执行分析；Python 不会伪造分析结果。

## 快速开始

```bash
python3 install.py --host codex       # 也支持 claude、workbuddy、deepseek
python3 tools/selftest.py             # 19 项自检
python3 tools/cp_lint.py analysis.R --json
```

Windows 如果没有 `python3`，请使用 `python`。Python 工具只依赖标准库；实际运行 R 分析需要安装 R 及相应的 Bioconductor/CRAN 包，见 [安装指南](INSTALL.md)。

自检包含 9 个 R 回归夹具、44 个文档代码块、工具冒烟检查和 API 索引完整性检查，当前 **19/19 通过**。本次环境没有安装 R，因此没有执行实际 R 分析。

## 文档

[英文主页](README.md) · [安装指南](INSTALL.md) · [技能说明](SKILL.md) · [变更记录](CHANGELOG.md)

本项目是独立社区技能，不是 YuLab-SMU 或 clusterProfiler 官方产品。许可证和上游归属请见 [NOTICE](NOTICE)。
