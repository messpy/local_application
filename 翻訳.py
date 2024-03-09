from logging import root
from turtle import width
from googletrans import Translator
import tkinter as tk
import win32com.client as wincl


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
