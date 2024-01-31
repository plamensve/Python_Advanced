import os

ABSOLUTE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
file_name = 'next_just_created.txt'
path = os.path.join(ABSOLUTE_DIR_PATH, '..', 'test', file_name)
with open(path, 'a') as file:
    file.write('Congratulations!!!')