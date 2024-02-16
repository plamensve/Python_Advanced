from collections import deque


def check_index(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return row, col
    print(f"The squirrel is out of the field.")
    print(f"Hazelnuts collected: {hazelnuts}")
    exit()


SIZE = int(input())
hazelnuts = 0
commands = deque([command for command in input().split(', ')])

matrix = []
for row in range(SIZE):
    sub_matrix = []
    for col in list(input()):
        sub_matrix.append(col)
    if 's' in sub_matrix:
        position = [row, sub_matrix.index('s')]
    matrix.append(sub_matrix)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while commands:
    command = commands.popleft()
    next_row = directions[command][0] + position[0]
    next_col = directions[command][1] + position[1]

    next_row, next_col = check_index(next_row, next_col)
    next_symbol = matrix[next_row][next_col]
    if next_symbol == 'h':
        matrix[next_row][next_col] = '*'
        hazelnuts += 1
        position = [next_row, next_col]

    elif next_symbol == '*':
        position = [next_row, next_col]

    elif next_symbol == 't':
        print(f"Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {hazelnuts}")
        exit()

if hazelnuts == 3:
    print(f"Good job! You have collected all hazelnuts!")
    print(f"Hazelnuts collected: {hazelnuts}")

else:
    print(f"There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {hazelnuts}")