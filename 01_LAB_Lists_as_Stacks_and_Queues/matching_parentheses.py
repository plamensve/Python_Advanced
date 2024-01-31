# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

string_line = input()
indexes = []
for index in range(len(string_line)):
    if string_line[index] == '(':
        indexes.append(index)
    elif string_line[index] == ')':
        start_index = indexes.pop()
        end_index = index + 1
        print(string_line[start_index:end_index])