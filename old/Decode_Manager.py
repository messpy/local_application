import base64
from tkinter import filedialog
import cv2
import numpy as np
import io
import PySimpleGUI as sg

def encode():
    tar= filedialog.askopenfilename()
    print(tar)
    file_data = open(tar, "rb").read()
    b64_data = base64.b64encode(file_data).decode('utf-8')
    print(b64_data)
    
    return b64_data 






def decode(txt):
    imf = txt[1:5] +".jpg"
        #バイナリデータ <- base64でエンコードされたデータ  
    img_binary = base64.b64decode(txt)
    jpg=np.frombuffer(img_binary,dtype=np.uint8)

        #raw image <- jpg
    img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
        #画像を保存する場合
    #cv2.imwrite(imf,img)

        #表示確認
    cv2.imshow('window title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




layout = [[sg.Text("",key="moji")],
          [sg.Button("encode"),sg.Button("decode")],
          [sg.Multiline(key="txt",size=(20,10))]



          ]

window = sg.Window("Base64",layout)

while True:
    event,value = window.read()
    if event == sg.WIN_CLOSED:
        print("exit")
        break
    elif event == "encode":
        a = encode()
        window['txt']. Update(a)
        window['moji']. Update(str(len(a)) + "文字")
        
    elif event == "decode":
        t = value["txt"]
        decode(t)
window.close()
