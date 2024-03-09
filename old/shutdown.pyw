from pystray import Icon,MenuItem, Menu
from PIL import Image
import time
import threading
import schedule
from ast import fix_missing_locations
import pyautogui
import os
import time
import datetime
import win32com.client as wincl
import tkinter as tk
from tkinter import messagebox
import sys
import winsound
from plyer import notification
import configparser
import requests

class taskTray:
    def __init__(self, image):
        self.status = False

        # アイコンの画像
        image = Image.open(image)
        # 右クリックで表示されるメニュー
        menu = Menu(
            MenuItem('Task', self.doTask),
            MenuItem('Exit', self.stopProgram),
        )

        self.icon = Icon(name='nameTray', title='Shutdown Program',
                         icon=image, menu=menu)

    def doTask(self):
        print('実行しました。')


        def line(me):
            url = "https://notify-api.line.me/api/notify"
            token = "TOKEN"
            headers = {"Authorization" : "Bearer "+ token}
            message =  me
            payload = {"message" :  message}
            r = requests.post(url, headers = headers, params=payload)

        # -------------------ini setting------------------------------
        inipass = PASS
        ini_name = ""
        config = configparser.ConfigParser()
        config.read(inipass + ini_name)
        timer = config["BASE"]["time"]
        timer2 = config["BASE"]["limit"]
        # iniと同じフォルダにすること
        Fmini = int(timer)  # 分設定
        Smini = int(timer2)   # 分設定

        Ftime = 60 * Fmini  # 時間設定
        Stime = 60 * Smini  # 2回目の時間設定
        # -----------------各種設定-----------------------------------------
        line("起動")
        dt_now = datetime.datetime.now()  # 現在時刻
        dt2 = dt_now + datetime.timedelta(minutes=Fmini + Smini)  # 現在時刻に時間を足す


        def nofi(time):  # シャットダウン通知
            notification.notify(
                title="あと" + time + "分でシャットダウンします",
                message="予定時刻：" + str(dt2) + "分",
                app_name="アプリの名前",
                # pp_icon="python.ico",
                timeout=5)


        def nowtime(f):
            dt_now = datetime.datetime.now()
            print(f, str(dt_now.strftime('%H:%M:%S')))


        # -----------------プログラム-----------------------------------------
        print("スタート\n1回目", Fmini, "分\n2回目", Smini, "分")
        print(ini_name, "を", inipass, "フォルダにしてください")
        nowtime("開始時刻：")
        notification.notify(
            title="START",
            message="1回目:" + str(Fmini) + "分\n2回目:" + str(Smini) + "分",
            app_name="アプリの名前",
            # pp_icon="python.ico",
            timeout=10)

        # -----------------メインウィンドウ-----------------------------------------


        for i in range(0, 100, 1):
            print("-----------------------------------------------------------------")
            fi = pyautogui.position()  # 定位置
            print(fi)
            nowtime("更新時刻：")
            time.sleep(Ftime)  # 待機時間----------------
            fi2 = pyautogui.position()  # 定位置
            if fi == fi2:
                print("--------------------1度目の静止状態-------------------------")
                nowtime("更新時刻：")


                nofi(str(Smini))

                time.sleep(Stime)  # 待機時間---------------
                print("---------------2度目の静止状態------------------------------")
                nowtime("15秒後にシャットダウンされます：")
                winsound.Beep(523, 900)
                time.sleep(15)
                fi3 = pyautogui.position()  # 定位置

                if fi2 == fi3:
                    print("---------------シャットダウン状態------------------------------")
                    line("シャットダウン")
                    nowtime("シャットダウン時刻:")
                    winsound.Beep(523, 900)
                    os.system('shutdown -s')

            else:
                print("-------------------更新されました--------------------------")
                notification.notify(
                    title="更新されます",
                    message="次回" + str(dt2) + "更新",
                    app_name="アプリの名前",
                    # pp_icon="python.ico",
                    timeout=10)


        # -----------------関数設定-----------------------------------------





    def runSchedule(self):
        # 5秒毎にタスクを実行する。
        schedule.every(5).seconds.do(self.doTask)
        # status が True である間実行する。
        while self.status:
            schedule.run_pending()
            time.sleep(1)

    def stopProgram(self, icon):
        self.status = False

        # 停止
        self.icon.stop()

    def runProgram(self):
        self.status = True

        # スケジュールの実行
        task_thread = threading.Thread(target=self.runSchedule)
        task_thread.start()

        # 実行
        self.icon.run()


if __name__ == '__main__':
    system_tray = taskTray(image=r"C:\Users\kent\Desktop\各ファイル\jpeg\sample.jpeg")
    system_tray.runProgram()
