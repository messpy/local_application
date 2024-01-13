try:
        
    from PIL import ImageGrab
    from time import sleep
    from plyer import notification as nofi
    import pyautogui as pgui
    x = 500

    nofi.notify(
        title="START",
        message="1秒後自動スタート",
        timeout=1
        )
    sleep(1)

    for i in range(x):
         
        print(i,"枚目")
        screenshot = ImageGrab.grab()
        screenshot.save(r"C:\Users\910143\Desktop\PythonF\screenshot" + "\\" + str(i) + "ascr.jpg")
        #ImageGrab.grab().save("pdf.png")
        #ImageGrab.grab().copy

    input("スクショ")
except Exception as a:
    print(a)

input("batu")
