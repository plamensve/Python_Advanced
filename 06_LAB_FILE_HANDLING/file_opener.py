import os

path = os.path.join('..', '07_TEST_DIRECTORY', 'text.txt')

file = open(path)
print(file.read())
