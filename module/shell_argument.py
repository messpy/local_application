import sys

args = sys.argv

if len(args) > 1:
    argument = args[1]
    print(argument)
else:
    print("値がありません")
    argument = "None"
