def position_valid(row_p, col_p, last_pos):
    if 0 <= row_p < int(row) and 0 <= col_p < int(col):
        return True
    return False


row, col = [int(el) for el in input().split(',')]
matrix = []
for r in range(row):
    sub_matrix = []
    for c in input():
        sub_matrix.append(c)
    matrix.append(sub_matrix)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
cheese_counter = 0
for row_pos in range(row):
    for col_pos in range(col):
        if matrix[row_pos][col_pos] == 'M':
            position = [row_pos, col_pos]
        elif matrix[row_pos][col_pos] == 'C':
            cheese_counter += 1

mouse_position = [position[0], position[1]]
while True:
    command = input()

    if command == 'danger':
        print(f"Mouse will come back later!")
        last_position = [mouse_position]
        break
    if cheese_counter == 0:
        break

    next_row_position = directions[command][0] + mouse_position[0]
    next_col_position = directions[command][1] + mouse_position[1]
    last_position = [mouse_position[0], mouse_position[1]]
    validate = position_valid(next_row_position, next_col_position, last_position)
    if validate:

        if command == 'down':
            if matrix[next_row_position][next_col_position] == '@':
                continue
            if matrix[next_row_position][next_col_position] == 'T':
                print(f"Mouse is trapped!")
                matrix[next_row_position][next_col_position] = 'M'
                matrix[last_position[0]][last_position[1]] = '*'
                break
            if matrix[next_row_position][next_col_position] == 'C':
                cheese_counter -= 1
                mouse_position = [next_row_position, next_col_position]
                matrix[next_row_position][next_col_position] = 'M'
            if matrix[next_row_position][next_col_position] == '*':
                matrix[next_row_position][next_col_position] = 'M'

        elif command == 'up':
            if matrix[next_row_position][next_col_position] == '@':
                continue
            if matrix[next_row_position][next_col_position] == 'T':
                print(f"Mouse is trapped!")
                matrix[next_row_position][next_col_position] = 'M'
                matrix[last_position[0]][last_position[1]] = '*'
                break
            if matrix[next_row_position][next_col_position] == 'C':
                cheese_counter -= 1
                mouse_position = [next_row_position, next_col_position]
                matrix[next_row_position][next_col_position] = 'M'
            if matrix[next_row_position][next_col_position] == '*':
                matrix[next_row_position][next_col_position] = 'M'

        elif command == 'left':
            if matrix[next_row_position][next_col_position] == '@':
                continue
            if matrix[next_row_position][next_col_position] == 'T':
                print(f"Mouse is trapped!")
                matrix[next_row_position][next_col_position] = 'M'
                matrix[last_position[0]][last_position[1]] = '*'
                break
            if matrix[next_row_position][next_col_position] == 'C':
                cheese_counter -= 1
                mouse_position = [next_row_position, next_col_position]
                matrix[next_row_position][next_col_position] = 'M'
            if matrix[next_row_position][next_col_position] == '*':
                matrix[next_row_position][next_col_position] = 'M'

        elif command == 'right':
            if matrix[next_row_position][next_col_position] == '@':
                continue
            if matrix[next_row_position][next_col_position] == 'T':
                print(f"Mouse is trapped!")
                matrix[next_row_position][next_col_position] = 'M'
                matrix[last_position[0]][last_position[1]] = '*'
                break
            if matrix[next_row_position][next_col_position] == 'C':
                cheese_counter -= 1
                mouse_position = [next_row_position, next_col_position]
                matrix[next_row_position][next_col_position] = 'M'
            if matrix[next_row_position][next_col_position] == '*':
                matrix[next_row_position][next_col_position] = 'M'
        mouse_position = [next_row_position, next_col_position]
        matrix[last_position[0]][last_position[1]] = '*'
    else:
        print(f"No more cheese for tonight!")
        break

if cheese_counter == 0:
    print(f"Happy mouse! All the cheese is eaten, good night!")
for r_c in matrix:
    print(''.join(r_c))