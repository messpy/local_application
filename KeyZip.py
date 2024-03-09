import itertools

# A-zと0-9のリスト
alphabet = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")

# itertools.combinations_with_replacementを使って、8文字までのすべての組み合わせを生成
for i in range(1,8):
    print(str(i)+"*"*10)
    combinations = itertools.combinations_with_replacement(alphabet + numbers,i)
    # 組み合わせをすべて表示
    for combination in combinations:
        print("".join(combination))
