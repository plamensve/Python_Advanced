numbers_as_string = input().split(' ')
new_stack = []

while len(numbers_as_string) > 0:
    pop_num = numbers_as_string.pop()
    new_stack.append(pop_num)

print(' '.join(new_stack))