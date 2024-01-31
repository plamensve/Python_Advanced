def shoot(direct: str):
    r = position[0] + directions[direct][0]
    c = position[1] + directions[direct][1]
    while 0 <= r < SIZE and 0 <= c < SIZE:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]

        r += directions[direct][0]
        c += directions[direct][1]


def move(direct: str, new_p: int):
    new_position_row = position[0] + directions[direct][0] * new_p
    new_position_col = position[1] + directions[direct][1] * new_p
    if 0 <= new_position_row < SIZE and 0 <= new_position_col < SIZE and matrix[new_position_row][new_position_col] == '.':
        return [new_position_row, new_position_col]
    return position


SIZE = 5

matrix = []
number_of_targets = 0
targets_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        position = [row, matrix[row].index('A')]

    if 'x' in matrix[row]:
        number_of_targets += matrix[row].count('x')

for command in range(int(input())):
    current_command = input().split()
    if current_command[0] == 'shoot':
        result = shoot(current_command[1])
        if result:
            targets_position.append(result)

    elif current_command[0] == 'move':
        new_position = move(current_command[1], int(current_command[2]))
        if new_position:
            position = new_position

if len(targets_position) < number_of_targets:
    print(f"Training not completed! {number_of_targets - len(targets_position)} targets left.")
    for t in targets_position:
        print(t)
else:
    print(f"Training completed! All {number_of_targets} targets hit.")
    for t in targets_position:
        print(t)
