# OpenAI API with Google Docs

本リポジトリは，Google Docs でプロンプトを管理する方法し，Python で OpenAI API を使用するためのテンプレートです．

## 🤖 開発環境・使用技術・ツール

<h3>環境，コード管理
<div>
 <img alt="Docker" src="https://img.shields.io/badge/-Docker-000?style=flat&logo=Docker&logoColor=46a2f1" />
 <img alt="Python" src="https://img.shields.io/badge/-Python-000?style=flat&logo=Python&logoColor=3776AB" />
 <img alt="GitHub" src="https://img.shields.io/badge/-GitHub-000?style=flat&logo=GitHub&logoColor=FFFFFF" />
<img alt="Git" src="https://img.shields.io/badge/-Git-000?style=flat&logo=Git&logoColor=F05032" />
</div>

<h3>外部サービス
<div>
 <img alt="Google Docs" src="https://img.shields.io/badge/-Google Docs-000?style=flat&logo=googledocs&logoColor=4285F4" />
 <img alt="OpenAI API" src="https://img.shields.io/badge/-OpenAI API-000?style=flat&logo=openai&logoColor=ffffff" />
</div>

## 🤖 環境構築・起動

> 環境構築について記載しています．

<details>
<summary>環境構築</summary>

1. `Git` と `Docker Desktop` をインストールしてください．
2. 任意のディレクトリで`git clone https://github.com/273Do/OpenAI-API-with-Google-Docs`を実行してください．
3. `Dockerfile`があるディレクトリ(ルート)に移動します．
4. 移動したディレクトリに`.env`ファイルと`service_account`ディレクトリを作成します．
5. `.env`ファイルに以下を記載してください．

   > OPENAI_API_KEY=
   >
   > DOCUMENT_ID=

6. [こちらの記事](https://mashimashi.net/skill/821)を参考に，Google Cloud Platform にアクセスして，**Google Drive API** と **Google Docs API** を有効化し，認証情報(json ファイル)をダウンロードしてください．
7. ダウンロードした認証情報を`credential.json`とファイル名を変更して，`service_account`ディレクトリに移動させます．
8. Google Drive に 専用テンプレートをコピーし，ドキュメントの URL を取得してください．(テンプレートについては開発者にお問い合わせください．)
9. 取得した URL`https://docs.google.com/document/d/<DOCUMENT_ID>`の`<DOCUMENT_ID>`の部分を控えてください．
10. `.env`ファイルに OpenAI API の API キーと控えた DOCUMENT_ID を記載してください．
11. `Docker Desktop`を起動して，`Dockerfile`があるディレクトリ(ルート)に移動します．
12. `docker compose build`を実行してコンテナイメージを作成します．

</details>

> [!CAUTION]
> .env ファイルと認証情報は絶対に公開しないでください．
>
> <br>

> 起動方法と終了方法について記載しています．

<details>

<summary>起動方法と終了方法</summary>

### 起動方法

1. `Docker Desktop`を起動します．
2. `docker-compose.yml`があるディレクトリ(ルート)に移動します．
3. `docker compose up -d`を実行してコンテナを起動します．(もしくは`Docker Desktop`のコンテナ起動ボタンを押します．)
4. `docker compose exec openai-api-with-google-docs bash`でコンテナの中に入ります．
5. `python3 app.py`でコードが実行できます．

### 終了方法

1. コンテナに入っている場合は`exit`で抜けられます．
2. `docker compose down`を実行してコンテナを終了します．(もしくは`Docker Desktop`のコンテナ終了ボタンを押します．)

</details>

> [!TIP]
> コンテナイメージを作成したら，以降は以下の手順でコンテナを起動するだけで OK です.
> 新たにライブラリや依存関係をインストールする場合は，`requirements.txt`にライブラリを記載して`docker compose build`を実行します．

## 🤖 クレジット・免責事項

- 開発：[273\*](https://www.273doworks.com/)
- この作成物および同梱物を使用したことによって生じたすべての障害・損害・不具合等に関しては，私と私の関係者および私の所属するいかなる団体・組織とも，一切の責任を負いません．各自の責任においてご使用ください．
