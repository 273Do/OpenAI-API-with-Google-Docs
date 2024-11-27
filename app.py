import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# OpenAI APIのクライアントを初期化
client = OpenAI()

# サービスアカウントの認証情報ファイル
current_dir = os.path.dirname(__file__)
path = f"{current_dir}/service_account/credential.json"
SERVICE_ACCOUNT_FILE = path

# 使用するスコープ(権限)
SCOPES = ["https://www.googleapis.com/auth/documents.readonly"]

# 認証情報の作成
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Google Docs APIのクライアント作成
docs_service = build("docs", "v1", credentials=credentials)

# 読み込むGoogleドキュメントのID
DOCUMENT_ID = os.environ["DOCUMENT_ID"]


# 解析結果を用いてChatGPTでフィードバックを生成する


def generate_feedback(estimate_sleep_df, cluster_stats):

    try:
        # Google Documentsからプロンプトを取得する
        system_prompt, user_prompt, output_format = get_prompt()

        # ChatGPTによるフィードバック生成
        res = client.chat.completions.create(
            model="gpt-4-turbo",  # gpt-4-turboを使用
            # 出力フォーマットを書いたテキストまたはmdファイルを指定する
            messages=[
                {"role": "system",
                 "content": f"{system_prompt}"},
                {"role": "user", "content": (
                    f"{user_prompt}"
                )},
                # 入力データに合わせてcontentを設定してください．
                {"role": "user",
                 "content": f"睡眠データ: {estimate_sleep_df}，歩数クラスタリングデータ: {cluster_stats}，フォーマット: {output_format}"}
            ])

        # フィードバックを取得
        feedback = res.choices[0].message.content
        return True, None, feedback

    except Exception as e:
        return False, str(e), None


# Google Documentsからプロンプトを取得する


def get_prompt():

    # 各プロンプトを格納する変数
    prompt_list = ["", "", ""]

    # 現在のインデックス
    current_index = 0

    try:
        # Google Documentsからプロンプトを取得
        # ドキュメントの内容を取得
        document = docs_service.documents().get(documentId=DOCUMENT_ID).execute()

        # ドキュメントの本文から必要な項目を取得し，格納
        content = document.get("body").get("content")
        for element in content:
            if "paragraph" in element:
                paragraphs = element["paragraph"].get("elements", [])
                for text_run in paragraphs:
                    text = text_run.get("textRun", {}).get("content", "")
                    # 空文字列を検知したら次の変数へ切り替える
                    if text == "":
                        current_index += 1
                        # インデックスがリストの長さを超えた場合は処理を終了
                        if current_index - 1 >= len(prompt_list):
                            break
                    elif text.startswith("//"):
                        # //で始まる行はコメントとして無視
                        break
                    elif current_index >= 1:
                        # ""が最初に検知されて，文字列がある場合，現在の変数に追加
                        prompt_list[current_index - 1] += text

        return True, None, prompt_list

    except Exception as e:
        return False, str(e), None


# プロンプトを出力
success, error_message, result = get_prompt()
if success:
    system_prompt, user_prompt, output_format = result
    print("system_prompt--------------")
    print(system_prompt)
    print("user_prompt----------------")
    print(user_prompt)
    print("format_prompt--------------")
    print(output_format)
else:
    # エラー表示
    print("error--------------")
    print(error_message)

# OpenAI APIを使用してフィードバックを生成
success, error_message, feedback = generate_feedback("test", "test")
if success:
    print("feedback--------------")
    print(feedback)
else:
    # エラー表示
    print("error--------------")
    print(error_message)
