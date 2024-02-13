def check_index(r, c):
    if 0 > r:
        return int(row) - 1, c
    elif r >= int(row):
        return 0, c

    if 0 > c:
        return r, int(col) - 1
    elif c >= int(col):
        return r, 0
    return r, c


row, col = input().split(', ')
matrix = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
counter = 0
collected_items = 0
flag = False

for r in range(int(row)):
    sub_matrix = []
    for c in input().split():
        sub_matrix.append(c)
        if 'Y' in sub_matrix:
            position = [r, sub_matrix.index('Y')]
        if c == 'D' or c == 'G' or c == 'C':
            counter += 1
    matrix.append(sub_matrix)

collected = {
    'D': 0,
    'G': 0,
    'C': 0,
}

command = input()
while command != 'End':
    current_command = command.split('-')
    direct, steps = current_command[0], int(current_command[1])

    for x in range(1, steps + 1):
        next_row = directions[direct][0] + position[0]
        next_col = directions[direct][1] + position[1]
        matrix[position[0]][position[1]] = 'x'

        if direct == 'up':
            n_row, n_col = check_index(next_row, next_col)
            position = [n_row, n_col]
            if matrix[n_row][n_col] in collected:
                collected[matrix[n_row][n_col]] += 1
                collected_items += 1
            matrix[n_row][n_col] = 'Y'
            if counter == collected_items:
                flag = True
                break

        elif direct == 'down':
            n_row, n_col = check_index(next_row, next_col)
            position = [n_row, n_col]
            if matrix[n_row][n_col] in collected:
                collected[matrix[n_row][n_col]] += 1
                collected_items += 1
            matrix[n_row][n_col] = 'Y'
            if counter == collected_items:
                flag = True
                break

        elif direct == 'left':
            n_row, n_col = check_index(next_row, next_col)
            position = [n_row, n_col]
            if matrix[n_row][n_col] in collected:
                collected[matrix[n_row][n_col]] += 1
                collected_items += 1
            matrix[n_row][n_col] = 'Y'
            if counter == collected_items:
                flag = True
                break

        elif direct == 'right':
            n_row, n_col = check_index(next_row, next_col)
            position = [n_row, n_col]
            if matrix[n_row][n_col] in collected:
                collected[matrix[n_row][n_col]] += 1
                collected_items += 1
            matrix[n_row][n_col] = 'Y'
            if counter == collected_items:
                flag = True
                break

    if flag:
        break
    command = input()

if flag:
    print(f"Merry Christmas!")

print(f"You've collected:")
for key, value in collected.items():
    if key == 'D':
        key = 'Christmas decorations'
    elif key == 'G':
        key = 'Gifts'
    elif key == 'C':
        key = 'Cookies'
    print(f"- {value} {key}")

for el in matrix:
    print(*el)