import os
with open('my_first_file.txt', 'a') as file:
    file.write('I just created my first file!')

path = os.path.join('my_first_file.txt')
change = open(path, 'a')
change.write('\nHello, I am Plamen Svetoslavov')

"""
Създаваме файл в същата директория
"""