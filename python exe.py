import pyperclip
import pyautogui as pgui
import time
import glob
import os
url ="C:\\Users\\kent\\Desktop\\*.py"
files = glob.glob(url)
app = {}
i = 1
for f in files:
    base = os.path.basename(f)
    app[base] = i
    print(i,base) 
    i += 1
    
val = int(input("番号を入力"))
for key,value in app.items():
    if val==value:
        print(key)
    
def keey(text):
    time.sleep(2)
    pyperclip.copy(text)
    pgui.hotkey("Ctrl","v")
    pgui.hotkey("Enter")

pgui.hotkey("Win")
pgui.hotkey("c")
pgui.hotkey("m")
pgui.hotkey("d")
pgui.hotkey("Enter")

time.sleep(1)
pgui.hotkey("Win","UP")
pgui.hotkey("Win","LEFT")
#pgui.click(5,10)
keey('cd Desktop')
keey(".venv\\Scripts\\activate.bat")


pyperclip.copy("pyinstaller " + key + " --onefile")
pgui.hotkey("Ctrl","v")
pgui.hotkey("Enter")


