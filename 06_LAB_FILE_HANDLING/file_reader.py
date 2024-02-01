import os

file_name = 'numbers.txt'
path = os.path.join('..', 'test', file_name)

file = open(path)
sum_numbers = 0

for num in file.readlines():
    sum_numbers += int(num)

print(sum_numbers)

#test