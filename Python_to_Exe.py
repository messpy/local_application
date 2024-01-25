import glob
import os
import tkinter.filedialog


fTyp = [("exeにしたいpyFile", "*.py")]
iDir = os.path.abspath(os.path.dirname(__file__))
pyfile = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

#pgui.hotkey("Enter")


result = subprocess.run(["cd", "desktop"], capture_output=True, encoding="utf-8")
result = subprocess.run(["pyinstaller",pyfile, "--onefile"], capture_output=True, encoding="utf-8")
print(result.stdout, end="")

