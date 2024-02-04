from collections import deque


def validate_index(row: int, col: int):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    print(f"The squirrel is out of the field.")
    print(f"Hazelnuts collected: {hazelnuts}")
    exit()


def move(move_r, move_c):
    global hazelnuts
    if matrix[move_r][move_c] == 't':
        print(f"Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {hazelnuts}")
        exit()
    elif matrix[move_r][move_c] == '*':
        return move_r, move_c
    elif matrix[move_r][move_c] == 'h':
        hazelnuts += 1
        matrix[move_r][move_c] = '*'
        return move_r, move_c,


size = int(input())
commands_list = deque([c for c in input().split(', ')])

matrix = []
for r in range(size):
    sub_matrix = []
    for c in input():
        sub_matrix.append(c)
    matrix.append(sub_matrix)

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "s":
            position = [r, c]

matrix[position[0]][position[1]] = "*"
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

hazelnuts = 0
while True:
    if not commands_list:
        break

    for index in range(len(commands_list)):
        if hazelnuts == 3:
            print(f"Good job! You have collected all hazelnuts!")
            print(f"Hazelnuts collected: {hazelnuts}")
            exit()
        command = commands_list.popleft()
        if command == 'left':
            next_row = directions[command][0] + position[0]
            next_col = directions[command][1] + position[1]
            validate_index(next_row, next_col)
            if validate_index:
                next_row, next_col = move(next_row, next_col)
                position = [next_row, next_col]

        elif command == 'right':
            next_row = directions[command][0] + position[0]
            next_col = directions[command][1] + position[1]
            validate_index(next_row, next_col)
            if validate_index:
                next_row, next_col = move(next_row, next_col)
                position = [next_row, next_col]

        elif command == 'down':
            next_row = directions[command][0] + position[0]
            next_col = directions[command][1] + position[1]
            validate_index(next_row, next_col)
            if validate_index:
                next_row, next_col = move(next_row, next_col)
                position = [next_row, next_col]

        elif command == 'up':
            next_row = directions[command][0] + position[0]
            next_col = directions[command][1] + position[1]
            validate_index(next_row, next_col)
            if validate_index:
                next_row, next_col = move(next_row, next_col)
                position = [next_row, next_col]

if hazelnuts < 3:
    print(f"There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {hazelnuts}")
elif hazelnuts == 3:
    print(f"Good job! You have collected all hazelnuts!")
    print(f"Hazelnuts collected: {hazelnuts}")