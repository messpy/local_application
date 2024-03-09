import dropbox
import requests
import json



def get_json(filename="data.json",key="test"):
    with open(filename, 'r') as file:
        data = json.load(file)
        if key in data:
            return data[key]
        else:
            print(f"Error: Key '{key}' not found in JSON file.")
            return None




def send_discord(webhook_url,msg, image_path="" ):
    print("Discodeに送信中")
    try:
        with open(image_path, 'rb') as image_file:
            payload = {
                "content": msg,
                "file": image_file
            }
            response = requests.post(webhook_url, files=payload)
            response.raise_for_status()
            print("Image sent successfully")
    except FileNotFoundError:
        print("File not found.")
    except requests.exceptions.RequestException as err:
        print(f"Error sending image via : {err}")




def send_line(token,msg):
        print("LINEに送信中")
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization" : "Bearer "+ token}
        payload = {"message" :  msg}
        r = requests.post(url, headers = headers, params=payload)



def send_discord_audio(webhook_url, fle_path):
    files = {'file': open(fle_path, 'rb')}
    response = requests.post(webhook_url, files=files)
    
    if response.status_code == 200:
        print('音声ファイルを送信しました。')
    else:
        print(f'エラー: {response.status_code}')


"""

msg = "hello~test"
json_fle = "data.json"
line_id = read_json_file(json_fle, "line")
send_line(line_id,msg)

discord_id = read_json_file(json_fle, "discord")
send_discord(discord_id,msg)
"""







"""
def dropbox_dl(ACCESS_TOKEN):
    # Dropboxアクセストークンを設定
 
    # ダウンロード先のフォルダ
    DOWNLOAD_DIR = '/home/kent/Remoto/iPhone'

    # Dropboxとの接続
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    # `raspi`フォルダ内のエントリ一覧を取得
    entries = dbx.files_list_folder('/Raspi')

    # 各エントリをダウンロード
    for entry in entries.entries:
        # ファイルの場合
        if isinstance(entry, dropbox.files.FileMetadata):
            # ファイル名
            filename = entry.name

            # ダウンロードパス
            download_path = os.path.join(DOWNLOAD_DIR, filename)
            download_path = DOWNLOAD_DIR.replace('\\', '/') + '/' + filename


            # ファイルダウンロード
            with open(download_path, 'wb') as f:
                metadata, res = dbx.files_download(entry.path_lower)
                f.write(res.content)
                

    # 処理完了
    print('ダウンロード処理が完了しました。')

"""
