import os
from tkinter import filedialog
import glob
x = 0
fld = filedialog.askdirectory()
print(fld)
#ファイル名の一致した物を検索
names = ["消費税仕入"]
#順番に付け足す
numb = ["fa0","①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩","⑪","⑫","⑬","⑭","⑮"]

fle = glob.glob(fld + "\*.*")
fnum = len(fle)
for name,num in zip(names,numb):
    print("--{}--".format(name))
    data = glob.glob(fld + "\*" + name + "*.*")
    x += 1
    for d in data:
        a,b = os.path.split(d)
        c = a + "\\" + numb[x] + b
        os.rename(d,c)
        print(c,"\n")
       #print("{} {}, {}/{}".format(num,d,x,fnum))
        
