import win32gui
import win32con
import time
from win32gui import GetWindowText, GetForegroundWindow
from plyer import notification

def wcancel(gw):
    print("CancelにしたいWindowを選択してください")
    notification.notify(
        title="Active解除設定",
        message="CancelにしたいWindowを選択してください",
        app_name=gw,
        timeout=10
    )
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    g = GetWindowText(GetForegroundWindow())
    memo = win32gui.FindWindow(None, g)
    time.sleep(1)
    win32gui.SetWindowPos(memo, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    t = f"{g}をアクティブ外にしました"
    return t

def windows(gw):
    memo = win32gui.FindWindow(None, gw)
    time.sleep(1)
    win32gui.SetWindowPos(memo, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    t = f"{gw}をアクティブにしました"
    return t

if __name__ == "__main__":
    print("ActiveにしたいWindowを選択してください\n(3秒後キャンセル設定）")

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    gw = GetWindowText(GetForegroundWindow())
    print(gw)

    if gw == "":
        print("Active Cancel")
        a = wcancel(gw)
    else:
        print("Active Window")
        a = windows(gw)

    notification.notify(
        title="Active",
        message=a,
        app_name="Active Window",
        timeout=10
    )
