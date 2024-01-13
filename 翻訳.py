from logging import root
from turtle import width
from googletrans import Translator
import tkinter as tk
import win32com.client as wincl
import winsound


winsound.Beep(262, 500)  # ド（262Hzの音を1000msec流す）
winsound.Beep(294, 500)  # レ（294Hzの音を1000msec流す）
winsound.Beep(330, 500)  # ミ（330Hzの音を1000msec流す）
winsound.Beep(349, 500)  # ファ（349Hzの音を1000msec流す）
winsound.Beep(392, 500)  # ソ（392Hzの音を1000msec流す）
winsound.Beep(440, 500)  # ラ（440Hzの音を1000msec流す）
winsound.Beep(494, 500)  # シ（494Hzの音を1000msec流す）

for i in range(1):  # 5回繰り返す
    winsound.Beep(523, 900)


def key_event(e):
    print(e.keysym)

    root.bind("<KeyPress>", key_event)

# 翻訳ボタン


def trans():
    excenge = txt.get()
    tr = Translator()
    result = tr.translate(excenge, src="en", dest="ja").text
    print(result)
    tran = tk.Label(text="訳:"+result)
    tran.place(x=20, y=80)

    voice = wincl.Dispatch("SAPI.SpVoice")
    voice.Volume = 30  # [0 to 100]
    voice.Rate = 0  # [-10 to 10]
    voice.Speak(excenge + "")


tki = tk.Tk()
tki.title("翻訳")
tki.attributes("-topmost", True)
tki.geometry("200x100+0+0")


transf = tk.Label(text="英語をを入力")
transf.place(x=20, y=10)

txt = tk.Entry(width=20)
txt.place(x=20, y=40)

push = tk.Button(tki, text="決定", command=trans)
push.place(x=160, y=35)


tki.mainloop()
