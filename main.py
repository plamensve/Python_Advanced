import os

path = os.path.join('D:', 'New Python Projects', '07_TEST_DIRECTORY', 'text.txt')

file = open(path)
print(file.read())