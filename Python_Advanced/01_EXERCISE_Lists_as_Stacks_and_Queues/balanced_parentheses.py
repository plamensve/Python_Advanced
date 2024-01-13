from collections import deque

parentheses_string = input()
balanced = 0

sequence_of_chars = deque()
for char in parentheses_string:
    sequence_of_chars.append(char)

sequence_of_chars_copy = sequence_of_chars.copy()
for index in range(0, len(sequence_of_chars), 2):

    if sequence_of_chars[index] == '{' and sequence_of_chars[index + 1] == '}':
        sequence_of_chars_copy.popleft()
        sequence_of_chars_copy.popleft()

    elif sequence_of_chars[index] == '(' and sequence_of_chars[index + 1] == ')':
        sequence_of_chars_copy.popleft()
        sequence_of_chars_copy.popleft()

    elif sequence_of_chars[index] == '[' and sequence_of_chars[index + 1] == ']':
        sequence_of_chars_copy.popleft()
        sequence_of_chars_copy.popleft()

if not sequence_of_chars_copy:
    print('YES')
else:
    result = len(sequence_of_chars) // 2
    while sequence_of_chars.copy():
        pop_a = sequence_of_chars.popleft()
        pop_b = sequence_of_chars.pop()
        if pop_a == '{' and pop_b == '}':
            result -= 1
        elif pop_a == '(' and pop_b == ')':
            result -= 1
        elif pop_a == '[' and pop_b == ']':
            result -= 1

    if result == 0:
        print('YES')
    else:
        print('NO')