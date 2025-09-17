# Shift Conversion

バイトのシフト予定を自動でGoogleカレンダーに追加するアプリケーションを作成するプロジェクトです．


## Requirement
- Python 3.11.12


## Installation
- 結果出力用ディレクトリを作成
```shell
mkdir result
```
- 各種モジュールのインストール
```shell
pip install -r requirements.txt
```


## Usage
- メインプログラムを実行．
  - `result/[日付][実行時刻]/` 下に実行結果とログが出力されます．
```shell
python main.py
```
- デフォルトのパラメータ設定をjson出力．
```shell
python config.py  # parameters.jsonというファイルが出力される．
```
- 以下のように，上記で生成されるjsonファイルの数値を書き換えて，実行時のパラメータを指定できます．
```shell
python main.py -p parameters.json
```
- 詳しいコマンドの使い方は以下のように確認できます．
```shell
python main.py -h
```


## Parameter Settings

- 指定できるパラメータは以下の通り．
```json
{
    "param1": 0,    # ダミーのパラメータ1
    "param2": {     # ダミーのパラメータ2
        "k1": "v1",
        "k2": "v2"
    }
}
```

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── dataclass                 # データクラス定義ファイルを格納するディレクトリ
│   │── file.py               # Fileクラスの定義
│   └── shift.py              # Shiftクラスの定義
├── image_processor           # 画像処理ファイルを格納するディレクトリ
│   │── image_processor.py    # 画像からシフトデータを作成
│   │── shift_parser.py       # 画像処理後のデータをShiftオブジェクトに変換
│   └── vision_client.py      # 画像処理を実施
├── config.py                 # パラメータ定義
├── main.py                   # 実行ファイル
├── parameters.json           # パラメータ指定用ファイル
├── result                    # 結果出力ディレクトリ
│   └── 20211026_165841
└── utils.py                  # 共有関数群
```
