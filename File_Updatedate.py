import os
import datetime
import win32_setctime
from tkinter import filedialog
import random

x = random.randint(3,29)
t = random.randint(10,17)
b = random.randint(1,5)
c = random.randint(6,7)


dir = "C:\pg"
files = filedialog.askopenfilenames(initialdir=dir)
#fld = filedialog.askdirectory(initialdir=dir)
print(files)
# (1/3) ファイルパスを決めます。
# （フォルダならフォルダパスを指定します）


m = c
d = x
h = t

now = datetime.datetime.now()
for file  in files:
    # (2/3) 作成日時、更新日時、アクセス日時を決めます。
    ctime = datetime.datetime(2022, m, d - b, h, 12, 13).timestamp()
    mtime = datetime.datetime(2022, m, d, h, 15, 16).timestamp()
    atime = now.timestamp()

    # (3/3) タイムスタンプを変更します。
    win32_setctime.setctime(file, ctime)
    os.utime(file, (atime, mtime))

    # (デバッグ) タイムスタンプを取得して表示します。
    t = os.stat(file)
    print("--"*10)
    print('　　作成日時: %s' % datetime.datetime.fromtimestamp(t.st_ctime))
    print('　　更新日時: %s' % datetime.datetime.fromtimestamp(t.st_mtime))
    print('アクセス日時: %s' % datetime.datetime.fromtimestamp(t.st_atime))
    print("--"*10)
