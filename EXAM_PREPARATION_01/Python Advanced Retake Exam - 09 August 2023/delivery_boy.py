def move(r, c, row_size, col_size):
    return 0 <= r < row_size and 0 <= c < col_size


size = [int(s) for s in input().split(' ')]
matrix = []
initial_position = None

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row_index in range(size[0]):
    data = list(input())

    if "B" in data:
        col_index = data.index("B")
        initial_position = (row_index, col_index)
    matrix.append(data)

current_position = initial_position
star_pos = initial_position
while True:
    command = input()

    next_row = directions[command][0] + current_position[0]
    next_col = directions[command][1] + current_position[1]
    result = move(next_row, next_col, size[0], size[1])

    if not result:
        print(f"The delivery is late. Order is canceled.")
        matrix[star_pos[0]][star_pos[1]] = ' '
        break

    next_symbol = matrix[next_row][next_col]

    if next_symbol == '*':
        continue

    current_position = [next_row, next_col]

    if next_symbol == 'P':
        print(f"Pizza is collected. 10 minutes for delivery.")
        matrix[next_row][next_col] = 'R'

    elif next_symbol == 'A':
        print(f"Pizza is delivered on time! Next order...")
        matrix[next_row][next_col] = 'P'
        break

    elif next_symbol == '-':
        matrix[next_row][next_col] = '.'

[print(''.join(el)) for el in matrix]
