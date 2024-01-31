string_line = [string.split() for string in input().split('|')]
string_line.reverse()


for el in range(len(string_line)):
    print(*string_line[el], end=' ')

