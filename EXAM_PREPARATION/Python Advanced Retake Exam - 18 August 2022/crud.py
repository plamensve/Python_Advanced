matrix = []
for r in range(6):
    sub_matrix = []
    for c in input().split():
        sub_matrix.append(c)
    matrix.append(sub_matrix)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

start = input().split("(,")
position = [int(start[0][1]), int(start[0][4])]

command = input()
while command != 'Stop':
    current_command = command.split(', ')
    action, *direction = current_command

    next_row = position[0] + directions[direction[0]][0]
    next_col = position[1] + directions[direction[0]][1]
    next_symbol_on_matrix = matrix[next_row][next_col]
    if action == 'Create' and next_symbol_on_matrix == '.':
        matrix[next_row][next_col] = direction[1]

    elif action == 'Update':
        if next_symbol_on_matrix.isalpha() or next_symbol_on_matrix.isdigit():
            matrix[next_row][next_col] = direction[1]

    elif action == 'Delete':
        matrix[next_row][next_col] = '.'

    elif action == 'Read':
        if next_symbol_on_matrix.isalpha() or next_symbol_on_matrix.isdigit():
            print(matrix[next_row][next_col])

    position = [next_row, next_col]

    command = input()

for row_m in matrix:
    print(' '.join(row_m))