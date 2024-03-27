import serial

# COMポートに接続
ser = serial.Serial('COM8', baudrate=9600, timeout=1)

# 送信するコマンドを指定
command = "Your command here"

# コマンドをバイト列にエンコードして送信
ser.write(command.encode())

# 必要に応じて応答を読み取る
response = ser.readline().decode().strip()
print("Response:", response)

# 接続を閉じる
ser.close()