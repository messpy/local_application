#import pykit_tool

import dropbox
import os
import logging
import time
import tkinter as tk
from tkinter import filedialog
import requests
import psutil 
import pyttsx3
import speech_recognition as sr
import pyaudio
import wave
import subprocess


def help():
    mydict = {
        "select_fld()":"fldを選択",
        "select_fle(extension)":"例:*.txt ファイル選択",
        "send_discord(webhook_url, msg,img_path)":"画像テキストを[bot]に送る",
        "send_line(token,msg)":"メッセージのみ送信",
        "dropbox_dl(ACCESS_TOKEN)":"dropboxダウンロードする",
        "speak(msg)":"音声発生",
        "battery()":"バッテリ残量",
        "speech_listen()":"音声をリアルタイムで",
        "record_audio('output.wav', duration=10) ":"10秒間録音する",
        "disk_usage('/')":"HDD容量 usb等は引数に",
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
    root = tk.Tk()
    root.withdraw()
    fTyp = [("データファイル",extension )]
    fle_path = filedialog.askopenfile(filetypes=fTyp)
    print(fle_path.name)

    return fle_path.name


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
    print("Discodeに送信中")
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





def disk_usage(path='/'):　# ディスク使用状況を表示
    disk_info = psutil.disk_usage(path)
    total = disk_info.total / (1024 ** 3)  # ギガバイト単位に変換
    used = disk_info.used / (1024 ** 3)
    free = disk_info.free / (1024 ** 3)
    total = "{:.2f}".format(total)
    used = "{:.2f}".format(used)
    free = "{:.2f}".format(free)
    print(disk_info)
    print(f"合計容量{total}GB")
    print(f"使用容量{used}GB")
    print(f"空き容量{free}GB")

    return total,used,free






def speak(msg):
    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()
    

def batterry():
    dsk = psutil.disk_usage('/')
    btr1 = psutil.sensors_battery()
    print(btr1.percent+"%")
    
def speech_listen():#pip install SpeechRecognition と　pip install pyaudio
    r = sr.Recognizer()
    mic = sr.Microphone()


    print("聞き取り中...(stop = end)")

    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    print ("解析中...")

    try:
        listentxt = r.recognize_google(audio, language='ja-JP')
        print(listentxt)

        # "ストップ" と言ったら音声認識を止める
        if r.recognize_google(audio, language='ja-JP') == "ストップ" :
            print("end")
            exit
    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        listentxt = ""
        print(listentxt+"---")
        speech_listen()
    except sr.RequestError as e:
        listentxt = "---; {0}".format(e)
        print(listentxt)
    return listentxt

        


def record_audio(flename, duration=5, channels=1, rate=44100, chunk=1024):
    # PyAudioのインスタンスを作成
    audio = pyaudio.PyAudio()

    # 録音する設定を指定
    format = pyaudio.paInt16
    frames = []

    # ストリームを開始
    stream = audio.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    print(f"{duration}秒間録音中...")

    # 録音データを取得
    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print(f"{duration}秒間録音終了")

    # ストリームを停止・終了
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # WAVファイルに保存
    with wave.open(flename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    print(f"{flename} に録音が保存されました。")
    return flename


"""
    outfle = "test.mp3"
    try:
        subprocess.run([r"C:\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe", '-i', flename, '-b:a', '192k', outfle], check=True)
        print(f"{flename} を {outfle} に変換しました。")
    except subprocess.CalledProcessError as e:
        print(f"エラー: {e}")

# WAVファイルをMP3形式に変換
"""

    



# 録音時間を指定して録音を実行



# 関数の呼び出しを行わない

