def index_valid(r, c):
    if 0 <= r < size_r and 0 <= c < size_c:
        return True
    return False


def obstacles(r, c):
    global touched_opponents
    global moves_counter
    if matrix[r][c] == 'O':
        return True
    elif matrix[r][c] == 'P':
        moves_counter += 1
        touched_opponents += 1
        matrix[current_position[0]][current_position[1]] = '-'
        return False
    elif matrix[r][c] == '-':
        moves_counter += 1
        matrix[current_position[0]][current_position[1]] = '-'
        return False


size_r, size_c = [int(x) for x in input().split()]

matrix = []
for row in range(size_r):
    sub_matrix = []
    for col in input().split():
        sub_matrix.append(col)
    matrix.append(sub_matrix)

for row_index in range(size_r):
    for col_index in range(size_c):
        if matrix[row_index][col_index] == 'B':
            position = [row_index, col_index]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
current_position = [position[0], position[1]]
touched_opponents = 0
moves_counter = 0
while True:
    command = input()
    if command == 'Finish':
        print(f'Game over!')
        print(f"Touched opponents: {touched_opponents} Moves made: {moves_counter}")
        break
    elif touched_opponents == 3:
        print(f"Game over!")
        print(f"Touched opponents: {touched_opponents} Moves made: {moves_counter}")
        break

    next_row = directions[command][0] + current_position[0]
    next_col = directions[command][1] + current_position[1]

    if command == 'down':
        if index_valid(next_row, next_col):
            if obstacles(next_row, next_col):
                continue
            else:
                matrix[next_row][next_col] = 'B'
                current_position = [next_row, next_col]
        else:
            continue

    elif command == 'up':
        if index_valid(next_row, next_col):
            if obstacles(next_row, next_col):
                continue
            else:
                matrix[next_row][next_col] = 'B'
                current_position = [next_row, next_col]
        else:
            continue

    elif command == 'left':
        if index_valid(next_row, next_col):
            if obstacles(next_row, next_col):
                continue
            else:
                matrix[next_row][next_col] = 'B'
                current_position = [next_row, next_col]
        else:
            continue

    elif command == 'right':
        if index_valid(next_row, next_col):
            if obstacles(next_row, next_col):
                continue
            else:
                matrix[next_row][next_col] = 'B'
                current_position = [next_row, next_col]
        else:
            continue

