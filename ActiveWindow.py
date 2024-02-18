import tkinter as tk
from tkinter import ttk
import win32gui
import win32con

class WindowManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Window Manager")

        self.status_label = ttk.Label(root, text="")
        self.status_label.pack(pady=20)

        self.activate_button = ttk.Button(root, text="On", command=self.activate_window)
        self.activate_button.pack(pady=10)

        self.deactivate_button = ttk.Button(root, text="Off", command=self.deactivate_window)
        self.deactivate_button.pack(pady=10)

        # タイマーの周期を設定 (ミリ秒)
        self.polling_interval = 1000  # 1秒ごとに確認
        self.countdown = 3  # カウントダウンの秒数

        # イベントループを開始
        self.root.after(self.polling_interval, self.check_window_state)

        # ウィンドウを右下に配置
        self.set_window_position()

    def set_status(self, status_text):
        self.status_label.config(text=status_text)

    def set_window_position(self):
        # ウィンドウの幅と高さを取得
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        # 画面の幅と高さを取得
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # ウィンドウを右下に配置
        x = screen_width - window_width
        y = screen_height - window_height
        self.root.geometry(f"+{x}+{y}")

    # 以下同じ...

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowManagerApp(root)
    root.mainloop()
