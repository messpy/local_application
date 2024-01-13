import os
import time
import pyautogui as pg
import datetime
import PySimpleGUI as sg
import configparser
import winsound
import requests


def line(me):
    url = "https://notify-api.line.me/api/notify"
    token = "TOKEN"
    headers = {"Authorization": "Bearer " + token}
    message = me
    payload = {"message":  message}
    r = requests.post(url, headers=headers, params=payload)


def time_init():
    inipass = "C:\\Users\\kent\\Desktop\\"
    ini_name = "time_setting.ini"
    config = configparser.ConfigParser()
    config.read(inipass + ini_name)
    timer = config["BASE"]["time"]
    timer2 = config["BASE"]["limit"]
    # iniと同じフォルダにすること
    Fmini = int(timer)  # 分設定
    Smini = int(timer2)   # 分設定
    return Fmini, Smini


def place(times):
    now = datetime.datetime.now()
    print(times, now)

    tx = pg.position()
    for t in range(times):
        time.sleep(1)
        t = times - t
        print(t)

    tx2 = pg.position()
    if tx == tx2:
        print("同じ")
        x = True
    else:
        x = False
    return x


Fmini, Smini = time_init()

first_time = 6 * Fmini  # 時間設定
second_time = 6 * Smini  # 2回目の時間設定

while True:
    print("a")
    if place(first_time) == True:
        if place(second_time) == True:
            print("shut!!")
            winsound.Beep(523, 900)
            break
            os.system('shutdown -s')
