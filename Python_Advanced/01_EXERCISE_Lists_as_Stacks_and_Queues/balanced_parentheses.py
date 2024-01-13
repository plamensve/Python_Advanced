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
    else:
        break


if not sequence_of_chars_copy:
    print('YES')
else:
    cop_sequence = sequence_of_chars.copy()
    index_a = len(sequence_of_chars) - 1
    for index in range(len(sequence_of_chars)):
        if sequence_of_chars[index] == '{' and sequence_of_chars[index_a] == '}':
            cop_sequence.popleft()
            cop_sequence.pop()
            index_a -= 1

        elif sequence_of_chars[index] == '(' and sequence_of_chars[index_a] == ')':
            cop_sequence.popleft()
            cop_sequence.pop()
            index_a -= 1

        elif sequence_of_chars[index] == '[' and sequence_of_chars[index_a] == ']':
            cop_sequence.popleft()
            cop_sequence.pop()
            index_a -= 1
        else:
            break
    if not cop_sequence:
        print('YES')
    else:
        print('NO')
