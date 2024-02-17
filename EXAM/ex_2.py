size = int(input())
armor = 300
enemy = 0

matrix = []
for row in range(size):
    sub_matrix = []
    for col in list(input()):
        sub_matrix.append(col)
        if col == 'E':
            enemy += 1
    if 'J' in sub_matrix:
        position = [row, sub_matrix.index('J')]
    matrix.append(sub_matrix)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix[position[0]][position[1]] = '-'
while True:
    if enemy == 0:
        break
    if armor == 0:
        break

    command = input()

    next_row = directions[command][0] + position[0]
    next_col = directions[command][1] + position[1]
    next_symbol = matrix[next_row][next_col]

    if next_symbol == '-':
        position = [next_row, next_col]

    elif next_symbol == 'E':
        matrix[next_row][next_col] = '-'
        enemy -= 1
        if enemy == 0:
            print(f"Mission accomplished, you neutralized the aerial threat!")
            matrix[next_row][next_col] = 'J'
            break
        else:
            armor -= 100
            position = [next_row, next_col]
            if armor <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
                matrix[next_row][next_col] = 'J'
                break

    elif next_symbol == 'R':
        armor = 300
        matrix[next_row][next_col] = '-'
        position = [next_row, next_col]

    elif next_symbol == 'J':
        matrix[next_row][next_col] = '-'
        position = [next_row, next_col]

for el in matrix:
    print(''.join(el))
