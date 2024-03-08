import os
import datetime
import win32_setctime
from tkinter import filedialog
import random


def ran(s,g):
    da = random.randint(3,29)
    retern da
    
y = ran(2024,2024)
m = ran(1995,2024)
d = ran(1,30)
h = ran(9,18)
mm = ran(0,59)

print(y,m,d,h,mm)


dir = "C:\pg"
files = filedialog.askopenfilenames(initialdir=dir)
#fld = filedialog.askdirectory(initialdir=dir)
print(files)
# (1/3) ファイルパスを決めます。
# （フォルダならフォルダパスを指定します）



now = datetime.datetime.now()
for file  in files:
    # (2/3) 作成日時、更新日時、アクセス日時を決めます。
    ctime = datetime.datetime(y, m, d, h, h, mm).timestamp()
    mtime = datetime.datetime(y, m, d, h, h, mm).timestamp()
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
