#!/usr/bin/env python
import cv2
import pysns_tool
import raspi_cameratool
import pykit_tool
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

        # 動きがあったかどうかを判定
        if len(contours) > 600:
            print(len(contours))
            print("動きがありました")
            break

            
        # 結果を出力
        #cv2.imshow("Frame", frame)
        key = cv2.waitKey(30)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

while True:
    motion()
    nowtime = pykit_tool.nowname()
    fle = raspi_cameratool.normal(str(nowtime))
    pysns_tool.send_discord("https://discord.com/api/webhooks/1204779730356928572/hHE-CBum_3hynzybh8Mz8Q5LDAg7dNHAS-KtGaqvzvwkoqd9bPgkE282n7C3frtV_X7f","sample", fle)
    
    
    pykit_tool.countdown(10)
    print("end")



    
