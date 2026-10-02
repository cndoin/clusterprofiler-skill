# clusterprofiler-skill · YuLab-SMU R エコシステム向けスキル

<p align="center"><img src="docs/clusterprofiler-skill.svg" alt="スキルのワークフロー" width="900"></p>

**38 パッケージ · API 許可リスト 6,137 件 · オフライン Python ツール · セルフチェック 19/19 合格**

AI エージェントが YuLab-SMU のバイオインフォマティクス R エコシステムを使って解析を作成、検査、計画、実行するためのクロスエージェントスキルです。API インデックスは上流の `NAMESPACE` と R ソースのシグネチャから生成されます。`cp_lint.py` が R スクリプトを提出前に検査します。

## 主な機能

- `cp_lint.py`：オフラインで R スクリプトを検査し、未知の関数、シグネチャが分かる場合の不正な引数、よくある誤記、構文、全角記号を検出します。
- `cp_api.py`：ローカルの API インデックスから実際のシグネチャを検索します。
- `cp_plan.py`：自然言語の依頼から解析手順と関数を提案します。
- YuLab-SMU エコシステム 38 パッケージ、6,137 キーを収録。3,087 件は仮引数を解析済みです。
- `scripts/run_cp.R` は実際の R パッケージを呼び出します。Python が解析結果を捏造することはありません。

## クイックスタート

```bash
python3 install.py --host codex       # claude、workbuddy、deepseek にも対応
python3 tools/selftest.py             # 19 項目を検証
python3 tools/cp_lint.py analysis.R --json
```

Windows で `python3` が使えない場合は `python` を使用してください。Python ツールは標準ライブラリのみを使用します。実際に解析を実行するには R と関連する Bioconductor/CRAN パッケージが必要です。[インストールガイド](INSTALL.md)を参照してください。

セルフチェックは R の回帰 fixture 9 件、ドキュメントのコードブロック 44 件、ツールの簡易テスト、API インデックスの整合性を確認し、**19/19 合格**です。検証環境に R がなかったため、実際の R 解析は実行していません。

## ドキュメント

[英語トップページ](README.md) · [インストール](INSTALL.md) · [スキル指示](SKILL.md) · [変更履歴](CHANGELOG.md)

本プロジェクトは独立したコミュニティスキルであり、YuLab-SMU または clusterProfiler の公式製品ではありません。ライセンスと帰属は [NOTICE](NOTICE) を参照してください。
