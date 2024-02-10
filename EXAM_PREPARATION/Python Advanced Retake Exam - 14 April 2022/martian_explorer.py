from collections import deque


def check_index(next_r, next_c):
    if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
        return next_r, next_c

    elif 0 > next_r and 0 <= next_c < SIZE:
        return next_r + SIZE, next_c
    elif 0 <= next_r == SIZE:
        return next_r - SIZE, next_c

    elif 0 <= next_r < SIZE and 0 > next_c:
        return next_r, next_c + SIZE
    elif 0 <= next_r < SIZE and next_c == SIZE:
        return next_r, next_c - SIZE


SIZE = 6
matrix = []
for row in range(SIZE):
    sub_matrix = []
    for col in input().split():
        sub_matrix.append(col)
        if 'E' in sub_matrix:
            position = [row, sub_matrix.index('E')]
    matrix.append(sub_matrix)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

resource = {
    'W': 'Water deposit',
    'M': 'Metal deposit',
    'C': 'Concrete deposit',
}

water = False
metal = False
concrete = False

deposit = 0
commands = deque([command for command in input().split(', ')])
while True:
    if not commands:
        break

    current_command = commands.popleft()
    next_row_index = directions[current_command][0] + position[0]
    next_col_index = directions[current_command][1] + position[1]

    next_row, next_col = check_index(next_row_index, next_col_index)
    next_symbol = matrix[next_row][next_col]

    if next_symbol == 'R':
        print(f"Rover got broken at {(next_row, next_col)}")
        break

    elif next_symbol == 'W' or next_symbol == 'M' or next_symbol == 'C':
        print(f"{resource[next_symbol]} found at {(next_row, next_col)}")
        position = [next_row, next_col]
        deposit += 1
        if next_symbol == 'W':
            water = True
        elif next_symbol == 'M':
            metal = True
        elif next_symbol == 'C':
            concrete = True

    elif next_symbol == '-':
        position = [next_row, next_col]
        continue


if deposit > 0:
    if water and metal and concrete:
        print(f"Area suitable to start the colony.")
    else:
        print(f"Area not suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")