import openpyxl

# Excelファイルのパス
excel_file_path = 'test.xlsx'

# ワークブックを開く
workbook = openpyxl.load_workbook(excel_file_path)

rowclm = 5

def first_choice():   
    # シートを選択
    sheet_names = workbook.sheetnames
    i = 0
    for shtname in sheet_names:
        print(str(i)+shtname)
        i += 1
        shtnum=int(input("何番目のシートを表示しますか？"))
        center_cell_address = input("Cellを選択してください (例: E6): ")  # 修正
        sht = workbook.worksheets[shtnum]
        center_cell = sht[center_cell_address]  # 修正
        return sht, center_cell




def cell_display(rowclm, sht, center_cell):        
    center_row, center_column = center_cell.row, center_cell.column

    # ヘッダー行
    print("   ", end="")
    for col_offset in range(-2, 3):
        target_column = center_column + col_offset
        if 1 <= target_column <= sht.max_column:
            print(f"{sht.cell(row=1, column=target_column).column_letter:^10}", end="")
        else:
            print(" " * 10, end="")
    print()  # 改行

    for row_offset in range(-2, 3):
        target_row = center_row + row_offset

        if 1 <= target_row <= sht.max_row:
            print(f"{target_row:2d} ", end="")
            for col_offset in range(-2, 3):
                target_column = center_column + col_offset
                
                if 1 <= target_column <= sht.max_column:
                    current_cell = sht.cell(row=target_row, column=target_column)
                    print(f"{str(current_cell.value):^10}", end="")
                else:
                    print(" " * 10, end="")  # 列が存在しない場合は空白セル

            print()  # 改行

if __name__ == "__main__":
    sht, center_cell = first_choice()
    cell_display(rowclm, sht, center_cell)

    # ワークブックを閉じる
    workbook.close()
