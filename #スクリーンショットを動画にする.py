# スクリーンショットを動画にする
import numpy as np
import cv2
import pyautogui as pag
import os
import time
import tkinter as tk

tki = tk.Tk()
tki.title("画面録画")


def rokuga():

    # 保存するファイル名
    timestr = time.strftime("%Y%m%d-%H%M%S")
    img_dir_name = "./formovie"+timestr
    print(img_dir_name)
    # 画像保存用ファイルを作成
    files = os.makedirs(img_dir_name, exist_ok=True)
    # 動画用の画像（スクリーンショット）を用意
    # 画像を格納するリスト
    img_list = []
    img_No = 0
    # 動画のフレームレイト
    FPS = 14
 # 録画したい時間---------------------------------------------------------------------------------------------------
    indices = listbox.curselection()
    index = indices[0]
    movie_time = listbox.get(index)
    print(movie_time)
    #movie_time = 20
    # 上記フレームレイトと録画時間を満たす繰り返し数
    photo_no = FPS*movie_time

    # デスクトップ画面の縦横の大きさを取得
    img = pag.screenshot()
    img = np.asarray(img)
    img_height, img_width, channels = img.shape

    # 繰り返しスクリーンショットを撮り、ファイルに保存
    for i in range(0, photo_no, 1):
        img_No = img_No + 1
        img = pag.screenshot()
        img = np.asarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img_output = '{}/{:010d}.png'.format(img_dir_name, img_No)
        cv2.imwrite(img_output, img)
        img_list.append(img_output)
    print("動画作成中")
    # 保存された画像を繋げて動画作成
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter('desktop_capture.mp4', fourcc,
                            FPS, (img_width, img_height))
    for s in img_list:
        img = cv2.imread(s)
        video.write(img)

    video.release()


list_value = tk.StringVar()
list_value.set([10, 30, 60, 500, 1000])

listbox = tk.Listbox(tki, height=5, width=3,
                     listvariable=list_value, selectmode="single")
listbox.pack()
listbox.place(x=5, y=3)
# 関数　リスト


def moviet():
    selected_indices = listbox.curselection()
    selected_module = ",".join([listbox.get(i) for i in selected_indices])


btn = tk.Button(tki, text="実行", command=rokuga)
btn.place(x=80, y=20)

tki.mainloop()
