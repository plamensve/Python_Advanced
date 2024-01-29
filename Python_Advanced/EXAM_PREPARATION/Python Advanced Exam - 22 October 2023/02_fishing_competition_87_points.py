size = int(input())

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

ship_pos = []
for row in range(size):
    matrix.append(list(input()))

    if 'S' in matrix[row]:
        ship_pos = [row, matrix[row].index('S')]

sank_flag = False
collected_fish = 0
current_command = input()
while current_command != "collect the nets":

    curr_pos_row = directions[current_command][0] + ship_pos[0]
    curr_pos_col = directions[current_command][1] + ship_pos[1]

    if curr_pos_row >= size:
        curr_pos_row = 0
    elif curr_pos_row < 0:
        curr_pos_row = size - 1

    if curr_pos_col >= size:
        curr_pos_col = 0
    elif curr_pos_col < 0:
        curr_pos_col = size - 1

# ----- Down direction -----------------------------------------------------#
    if current_command == 'down':
        if matrix[curr_pos_row][curr_pos_col] == 'W':
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
                  f"Last coordinates of the ship: [{curr_pos_row},{curr_pos_col}]")
            sank_flag = True
            break

        elif matrix[curr_pos_row][curr_pos_col].isdigit():
            collected_fish += int(matrix[curr_pos_row][curr_pos_col])
            matrix[ship_pos[0]][ship_pos[1]] = '-'
            matrix[curr_pos_row][curr_pos_col] = 'S'
            ship_pos = [curr_pos_row, curr_pos_col]
        else:
            matrix[ship_pos[0]][ship_pos[1]] = '-'
            matrix[curr_pos_row][curr_pos_col] = 'S'
            ship_pos = [curr_pos_row, curr_pos_col]

# ----- Right direction -----------------------------------------------------#
    elif current_command == 'right':
        if matrix[curr_pos_row][curr_pos_col] == 'W':
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
                  f"Last coordinates of the ship: [{curr_pos_row},{curr_pos_col}]")
            sank_flag = True
            break

        elif matrix[curr_pos_row][curr_pos_col].isdigit():
            collected_fish += int(matrix[curr_pos_row][curr_pos_col])
            matrix[ship_pos[0]][ship_pos[1]] = '-'
            matrix[curr_pos_row][curr_pos_col] = 'S'
            ship_pos = [curr_pos_row, curr_pos_col]
        else:
            matrix[ship_pos[0]][ship_pos[1]] = '-'
            matrix[curr_pos_row][curr_pos_col] = 'S'
            ship_pos = [curr_pos_row, curr_pos_col]

# ----- Left direction -----------------------------------------------------#
    elif current_command == 'left':
        if matrix[curr_pos_row][curr_pos_col] == 'W':
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
                  f"Last coordinates of the ship: [{curr_pos_row},{curr_pos_col}]")
            sank_flag = True
            break

        elif matrix[curr_pos_row][curr_pos_col].isdigit():
            collected_fish += int(matrix[curr_pos_row][curr_pos_col])
            matrix[ship_pos[0]][ship_pos[1]] = '-'
            matrix[curr_pos_row][curr_pos_col] = 'S'
            ship_pos = [curr_pos_row, curr_pos_col]
        else:
            matrix[ship_pos[0]][ship_pos[1]] = '-'
            matrix[curr_pos_row][curr_pos_col] = 'S'
            ship_pos = [curr_pos_row, curr_pos_col]

# ----- Up direction -----------------------------------------------------#
    elif current_command == 'up':
        if matrix[curr_pos_row][curr_pos_col] == 'W':
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
                  f"Last coordinates of the ship: [{curr_pos_row},{curr_pos_col}]")
            sank_flag = True
            break

        elif matrix[curr_pos_row][curr_pos_col].isdigit():
            collected_fish += int(matrix[curr_pos_row][curr_pos_col])
            matrix[ship_pos[0]][ship_pos[1]] = '-'
            matrix[curr_pos_row][curr_pos_col] = 'S'
            ship_pos = [curr_pos_row, curr_pos_col]
        else:
            matrix[ship_pos[0]][ship_pos[1]] = '-'
            matrix[curr_pos_row][curr_pos_col] = 'S'
            ship_pos = [curr_pos_row, curr_pos_col]

    current_command = input()
if not sank_flag:
    if collected_fish >= 20:
        print(f"Success! You managed to reach the quota!")
        print(f"Amount of fish caught: {collected_fish} tons.")
        [print(''.join(el)) for el in matrix]
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} tons of fish "
              f"more.")
        if collected_fish > 0:
            print(f"Amount of fish caught: {collected_fish} tons.")
        [print(''.join(el)) for el in matrix]