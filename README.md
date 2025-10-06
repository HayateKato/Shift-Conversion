# Shift Conversion

- バイトのシフト予定を自動でGoogleカレンダーに追加するアプリケーションを作成するプロジェクトです．
- Notion記事(https://gregarious-lumber-950.notion.site/259c7af0e3de80599b61e9cdb2746603?source=copy_link)


## Requirement
- Python 3.11.12


## Usage
- アプリケーションをDockerコンテナとして実行します．
  - `src/result/[日付][実行時刻]/` 下に実行結果とログが出力されます．
```shell
docker compose up
```


## Directory Structure
- プロジェクトの構成は以下の通りです．
```shell
.
├── src                         # ソースコードを格納するディレクトリ
│   ├── dataclass               # データクラス定義ファイルを格納するディレクトリ
│   │   ├── file.py             # Fileクラスの定義
│   │   └── shift.py            # Shiftクラスの定義
│   ├── image_processor         # 画像処理ファイルを格納するディレクトリ
│   │   ├── image_processor.py  # 画像からシフトデータを作成
│   │   ├── shift_parser.py     # 画像処理後のデータをShiftオブジェクトに変換
│   │   └── vision_client.py    # 画像処理を実施
│   ├── result                  # 結果出力ディレクトリ
│   │   └── 20211026_165841
│   ├── calendar_client.py      # Googleカレンダーとのやりとりを管理
│   ├── config.py               # パラメータ定義
│   ├── controller.py           # アプリケーション全体を管理
│   ├── main.py                 # 実行ファイル
│   ├── slack_client.py         # Slackとのやりとりを管理
│   └── utils.py                # 共有関数群
├── .gitignore                  # gitの非追跡対象を定義するファイル
├── Dockerfile                  # Dockerイメージファイル
├── docker-compose.yml          # Dockerコンテナ構成ファイル
└── requirements.txt            # 必要ライブラリ
```