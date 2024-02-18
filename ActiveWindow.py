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

        # ウィンドウを右下に配置
        self.set_window_position()

        # イベントループを開始
        self.root.after(self.polling_interval, self.check_window_state)

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
        
    def set_status(self, status_text):
        self.status_label.config(text=status_text)

    def activate_window(self):
        self.countdown = 3
        self.countdown_label()
        self.root.after(3000, self.do_activate_window)

    def deactivate_window(self):
        self.countdown = 3
        self.countdown_label()
        self.root.after(3000, self.do_deactivate_window)

    def countdown_label(self):
        if self.countdown > 0:
            self.set_status(f"処理開始まで {self.countdown} 秒...")
            self.countdown -= 1
            self.root.after(1000, self.countdown_label)
        else:
            self.set_status("")

    def do_activate_window(self):
        gw = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if gw:
            memo = win32gui.FindWindow(None, gw)
            win32gui.SetWindowPos(memo, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            status_text = f"{gw}をアクティブにしました"
        else:
            status_text = "Active Cancel"

        self.set_status(status_text)

    def do_deactivate_window(self):
        gw = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if gw:
            memo = win32gui.FindWindow(None, gw)
            win32gui.SetWindowPos(memo, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            status_text = f"{gw}を非アクティブにしました"
        else:
            status_text = "No active window to deactivate"

        self.set_status(status_text)

    def check_window_state(self):
        # ウィンドウの状態を確認
        gw = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if gw:
            status_text = f"現在のウィンドウ: {gw}"
        else:
            status_text = "現在のウィンドウがありません"

        # 状態を表示
        self.set_status(status_text)

        # 次の確認をスケジュール
        self.root.after(self.polling_interval, self.check_window_state)

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowManagerApp(root)
    root.mainloop()
