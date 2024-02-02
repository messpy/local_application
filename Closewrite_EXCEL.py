import openpyxl

# Excelファイルのパス
excel_file_path = 'your_excel_file.xlsx'

# ワークブックを開く
workbook = openpyxl.load_workbook(excel_file_path)

# シートを選択
sheet = workbook.active

# ユーザーに対話的に中心のセルを入力
center_row = int(input("中心のセルの行を入力してください: "))
center_column = int(input("中心のセルの列を入力してください: "))

# 周りの10×10のセルを表示
for row in range(center_row - 5, center_row + 5 + 1):
    for col in range(center_column - 5, center_column + 5 + 1):
        cell_value = sheet.cell(row=row, column=col).value
        print(f"セル({row}, {col})の値: {cell_value}")

# ワークブックを閉じる
workbook.close()