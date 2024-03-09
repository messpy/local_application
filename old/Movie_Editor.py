import cv2
import pyocr
from PIL import Image
from time import sleep


path = "/home/user/ダウンロード/movie_edit/RPR.mp4"
cap = cv2.VideoCapture(path)

i = 1
hight =  1300
while True:
    print("Frame"+str(i))
    ret,img = cap.read()
#ここから画像をトリミング6
    
    toriming_data = img[700:800, hight:1320]
    hight += 2
    x = str(i)
    #screenshot toriming
    cv2.imwrite(f"/home/*/ダウンロード/movie_edit/Routput{x}.png", toriming_data)
#ocr
    sleep(1)
    if i == 5:
        break

    #speed_number = toriming_data.image_to_string(
    #toriming_data.open("/home/user/ダウンロード/movie_edit/Routput.png")lang="eng")
    #print(speed_number)

 #   if ret == False:
  #      break

   # cv2.imshow("Video",img)
    i += 1

cap.release
cv2.destroyAllWindows()

print("END")
