from PIL import ImageGrab, Image
import time
import pytesseract

import pytesseract

def capture_clipboard_image_and_ocr(filename='crs.png'):
    try:
        pytesseract.pytesseract.tesseract_cmd = r'\tesseract.exe'
        screenshot = ImageGrab.grabclipboard()
        dir_path = "C:\\Users\\kent\\Desktop"
        file_path = f"{dir_path}\\{filename}"

        print(file_path)
        if screenshot:
            # 画像をファイルに保存
            screenshot.save(file_path)
            print(f"クリップボードの画像が {file_path} に保存されました.")
            time.sleep(3)

            # 保存した画像を開く
            image = Image.open(file_path)

            # OCRを実行して文字を検出
            text = pytesseract.image_to_string(image)

            # 検出された文字列を表示
            print("検出された文字列:")
            print(text)

        else:
            print("クリップボードに画像がありません。")

    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    capture_clipboard_image_and_ocr()
