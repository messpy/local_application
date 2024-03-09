#import pykit_tool
# pykit_tool.help
# pykit_tool.send_line(引数)#"mmjcR1plHjBEGizK6p3ZP7rA9hERqz9VwDhfNr1VOKf"
# pykit_tool.send_discord(引数)"https://discord.com/api/webhooks/1204779730356928572/hHE-CBum_3hynzybh8Mz8Q5LDAg7dNHAS-KtGaqvzvwkoqd9bPgkE282n7C3frtV_X7f"


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
import speedtest
import ifcfg
import os
import inspect
import json
from datetime import datetime

def help():
    mydict = {
        "select_fld()": "fldを選択",
        "select_fle(extension)": "例:*.txt ファイル選択",
        "send_discord(webhook_url, msg,img_path)": "画像テキストを[bot]に送る",
        "send_line(token,msg)": "メッセージのみ送信",
        "dropbox_dl(ACCESS_TOKEN)": "dropboxダウンロードする",
        "speak(msg)": "音声発生",
        "battery()": "バッテリ残量",
        "speech_listen()": "音声をリアルタイムで",
        "record_audio('output.wav', duration=10) ": "10秒間録音する",
        "disk_usage('/')": "HDD容量 usb等は引数に",
        "ping_test()→ping": ""



    }
    print("関数(引数):説明")
    for mykey, myvalue in mydict.items():
        print(f"[{mykey}] {myvalue}")
#

# 設定関連


def setup_logging(log_file):
    """ログの設定を行う関数"""
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    print("関数をファイル名を指定して呼び出してください「logging.info()」")


""" カスタムのログレベルを使ってログを記録する
logging.log(logging.DEBUG, "デバッグ情報です")

try:
    # 何らかの処理を実行する
except Exception as e:
    logging.exception("処理中にエラーが発生しました:")

 プログラムの終了時にロギングシステムをシャットダウンする
logging.shutdown()


"""
def nowname():
    # 現在の日付と時間を取得
    now = datetime.now()

    # 年の部分を取得
    nowtime = now.strftime("%Y%m%d_%H%M_%S")

    # 結果を出力
    print(nowtime)
    return nowtime


def get_json(filename="data.json", key="test"):
    with open(filename, 'r') as file:
        data = json.load(file)
        if key in data:
            return data[key]
        else:
            print(f"Error: Key '{key}' not found in JSON file.")
            return None


def send_notification(message):
    notification.notify(
        title='Notification',
        message=message,
    )


def countdown(timer):
    while timer > 0:
        print(f"{str(timer)}秒")
        time.sleep(1)
        timer -= 1
    print("終了")


def select_fld(selection):
    """指定されたオプションに応じてフォルダまたはファイルを選択する関数を生成する"""
    root = tk.Tk()
    root.withdraw()

    if selection == "fld":
        return filedialog.askdirectory()
    elif selection == "flds":
        return filedialog.askdirectoryes()
    elif selection == "fle":
        return filedialog.askopenfilename()
    elif selection == "fles":
        return filedialog.askopenfilenames()


# Python周り関連
def create_executable(file_name):
    """指定されたファイル名で pyinstaller を実行し、--onefile オプションを付ける関数"""
    try:
        subprocess.run(['pyinstaller', '--onefile', file_name])
        print("実行可能ファイルが作成されました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")


# 内部情報関連

def batterry():
    dsk = psutil.disk_usage('/')
    btr1 = psutil.sensors_battery()
    print(f"{btr1.percent}%")


def disk_usage():  # ディスク使用状況を表示
    path = '/'
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

    return total, used, free


def ping_test():  # 回線チェック

    print("speed test中..")
    st = speedtest.Speedtest()
    st.get_best_server()
    print("計算中...")

    # 速度測定を実行
    download_speed = st.download() / 1024 / 1024  # Mbpsに変換
    upload_speed = st.upload() / 1024 / 1024  # Mbpsに変換
    ping = st.results.ping

    # Wifi名取得CMD使う
    print("Wifi名取得中...")
    try:
        wifi_name = next((line.split(":")[1].strip() for line in subprocess.run(
            ["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True, check=True).stdout.splitlines() if "SSID" in line), "none")
    except subprocess.CalledProcessError:
        wifi_name = "none"
    except Exception as e:
        wifi_name = "none"

    print("[測定結果]")
    print(f"WiFi名:{wifi_name}")
    print(f"download_speed: {download_speed}Mbps")
    print(f"upload_speed: {upload_speed}Mbps")
    print(f"ping: {ping}ms")
    return wifi_name, download_speed, upload_speed, ping


# 音声関連


def speech_listen():  # pip install SpeechRecognition と　pip install pyaudio
    r = sr.Recognizer()
    mic = sr.Microphone()

    print("聞き取り中...(stop = end)")

    with mic as source:
        r.adjust_for_ambient_noise(source)  # 雑音対策
        audio = r.listen(source)

    print("解析中...")

    try:
        listentxt = r.recognize_google(audio, language='ja-JP')
        print(listentxt)

        # "ストップ" と言ったら音声認識を止める
        if r.recognize_google(audio, language='ja-JP') == "ストップ":
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


def speak(msg):
    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()


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
