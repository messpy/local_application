import zipfile
from tkinter import filedialog


zff = filedialog.askopenfilename(title="zip")

def openzip(pas,f):
    zff = f
    zfff=r"C:\Users\kent\Desktop"
    with zipfile.ZipFile(zff,"r")as zf:
        try:
            zf.extractall(path=zfff,pwd=pas.encode())
            print("Password:",pas)
            input("終了")
        except Exception as e:
            pass
        
def main(f):
    num = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
    num1 = [48,49,50,51,52,53,54,55,56,57]
    mypass = []

    for a in num:
        for b in num:
            for c in num:
                for d in num:
                    yp = chr(a) + chr(b) + chr(c) + chr(d)
                    print(yp)

                    openzip(yp,f)


                    
if __name__ == "__main__":
    main(zff)
