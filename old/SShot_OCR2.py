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
        self.master.attributes('-topmost', 1)  # メインウィンドウを常に最前面に保つ

        self.label = tk.Label(self.master, text="右クリックまたはボタンクリックでスクリーンショット")
        self.label.pack(pady=20)

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
            # Bring the active window to the front temporarily
            active_window.activate()

            # Get the dimensions of the active window
            left, top, right, bottom = active_window.left, active_window.top, active_window.right, active_window.bottom
            width = right - left
            height = bottom - top

            # Capture the screenshot of the active window only
            screenshot = ImageGrab.grab(bbox=(left, top, left + width, top + height))

            # スクリーンショットを300x300にリサイズ
            screenshot = screenshot.resize((300, 300))

            # スクリーンショットを表示
            self.display_screenshot(active_window.title, screenshot)
        else:
            print("アクティブなウィンドウが見つかりません。")

    def display_screenshot(self, window_title, screenshot):
        # スクリーンショットをPIL ImageからTkinter PhotoImageに変換
        screenshot_tk = ImageTk.PhotoImage(screenshot)

        # 新しいウィンドウを作成
        display_window = tk.Toplevel(self.master)
        display_window.title(f"Screenshot of {window_title}")  # ウィンドウタイトルをアクティブなウィンドウの名前に
        display_window.attributes('-topmost', 1)  # サブウィンドウを常に最前面に保つ
        display_window.geometry("400x400+1000+0")  # ウィンドウの位置をもっと右上に配置

        # 画像を表示するキャンバスを作成
        canvas = tk.Canvas(display_window)
        canvas.pack()

        # スクリーンショットをキャンバスに表示
        canvas.create_image(0, 0, anchor=tk.NW, image=screenshot_tk)

        # Tkinter PhotoImageオブジェクトを保持
        canvas.image = screenshot_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
