import os
import zipfile
import shutil

# 実行ファイルのディレクトリを取得
current_directory = os.path.dirname(os.path.abspath(__file__))

# 実行ファイルのディレクトリにある圧縮ファイルを検索
zip_files = [f for f in os.listdir(current_directory) if f.endswith('.zip')]

# 各圧縮ファイルごとに処理
for zip_file in zip_files:
    # 圧縮ファイル名からフォルダ名を作成
    folder_name = os.path.splitext(zip_file)[0]
    print(folder_name)

    # フォルダを作成
    destination_folder = os.path.join(current_directory, folder_name)
    os.makedirs(destination_folder, exist_ok=True)

    # 圧縮ファイルを解凍
    with zipfile.ZipFile(os.path.join(current_directory, zip_file), 'r') as zip_ref:
        zip_ref.extractall(destination_folder)
        print(f"{destination_folder}を解凍中")

    # zipファイルを移動
    print("移動中")
    shutil.move(os.path.join(current_directory, zip_file), destination_folder)

print("解凍が完了しました。")
