#import pykit_tool
#pykit_tool.send_discord(引数)


import logging
import time
from tkinter import filedialog
import requests


def help():
    mydict = {
        "select_fld()":"fldを選択",
        "select_fle(extension)":"複数ファイル選択",
        "send_discord(webhook_url, msg,img_path)":"画像テキストを[bot]に送る",
        "send_line(token,msg)":"メッセージのみ送信",
        "":""


              }
    print("関数(引数):説明")
    for mykey, myvalue in mydict.items():
        print(f"[{mykey}] {myvalue}")
#


    
def select_fld():
    fld_path = filedialog.askdirectory()
    print(fld_path)
    return fld_path

def select_fle(extension):
    fTyp = [("データファイル",extension )]
    fle_path = filedialog.askopenfiles(filetypes=fTyp)
    print(fle_path)

    return fle_path



# logging_utils.py



def setup_logging(log_file, log_level=logging.INFO):
    """指定されたログファイルとログレベルでロギングを設定します。"""
    # ロガーを作成
    logger = logging.getLogger(__name__)
    print(logger)
    logger.setLevel(log_level)

    # 既にハンドラが存在する場合は削除する
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # ログフォーマットを設定
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # ファイルハンドラを設定
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # コンソールハンドラを設定
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)





def send_discord(webhook_url, msg,img_path):
    try:
        with open(img_path, 'rb') as file:
            files = {'file': file}
            payload = {'content': msg}
            response = requests.post(webhook_url, files=files)
            response.raise_for_status()
            print("Image sent successfully to Discord!")
    except FileNotFoundError:
        print("File not found.")
    except requests.exceptions.HTTPError as err:
        print(f"Error sending image to Discord: {err}")

def send_line(token,msg):
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization" : "Bearer "+ token}
        payload = {"message" :  msg}
        r = requests.post(url, headers = headers, params=payload)


# 関数の呼び出しを行わない

