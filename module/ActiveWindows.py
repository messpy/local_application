import win32gui
import win32con
import time
def activewindow(active):
    windowname = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    winnum = win32gui.FindWindow(None, windowname)
    if active == 0:
        win32gui.SetWindowPos(winnum, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"{windowname}\n\nActiveON")
    elif active == 1:
        win32gui.SetWindowPos(winnum, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"{windowname}\n\nActiveOFF")
    

if __name__=="__main__":
    offon = int(input("0=ActiveON\n1=AvtiveOFF\n選んでください:"))
    time.sleep(2)
    activewindow(offon)
