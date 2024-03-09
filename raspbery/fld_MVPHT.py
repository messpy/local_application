import os
import time
import shutil
import pysns_tool
import pykit_tool
import logging
import subprocess

def get_exif_info(fle):
    try:
        exif_output = subprocess.check_output(["exiftool", fle]).decode("utf-8")
        return exif_output
    except subprocess.CalledProcessError as e:
        exif_output = f"Exif情報の取得中にエラーが発生しました: {e}"
        
        return exif_output

    

def watch_folder(source_folder, destination_folder):
    while True:
        i = 2
        if os.path.exists(destination_folder):
            files = os.listdir(source_folder)
            for file in files:
                file_path = os.path.join(source_folder, file)
                if os.path.isfile(file_path) and time.time() - os.path.getctime(file_path) > 1:
                    try:
                        shutil.move(file_path, destination_folder)
                        txt = f"SuccessMove[{file}]{destination_folder}"
                        print(txt)
                        logging.info(logging.INFO, txt)
                        return file
                    except shutil.Error as e:
                        errfile = "media/alredy"+str(i)+file
                        print()
                        os.rename(file_path,errfile)
                        txt =f"already[{file}]is[{errfile}]{e}"
                        logging.error(txt)
                        print(txt)
                        i += 1
                        
                    except Exception as e:
                        txt =f"Error!!:[{file}]{e}"
                        logging.error(txt)
                        print(txt)
                        input("")
                        
        else:
            print("Destination folder does not exist.")
        time.sleep(5)

# 監視するフォルダと移動先のフォルダを指定
source_folder = pysns_tool.getjson("iPhonefld")
destination_folder = pysns_tool.getjson("savefld")
pykit_tool.setup_logging("log/iPFle1.log")
while True:
        
    # フォルダを監視し、ファイルが追加されたら移動する
    fle = watch_folder(source_folder, destination_folder)
    print("追加されたファイル:", fle)


    
    last_dot_index = fle.rfind(".")
    extension = "" if last_dot_index == -1 else fle[last_dot_index + 1:]
    print(extension)
    if extension != "heic":        
        getjson = pysns_tool.getjson("discord")
        pysns_tool.send_discord(getjson,"",destination_folder + "/" + fle)
    print("fle情報書き込み")
    txt = f"{destination_folder}:{fle}"
    logging.info( txt)

    time.sleep(10)
