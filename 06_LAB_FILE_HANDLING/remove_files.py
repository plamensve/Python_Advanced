import os

try:
    path = os.path.join('..', 'test', 'for_remove.txt')
    os.remove(path)
    print(f'File is deleted')
except FileNotFoundError:
    print('File is already deleted!')

