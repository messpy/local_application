try:
    
    import win32gui
    import win32con
    import pyautogui
    import ctypes
    import time
    from win32gui import GetWindowText, GetForegroundWindow

    from plyer import notification
     

    def wcancel(gw):
        print("CancelにしたいWindowを選択してください")
        notification.notify(
            title="Active解除設定",
            message= "CancelにしたいWindowを選択してください",
            app_name= gw,
            timeout=10
        )
        for i in range (0,7):
            i = i - 7
            print(abs(i))
            time.sleep(1)
            
        g = GetWindowText(GetForegroundWindow())
        memo = win32gui.FindWindow(None,g)
        time.sleep(1)
        win32gui.SetWindowPos(memo, win32con.HWND_NOTOPMOST, 0,0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        t = g + "をアクティブ外にしました"
        return t
    def windows(gw):
        memo = win32gui.FindWindow(None,gw)
        time.sleep(1)
        win32gui.SetWindowPos(memo,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        t = str(gw) + "をアクティブにしました"
        return t

    m = "ActiveにしたいWindowを選択してください\n(3秒後キャンセル設定）"
    print(m)

    for i in range (0,3):
        i = i - 3
        print(abs(i))
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
        message= a ,
        app_name="Active Window",
        timeout=10
    )

except Exception as e:
    print(e)
    input("Error:")
