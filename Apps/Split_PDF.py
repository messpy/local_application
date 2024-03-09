import PyPDF2
import os

# 処理対象のPDFファイルパス
input_dir = "./input"

# 出力ディレクトリ
output_dir = "./output"

# 出力ファイル名フォーマット
output_filename_format = "{name}_{page:03d}.pdf"

# 入力ディレクトリ内のPDFファイル一覧を取得
files = os.listdir(input_dir)

# 各ファイルに対して処理を行う
for file in files:
  # 入力ファイルパス
  input_filepath = os.path.join(input_dir, file)

  # 出力ファイル名
  output_filename = output_filename_format.format(
      name=os.path.splitext(file)[0],
      page=1,
  )

  # PDFリーダーオブジェクトを作成
  reader = PyPDF2.PdfReader(input_filepath)

  # ページ数
  num_pages = reader.numPages

  # 各ページを分割して保存
  for page_num in range(num_pages):
    # 出力ファイルパス
    output_filepath = os.path.join(output_dir, output_filename)

    # PDFライターオブジェクトを作成
    writer = PyPDF2.PdfWriter()

    # 現在のページを追加
    writer.addPage(reader.getPage(page_num))

    # PDFファイルを保存
    with open(output_filepath, "wb") as f:
      writer.write(f)

    # 出力ファイル名
    output_filename = output_filename_format.format(
        name=os.path.splitext(file)[0],
        page=page_num + 1,
    )

