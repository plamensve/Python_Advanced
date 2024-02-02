import os
from string import punctuation

ABSOLUTE_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
file_name = 'text.txt'
path = os.path.join(ABSOLUTE_DIR_PATH, 'test', file_name)

path_output = os.path.join('..', 'test', 'output.txt')
output_file = open(path_output, 'a')

with open(path, 'r') as file:
    text = file.readlines()
    for row in range(len(text)):
        letter = 0
        symbol = 0
        for el in text[row]:
            if el.isalpha():
                letter += 1
            elif el in punctuation:
                symbol += 1

        output_file.write(f"Line {row + 1}: {text[row]}({letter})({symbol})\n")

output_file.close()