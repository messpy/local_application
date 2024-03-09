from time import sleep
import pyautogui as pg
import ctypes
import time
import numpy as np
#pg.FAILSAFE=False

def rec():
    print("録画します。Ctrl + C で終了")
    xs = []
    xm=[]
    xl=[]
    i = 0
    c = 0
    t = 0


    for i in range(1,6):
        sleep(1)
        print(abs(i-5))


    try:
        time_sta = time.time()
        f = open(r"C:\Users\USER\Desktop\mause.txt", "w")#変更
        while True:
                print(pg.position())
                xs.append(pg.position())
                
                i += 1
                if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                    print("Click!")
                    xm.append(pg.position())
                    xl.append(time.time())
                    a = str(pg.position())
                    a = a.replace('Point', '')
                    a = a.replace('(', '')
                    a = a.replace(')', '')
                    a = a.replace('x', '')
                    a = a.replace('y', '')
                    a = a.replace('=', '')
                    print(a)
                    f.write(a + "\n")
                    sleep(0.7)
                    c += 1
    except KeyboardInterrupt:   # exceptに例外処理を書く
        print('stop! \nlog:',i,"Click:",c)
        
        f.close()
        print(xl)
        x = input("再生しますか?y/n")
        if x == "y":
            rep()
        else:
            print("終了")
    except Exception as e:
        print("不明なエラー",e)
    m = i - 5
    xl = np.diff(xl)

    """
    for x in xs:
        print("残り",m,x)
        pg.moveTo(x)
        m-=1
    """
def rep():
    for o in range(20):
        f = open(r"C:\Users\USER\Desktop\mause.txt")#変更
        sleep(2)
        areas = f.read().split("\n")
        print("test:",areas)
        c = len(areas)
        h = 0
        
        try:
            for x in areas:
                d = 3
                print("Click残り",c,x)
                a,b =  x.split(",")
               #print(int(x),type(x[h+1]))
                pg.click(int(a),int(b))
                
                sleep(1)
                c -= 1
                h += 1
            
        except ValueError:
            f.close()
            print("終わり")
            #input("終了しました")

y = input("1.録画 2.再生 3.終了:")
if y == "1":
    rec()
elif y ==  "2":
    rep()
else:
    pass
