# dbt-duckdb-dagster

[Preppin' Data](https://preppindata.blogspot.com/p/the-challenge-index.html) チャレンジのデータを **dbt + DuckDB + Dagster** で処理するパイプラインです。

## 構成

```
dbt-duckdb-dagster/
├── dagster_project/      # Dagster アセット・ジョブ・スケジュール定義
├── dbt_project/          # dbt モデル
│   └── models/
│       ├── 0__raw/       # Google Drive から CSV をロード（Polars）
│       ├── 1__staging/   # 型変換・クリーニング（view）
│       └── 3__marts/     # 集計テーブル（table）
├── data/
│   └── preppin.duckdb    # DuckDB データベースファイル
└── profiles.yml          # dbt 接続設定
```

## 技術スタック

| ツール | バージョン | 用途 |
|---|---|---|
| dbt-core | >=1.8 | データ変換 |
| dbt-duckdb | >=1.8 | DuckDB アダプター |
| DuckDB | >=1.5.2 | ローカル分析用 DB |
| Dagster | >=1.9 | ワークフローオーケストレーション |
| dagster-dbt | >=0.25 | dbt ↔ Dagster 連携 |
| Polars | >=1.0 | Python モデルでの CSV 読み込み |

## セットアップ

```bash
# 依存関係のインストール（uv）
uv sync

# dbt マニフェストの生成（初回・モデル追加時）
cd dbt_project
uv run dbt deps
uv run dbt parse
```

## dbt の実行

```bash
cd dbt_project

# 全モデルをビルド
uv run dbt build

# タグで絞り込み
uv run dbt build --select tag:2023
uv run dbt build --select tag:2019
```

## Dagster の起動

```bash
uv run dagster dev

# バックグラウンド実行
nohup uv run dagster dev > dagster.log 2>&1 &

# バックグラウンド停止
ps aux | grep dagster
kill {{ Dagster PID }}
```

ブラウザで `http://localhost:3000` を開くと Dagster UI にアクセスできます。

### ジョブとスケジュール

| ジョブ | 対象タグ | スケジュール（JST） |
|---|---|---|
| `dbt_2023_job` | `tag:2023` | 毎日 00:05 |
| `dbt_2019_job` | `tag:2019` | 毎日 00:15 |

## データモデル

### レイヤー構成

| レイヤー | マテリアライズ | 説明 |
|---|---|---|
| `0__raw` | table | Google Drive から CSV をダウンロードして DuckDB にロード |
| `1__staging` | view | カラム名の正規化・型変換 |
| `3__marts` | table | ビジネスロジックに基づく集計 |

### データソース

Google Drive 上の CSV ファイルを各 raw モデルが直接ダウンロードします。ファイル一覧は [dbt_project/models/0__raw/2019/README.md](dbt_project/models/0__raw/2019/README.md) を参照してください。

### 実装済みチャレンジ

| 年 | Week | モデル例 |
|---|---|---|
| 2019 | Week 01–46 | `raw__2019_week01__input` |
| 2023 | Week 01 | `raw__2023_week01__transactions` → `stg__2023_week01__transactions` → `mrt__2023_week01__total_by_bank` |

## DuckDB への直接アクセス

```bash
uv run duckdb -ui data/preppin.duckdb
```
