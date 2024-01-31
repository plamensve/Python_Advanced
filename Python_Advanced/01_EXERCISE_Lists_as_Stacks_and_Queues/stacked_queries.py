def push_the_number(number_1):
    my_stack.append(number_1)


def delete_the_number():
    if my_stack:
        my_stack.pop()


def max_number_in_the_stack():
    if my_stack:
        print(max(my_stack))


def min_number_in_the_stack():
    if my_stack:
        print(min(my_stack))


queries_number = int(input())
my_stack = []

for query in range(queries_number):
    current_command = input().split()
    if current_command[0] == '1':
        push_the_number(int(current_command[1]))

    elif current_command[0] == '2':
        delete_the_number()

    elif current_command[0] == '3':
        max_number_in_the_stack()

    elif current_command[0] == '4':
        min_number_in_the_stack()

my_stack.reverse()
print(*my_stack, sep=', ')