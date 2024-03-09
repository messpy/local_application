from googletrans import Translator

# 翻訳したいテキスト
text = input("翻訳[en-jp]:")

# 翻訳先の言語コード
to_lang = "ja"

# Translatorインスタンスを作成
translator = Translator()

# 翻訳を実行
translation = translator.translate(text, dest=to_lang)

# 翻訳結果を出力
print(translation.text)
