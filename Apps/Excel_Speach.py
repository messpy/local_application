import xlwings as xw
import win32com.client
import mathBook.xls"shtpatch("Sapi.SpVoice")


r = int(input("読み上げ行:"))
ret = input("MNO等の列")
cell = "L"
def cel(x,c):
    sheet = xw.Range(cell + str(c)).value
    sheet = int(round(sheet,0))
    y = xw.Range(str(x) + str(c)).value
    y = round(int(y),1)
    print(c,"[",sheet,"シート]",y)
    page0 = xw.Range(cell + str(c - 1)).value
    page0 = int(round(page0,0))
    print(page0)
    if sheet != page0:     
        speech.Speak(str(sheet)+"シートめ")
    else:
        print("同じ")
    
    speech.Speak(str(y))
    print("a")
    
    try:
        int(round(xw.Range(cell + str(c + 1)).value,0))
    except TypeError:
        print("ありません")
        exit()
    else:
        pass
    #sleep(2) str(c)+"回目"+

 
for f in range(r,800):
    
    cel(ret,f)
    #cel("F",f,"")
    #cel("G",f,"\n")
    
    f += 1
input("完了")


