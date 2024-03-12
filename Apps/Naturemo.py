from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from json import loads
import datetime
import sys


def remocon(select_button):
    select_button = int(select_button)
    print(select_button)
    appliance = "LIGHT" #操作する家電の種類["TV", "LIGHT"]
    nickname = "Takizumi"   #テレビ/ライトのニックネーム
    #nickname = "Atrium-light"   #ライトのニックネーム
    api_access_key = "NKFro7WlqpjZXszgLYAqDLiVQlsIHMX25z1f-ipn1I4.Y1ObZ6ZwByRQJZ3v5zZ7vbrSt7xggykHJADJx9b0LLY" # APIアクセストークン

    url = "https://api.nature.global"

    headers = {
        "Authorization" :"Bearer " + api_access_key,
        "accept" :"application/json",
        "Content-Type" :"application/x-www-form-urlencoded"
    }

    #全ての家電情報を取得
    request = Request(url + "/1/appliances/", headers=headers) 

    try:
      with urlopen(request) as response:
        data = response.read()
        devices = loads(data)
    except HTTPError as e:
        print(e)


    #デバイスID探索
    device_id = "" 

    for device in devices:
      if device["type"] == appliance and device["nickname"] == nickname:
        device_id = device["id"]
        buttons = device[appliance.lower()]["buttons"]


    #各ボタンの表示
    print("操作するボタンを数字で選んでください。")
    num = 0
    for button in buttons:
      if button["label"] != "":#空白のボタンがあるためif文で処理
        print(str(num) + " :\t"  + button["label"])
        num += 1

    #selected_button = int(input("入力:"))

    signal = buttons[select_button]["name"]
    #データ送信
    request = Request(url + "/1/appliances/" + device_id + "/" + appliance.lower(), headers=headers)

    data = {
        "button": signal
    }

    data = urlencode(data).encode("utf-8")

    try:
      urlopen(request, data)
      print("成功です。")
    except HTTPError as e:
        print(e)

args = sys.argv

if len(args) > 1:
    argument = args[1]
    print(argument)
    remocon(argument)
else:
    print("値がありません")
    argument = "None"
    
if __name__=="__main__":
    print("0:ON\n1:OFF\n2:ALL")
    x = input("操作するボタンを数字で選んでください:")
    remocon(x)




    
    
