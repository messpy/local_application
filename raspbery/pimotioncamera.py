from time import sleep
import time
import cv2
import picamera
import pysns_tool
import json
import subprocess
def normal(flename='motion_camera'):

    flename = "media/Photo/picamera_"+flename +".jpg"
    print("撮影します")
    # カメラの解像度を設定します
    CAMERA_WIDTH = 1280
    CAMERA_HEIGHT = 720

    # 逆さにするためのオプションを設定します
    REVERSE_VERTICAL = False #Trueで逆
    REVERSE_HORIZONTAL = False

    # カメラを初期化します
    camera = picamera.PiCamera()

    # カメラの解像度を設定します
    camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)

    # カメラの画像を逆さにする
    camera.vflip = REVERSE_VERTICAL
    camera.hflip = REVERSE_HORIZONTAL

    # 撮影を開始します
    camera.start_preview()

    # 2秒待機してから撮影します（プレビューを見るため）
    sleep(2)

    # 画像を保存します
    camera.capture(flename)
    print(flename+"を保存しました")
    # 撮影を終了します
    camera.stop_preview()
    camera.close()
    return flename

def motion():
    # Webカメラを使うときはこちら
    cap = cv2.VideoCapture(0)
    avg = None
    
    while True:
        # 1フレームずつ取得する。
        ret, frame = cap.read()
        if not ret:
            break
        # グレースケールに変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 比較用のフレームを取得する
        if avg is None:
            avg = gray.copy().astype("float")
            continue
        # 現在のフレームと移動平均との差を計算
        cv2.accumulateWeighted(gray, avg, 0.6)
        frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
        # デルタ画像を閾値処理を行う
        thresh = cv2.threshold(frameDelta, 3, 255, cv2.THRESH_BINARY)[1]
        # 画像の閾値に輪郭線を入れる
        contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
        if len(contours) > 500:
            print(len(contours))
            print("動きがありました")
            break
        else:
            pass
        # 結果を出力
        #cv2.imshow("Frame", frame)
        key = cv2.waitKey(30)
        if key == 27:
            break
def get_json(fle,key="test"):
    
    with open(fle, 'r',encoding="utf-8") as fle:
        data = json.load(fle)
        if key in data:
            return data[key]
        else:
            print(f"Error: Key '{key}' not found in JSON file.")
            return None

    cap.release()
    cv2.destroyAllWindows()

while True:
        
    print("開始")
    motion()
    fle = normal()
    token = get_json("data.json",key="discord")
    print(fle,token)
    pysns_tool.send_discord(token,fle)
    subprocess.run(["vcgencmd measure_temp"],shell=True)
    time.sleep(60)
    
