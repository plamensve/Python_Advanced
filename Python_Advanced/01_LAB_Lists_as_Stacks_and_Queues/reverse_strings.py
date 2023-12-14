string_line = input()
new_string = ''
for index in range(len(string_line), -1, -1):
    if index == 0:
        break
    new_string += string_line[index - 1]
print(new_string)
#testTestTestTestTestTestTestTestТestTestTest