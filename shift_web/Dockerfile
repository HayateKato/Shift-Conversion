# ベースイメージとしてpython3.11の軽量版を指定
FROM python:3.11-slim

# タイムゾーンを東京に指定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# gitをインストール
RUN apt-get update && apt-get install -y git

# pythonライブラリをインストール
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# コンテナ内のデフォルトディレクトリをsrcディレクトリに指定
WORKDIR /src

# ファイルをデフォルトディレクトリにコピー
COPY ./src /src

# コンテナ起動時にmain.pyを実行
CMD ["python", "main.py"]