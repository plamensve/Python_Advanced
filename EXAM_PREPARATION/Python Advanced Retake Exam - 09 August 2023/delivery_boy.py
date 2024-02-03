def validated_index(r, c):
    if 0 <= r < int(matrix_row) and 0 <= c < int(matrix_col):
        return True
    print(f"The delivery is late. Order is canceled.")
    matrix[start_position[0]][start_position[1]] = ' '
    for row in matrix:
        print(''.join(row))
    exit()


def next_position(next_r, next_c):
    if matrix[next_r][next_c] == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[next_r][next_c] = 'R'
        return False
    elif matrix[next_r][next_c] == 'A':
        print(f"Pizza is delivered on time! Next order...")
        matrix[next_r][next_c] = 'P'
        return True
    elif matrix[next_r][next_c] == '-':
        matrix[next_r][next_c] = 'B'
        matrix[position[0]][position[1]] = '.'
        return False


matrix_row, matrix_col = list(input().split())
matrix = []
for row in range(int(matrix_row)):
    sub_matrix = []
    for col in input():
        sub_matrix.append(col)
    matrix.append(sub_matrix)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
position = []
start_position = []
for r in range(int(matrix_row)):
    for c in range(int(matrix_col)):
        if matrix[r][c] == "B":
            position = [r, c]
            start_position = [r, c]

while True:
    command = input()
    if command == 'down':
        next_row = directions[command][0] + position[0]
        next_col = directions[command][1] + position[1]
        validated_index(next_row, next_col)
        if validated_index and matrix[next_row][next_col] != '*':
            position = [next_row, next_col]
        if matrix[next_row][next_col] == '*':
            continue
        else:
            result = next_position(next_row, next_col)
            if result:
                break
    elif command == 'up':
        next_row = directions[command][0] + position[0]
        next_col = directions[command][1] + position[1]
        validated_index(next_row, next_col)
        if validated_index and matrix[next_row][next_col] != '*':
            position = [next_row, next_col]
        if matrix[next_row][next_col] == '*':
            continue
        else:
            result = next_position(next_row, next_col)
            if result:
                break
    elif command == 'left':
        next_row = directions[command][0] + position[0]
        next_col = directions[command][1] + position[1]
        validated_index(next_row, next_col)
        if validated_index and matrix[next_row][next_col] != '*':
            position = [next_row, next_col]
        if matrix[next_row][next_col] == '*':
            continue
        else:
            result = next_position(next_row, next_col)
            if result:
                break
    elif command == 'right':
        next_row = directions[command][0] + position[0]
        next_col = directions[command][1] + position[1]
        validated_index(next_row, next_col)
        if validated_index and matrix[next_row][next_col] != '*':
            position = [next_row, next_col]
        if matrix[next_row][next_col] == '*':
            continue
        else:
            result = next_position(next_row, next_col)
            if result:
                break
matrix[start_position[0]][start_position[1]] = 'B'
for row in matrix:
    print(''.join(row))