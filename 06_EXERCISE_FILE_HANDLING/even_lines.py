import os

ABSOLUTE_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
file_name = 'text.txt'

path = os.path.join(ABSOLUTE_DIR_PATH, 'test', file_name)

symbols = ("-", ",", ".", "!", "?")
with open(path, 'r') as file:
    text = file.readlines()

for row in range(0, len(text), 2):

    for symbol in symbols:
        text[row] = text[row].replace(symbol, '@')

    print(*text[row].split()[::-1])