import keyboard
import os
import time
import pyautogui as pg
import datetime
import PySimpleGUI as sg
import configparser
import winsound
import requests
from plyer import notification
import psutil
import logging
import psutil
import win32gui
import win32con
from win32gui import GetWindowText, GetForegroundWindow



set_time = 60
i = set_time * 90 


def timer(i):
    i -= 1
           
    print(i) 
    return i
    
def line(me):
    try:
        
        dsk = psutil.disk_usage('/')
        btr = psutil.sensors_battery()
        
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('./test.log')
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(levelname)s  %(asctime)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info(str(me)+str(btr.percent)+"%")

        url = "https://notify-api.line.me/api/notify"
        token = "mmjcR1plHjBEGizK6p3ZP7rA9hERqz9VwDhfNr1VOKe"
        headers = {"Authorization" : "Bearer "+ token}
        message =  me + " "  + str(btr.percent) + "%"
        payload = {"message" :  message}
        r = requests.post(url, headers = headers, params=payload)
    except Exception as e:
        print("Error",e)


def nofi(time):  # シャットダウン通知
        notification.notify(
        title="残り時間",
        message= "残り" + time + "分になりました",
        app_name="アプリの名前",
        # pp_icon="python.ico",
        timeout=5)
        winsound.Beep(523, 900)




layout=[
        [sg.Text(key="jikan")],
        [sg.Input(set_time,key="set",size=(3,5)),sg.Button("分",key="ok")]
       
        ]

window = sg.Window("Exit",layout,
                   #size=(20,70),
                   relative_location=(630,310),
                   alpha_channel=0.8,
                   return_keyboard_events=True,
                   no_titlebar= True,
                   keep_on_top=True,
                   border_depth=3,
                   right_click_menu=['Unused', ["shutdown","Active","exit"]])

line("起動")
while True:
    event,value = window.read(timeout=20,timeout_key="timer")
    
    btr = psutil.sensors_battery()
    if btr.percent == 3:
        line("残り")
        nofi("3%")
        time.sleep(60)
    tx = pg.position()
    time.sleep(1)
    if event == sg.WIN_CLOSED or event =="exit":
        break
    elif event == "ok" or event=="\r":
        print("ok")
        set_time = int(value["set"])
        i = set_time * 60

    elif event in (None,):
        break
    
    elif event in 'timer':
        ty = pg.position()
        if tx == ty:
            i = timer(i)
        else:
            i = set_time * 60
            
        window['jikan'].update("{0}分{1}秒".format(str(i//60),str(i%60)))
        
        if i * 60 == 10 or i* 60 == 5 or i* 60 == 1:
            print("残り{0}分です".format(str(i)))
            nofi(str(i))

        if i == 0:
            line("終了")
            os.system('shutdown -s')
            break
    elif event == "shutdown":
            line("終了")
            os.system('shutdown -s')
        
    elif event == "Active":
        for i in range(0,3):
            i = i - 3
            time.sleep(1)
            
        g = GetWindowText(GetForegroundWindow())
        memo = win32gui.FindWindow(None, g)
        
        win32gui.SetWindowPos(memo, win32con.HWND_TOPMOST, 0,0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        t = str(g) + "をアクティブにしました"
        print(g)
    
window.close()
        
