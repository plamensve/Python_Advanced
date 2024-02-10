import os

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "01_02_text.txt")
symbols = {"-", ",", ".", "!", "?"}

with open(file_path, "r") as f:
    result = f.readlines()

for i in range(0, len(result), 2):
    for symbol in symbols:
        result[i] = result[i].replace(symbol, "@")

    for word in reversed(result[i].split()):
        print(word, end = " ")

    if i != len(result) - 1: print()
        