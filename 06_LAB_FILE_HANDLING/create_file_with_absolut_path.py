import os

ABSOLUTE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
file_name = 'next_just_created.txt'
path = os.path.join(ABSOLUTE_DIR_PATH, '..', 'test', file_name)
with open(path, 'a') as file:
    file.write('Congratulations!!!')


"""
Създаваме абсолютен път до директорията в която се намира файла който рънва скрипта. В променливата path
записваме ABSOLUTE_DIR_PATH -> в случая се намираме вътре в директорията на скрипта -> '..' с тази команда излизаме
извън директорията и насочваме към 'test', най-накрая създаваме file_name, което е име на променлива, която пази името на файла.
"""