import picamera
from time import sleep
import cv2
import time
def normal(flename='captured'):
    flename = "media/picamera/picamera_"+flename +".jpg"
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


def kao():

    print("顔検出中")
    # OpenCVのカスケード分類器をロードします
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # カメラを初期化します
    cap = cv2.VideoCapture(0)

    while True:
        # フレームをキャプチャします
        ret, frame = cap.read()
        
        # グレースケールに変換します
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 顔を検出します
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # 顔が検出されたら、画像を保存します
        if len(faces) > 0:
            # 現在のUNIX時刻を使用してファイル名を生成します
            timestamp = int(time.time())
            flename = f'face_{timestamp}.jpg'
            
            # 画像を保存します
            cv2.imwrite(filename, frame)
            print(f'写真が {flename} として保存されました！')
            
        # ESCキーを押すと終了します
        #if cv2.waitKey(1) & 0xFF == 27:
            break
            
    # キャプチャを解放します
    cap.release()
    cv2.destroyAllWindows()
    return flename


if __name__ == "__main__":
    now = datetime.now()
    nowtime = now.strftime("%Y%m%d_%H%M_%S")
    filename = normal(nowtime)
