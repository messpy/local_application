import logging
import PySimpleGUI as sg
import pyautogui
import time
from plyer import notification
from module import ActiveWindows
from module import pykit_tool 
from module import pysns_tool


class Shutdown:
    def __init__(self):
        self.position = []

    def set_sht_limit(self, sht_limit):
        self.sht_limit = sht_limit * 60
        


    def set_gui(self):
        # GUIのレイアウトとウィジェットを定義
        layout = [[sg.Text(self.sht_limit, key='time')],
                  [sg.InputText(key='-Input-', size=3), sg.Button('分')]]
        
        window = sg.Window('Shutdown Timer',
                            layout,size=(90,70),
                            location=(1270,660),
                            no_titlebar=True,
                            alpha_channel=0.8,
                            grab_anywhere=True,
                           
        right_click_menu=['Unused', ['ActiveON', 'ActiveOFF','!&Click', 'Exit',]],right_click_menu_text_color='green')
        # イベントループ
        while True:
            event, values = window.read(timeout=1000)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == sg.WIN_CLOSED or event == 'ActiveON':
                ActiveWindows.activewindow(0)
            elif event == sg.WIN_CLOSED or event == 'ActiveOFF':
                ActiveWindows.activewindow(1)

            # 時間を更新
            self.sht_limit -= 1
            warntime = 60
            #残り60秒なら通知
            if self.sht_limit == warntime:
                pykit_tool.send_notification(f"残り{warntime}秒です")
            m, s = divmod(self.sht_limit, 60)
            window['time'].update(f"{m}分{s}秒")

            # マウス位置を取得
            position = pyautogui.position()

            # マウス位置が変化したら時間をリセット
            if position not in self.position:
                self.position.append(position)
                self.set_sht_limit(30)

            # 入力された時間を読み込み、カウントダウンを開始
            if event == '分':
                try:
                    sht_limit = int(values['-Input-'])
                    self.set_sht_limit(sht_limit)
                except ValueError:
                    pass

        window.close()

    def count_time(self):
        # 時間経過処理
        while self.sht_limit > 0:
            time.sleep(1)
            self.sht_limit -= 1

        # 時間切れ処理
        print('時間切れです!')


def sendlog(msg):
    line = pysns_tool.get_json(key="line")
    btr = pykit_tool.batterry()
    txt = f"{btr} {msg}"
    logging.info(txt)
    pysns_tool.send_line(line,txt)


if __name__ == '__main__':
    pykit_tool.setup_logging(r"media\job.log")
    sendlog("起動")
    shutdown = Shutdown()
    shutdown.set_sht_limit(30)
    shutdown.set_gui()
    shutdown.count_time()
    sendlog("終了")
