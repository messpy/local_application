import tkinter as tk
import threading
import time


class PerformanceImprovementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Performance Improvement")

        self.is_processing = False

        self.start_button = tk.Button(
            master, text="処理開始", command=self.toggle_processing)
        self.start_button.pack()

    def toggle_processing(self):
        if not self.is_processing:
            self.is_processing = True
            threading.Thread(target=self.heavy_processing).start()
            self.start_button.config(text="処理停止")
        else:
            self.is_processing = False
            self.start_button.config(text="処理開始")

    def heavy_processing(self):
        while self.is_processing:
            # 重い処理（例：無限ループ）
            for _ in range(1000000):
                pass
            time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = PerformanceImprovementApp(root)
    root.mainloop()
