import win32gui
import win32con
import time



def notification(titlemsg,message):
    from plyer import notification
    notification.notify(
        title=titlemsg,
        message=message,
    )
    
def activewindow(wm=0):
    modify = ""
    time.sleep(2)
    #Avtivename
    active_hwnd = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    #ActiveNumber
    hwnd = win32gui.FindWindow(None, active_hwnd)
    #wm = win32gui.GetForegroundWindow() ==  hwnd
    

    if wm == 0:
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        modify = "ActiveOFF"
    elif wm == 1:
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        modify = "ActiveON"
        

    print(modify)
    notification(modify,f"{active_hwnd}")

    
if __name__=="__main__":
    x = int(input("ActiveON=1\nActiveOFF=0\nActive?:"))

    active_hwnd = activewindow(x)

    
