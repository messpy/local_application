import tkinter as tk
import pygetwindow as gw
from PIL import ImageGrab, Image, ImageTk
import threading
import time

class ScreenshotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Screenshot App")
        self.master.geometry("300x200")

        # メインウィンドウを常に最前面に
        self.master.wm_attributes('-topmost', True)

        # サブウィンドウを右上に配置
        self.display_window = None

        # ボタンを追加
        self.button = tk.Button(self.master, text="スクリーンショットを撮影", command=self.start_countdown)
        self.button.pack()

    def start_countdown(self):
        # カウントダウンを開始
        countdown_thread = threading.Thread(target=self.countdown)
        countdown_thread.start()

    def countdown(self):
        # カウントダウン処理
        for i in range(3, 0, -1):
            print(f"カウントダウン: {i}")
            time.sleep(1)

        # カウントダウン終了後、アクティブなウィンドウのスクリーンショットを取得
        active_window = gw.getActiveWindow()
        if active_window:
            left, top, right, bottom = active_window.left, active_window.top, active_window.right, active_window.bottom
            screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

            # スクリーンショットを300x300にリサイズ
            screenshot = screenshot.resize((300, 300))

            # サブウィンドウを作成
            self.display_window = self.create_display_window(screenshot, active_window.title)

        else:
            print("アクティブなウィンドウが見つかりません。")

    def create_display_window(self, screenshot, window_title):
        # スクリーンショットをPIL ImageからTkinter PhotoImageに変換
        screenshot_tk = ImageTk.PhotoImage(screenshot)

        # サブウィンドウを作成
        display_window = tk.Toplevel(self.master)
        display_window.title(window_title)

        # 画像を表示するキャンバスを作成
        canvas = tk.Canvas(display_window)  # widthとheightは指定しない
        canvas.pack()

        # スクリーンショットをキャンバスに表示
        canvas.create_image(0, 0, anchor=tk.NW, image=screenshot_tk)  # widthとheightは削除

        # Tkinter PhotoImageオブジェクトを保持
        canvas.image = screenshot_tk

        # サブウィンドウを右上に配置
        display_window.geometry("+%d+%d" % (self.master.winfo_width() - display_window.winfo_width(), 0))

        return display_window

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
