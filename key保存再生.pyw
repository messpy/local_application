import keyboard
import time
import PySimpleGUI as sg

layout = [[sg.Text("キーボード録画"),sg.Input("5",key="repeat",size=(4,1)),sg.Text("回")],
          [sg.Button("REC",key="rec"),sg.Button("PLAY",key="play")]


          ]

window = sg.Window("KeyBorad",layout,return_keyboard_events=True)

while True:
    event,value = window.read()
    if event == sg.WIN_CLOSED or event == "End":
        break

    elif event == "rec":
        record = keyboard.record("esc")
 

    elif event=="play":
        time.sleep(3)
        try:
            c = int(value["repeat"])
        except ValueError or TypeError :
            c = 1
        
        for i in range(c):
            keyboard.play(record,speed_factor=10)
        window["repeat"].update("End")

    

    
    


