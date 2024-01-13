import os
from tkinter import filedialog
import glob
x = 0
fld = filedialog.askdirectory()
print(fld)
names = ["様式8","様式2別紙_事業実施計画","スキーム","本事業","積算根拠","対象となる","実施予定施設","資料","写し","実績レポート","計算表","支出","収入","補助金調書","収益状況報告書","消費税仕入"]

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
        
