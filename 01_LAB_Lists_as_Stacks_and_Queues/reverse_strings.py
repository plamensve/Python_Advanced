# string_line = input.txt()
# new_string = ''
# for index in range(len(string_line), -1, -1):
#     if index == 0:
#         break
#     new_string += string_line[index - 1]
# print(new_string)

string_line = list(input())
my_stack = []

while string_line:
    my_stack.append(string_line.pop())

print("".join(my_stack))