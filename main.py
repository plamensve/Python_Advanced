import os

file_name = 'text.txt'
path = os.path.join('test', file_name)

try:
    file = open(path)
    print('File found!')
    print(file.read())
except FileNotFoundError:
    print('File not found!')
