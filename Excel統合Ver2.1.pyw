import PySimpleGUI as sg
from tkinter import filedialog
import glob
import xlwings as xw
import os

pbmax = 10

#Setting

def Excel_Integration(update,new):
    
    xw.App(visible=False)
    newbook = xw.Book()
    window["readfile"].update(value="読み込み中..")
    window["time"].update(value="0.0%")
    sk = 1
    fld = glob.glob(update)
    data = len(fld)
    window["readfile"].update(value=fld[0])
    for i,fd in enumerate(fld):
        c = 2
        aleadybook = xw.Book(fd)
        ls = len(aleadybook.sheets)
        print(fd,ls,"枚")
        print(i,"/",data)
        basename = os.path.basename(fd)
        pb = i / data * 10
        window["time"].update(value=str(pb * 10) + "%")
        window["data"].update_bar(pb)
        window["readfile"].update(value=basename)
        newbook.save(r"C:\Users\910143\Desktop" + "\\" + new)
            
        for ii,s in enumerate(range(ls)):
            print("　・",aleadybook.sheets[s].name)
            if "例" in aleadybook.sheets[s].name or "シートについて" in aleadybook.sheets[s].name:
                print("例を除外:",aleadybook.sheets[s].name)
                pass
            else:
                window["readfile"].update(value=basename)
                aleadybook.sheets[s].copy(after=newbook.sheets[-1])
                newbook.sheets[0].cells(sk, 1).value = fd
                newbook.sheets[0].cells(sk, c).value = aleadybook.sheets[s].name
                newbook.sheets[ii].cells(1, 20).value = basename
            sk += 1
            c += 1
        aleadybook.close()
    window["readfile"].update(value="完了")
    window["time"].update(value="100%")
    newbook.save(r"C:\Users\910143\Desktop" + "\\" + new)
    newbook.close()
    window["data"].update_bar(10)
    sg.popup_ok(r"C:\Users\910143\Desktop" + "\\" + new + "\n作成しました") 
    return aleadybook
        

def pdf(update):
        xw.App(visible=False)

        window["readfile"].update(value="読み込み中..")
        sk = 1
        fld = glob.glob(update)
        data = len(fld)
        
        for i,fd in enumerate(fld):
            print(i,"/",data)
            basename = os.path.basename(fd)
            pb = i / data * 10
            window["data"].update_bar(pb)
            window["readfile"].update(value=basename)
            aleadybook = xw.Book(fd)
            ls = len(aleadybook.sheets)
            print(fd,ls,"枚")
            
            for ii,s in enumerate(range(ls)):
                print(s)
                window["data"].update_bar(pb)
                print("  ",aleadybook.sheets[s].name)
                aleadybook.sheets[s].to_pdf(basename + aleadybook.sheets[s].name +".pdf",show=True)

#main Window

layout = [[sg.Text("Excel統合")],
          [sg.Input(key="folder"),sg.Button("参照",key="参照"),sg.Checkbox("サブ", default=False,key="sub")],
          [sg.Text("検索名指定"),sg.Input(size=(10,2),key="file"),sg.Text("File名指定"),sg.Input(size=(10,2),key="name"),sg.Button("実行",key="ok"),sg.Button("PDF",key="pdf")],
          [sg.ProgressBar(pbmax,size=(30,5),key="data"),sg.Text("/",key="time")],
          [sg.Text("                        読み込みファイル",size=(30,2),key="readfile")]
          ]

window = sg.Window('Excel統合Ver1.03', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '終了':
        break
    if event == "参照":
        dir = "C:\pg"
        folder = filedialog.askdirectory(initialdir=dir)
        window["folder"].update(value=folder)

        
        
    if event == "ok":
        print("excel")
        if values["sub"] == True:
            update = folder + "/*/*" + values["file"] + "*.xls*"
        else:            
            update = folder + "/*" + values["file"] + "*.xls*"
            
        window["folder"].update(value=update)
        New_filename =  values["name"] + ".xlsx"
        print(New_filename)
        try:
            Excel_Integration(update,New_filename)
        except Exception as e:
            window["readfile"].update(value="ERROR!")
            sg.popup_ok(e)
        
    if event == "pdf":
        print("pdf")
        if values["sub"] == True:
            update = folder + "/*/*" + values["file"] + "*.xls*"
        else:            
            update = folder + "/*" + values["file"] + "*.xls*"
            
        window["folder"].update(value=update)
        pdf(update)
        


window.close()
