size = int(input())

matrix = []
battle_cruiser = 0

for r in range(size):
    sub_matrix = []
    for c in input():
        sub_matrix.append(c)
        if c == 'S':
            position = [r, sub_matrix.index('S')]
        if c == 'C':
            battle_cruiser += 1
    matrix.append(sub_matrix)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
naval_mine = 0
matrix[position[0]][position[1]] = '-'
while True:
    if battle_cruiser == 0:
        print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        matrix[position[0]][position[1]] = 'S'
        for row in matrix:
            print(''.join(row))
        break
    if naval_mine > 2:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
        matrix[position[0]][position[1]] = 'S'
        for row in matrix:
            print(''.join(row))
        break

    command = input()

    next_row = directions[command][0] + position[0]
    next_col = directions[command][1] + position[1]

    if matrix[next_row][next_col] == '*':
        matrix[next_row][next_col] = '-'
        naval_mine += 1
        position = [next_row, next_col]

    elif matrix[next_row][next_col] == 'C':
        matrix[next_row][next_col] = '-'
        battle_cruiser -= 1
        position = [next_row, next_col]

    elif matrix[next_row][next_col] == '-':
        position = [next_row, next_col]
















