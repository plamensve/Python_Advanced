import os

path = os.path.join('..', 'test', 'new_file_in_another_dir.txt')

with open(path, 'a') as file:
    file.write('Some content')

"""
Създаваме файл в друга директория
"""