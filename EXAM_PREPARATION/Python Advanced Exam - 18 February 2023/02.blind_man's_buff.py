def find_my_cooridnates(r, c, mtrx):
    for row in range(r):
        for col in range(c):
            if mtrx[row][col] == "B":
                return [row, col]


def check_my_next_position(my_row, my_col, current_matrix):
    if 0 <= my_row < len(current_matrix) and 0 <= my_col < len(current_matrix[0]):
        next_position = current_matrix[my_row][my_col]
        if next_position == "O":
            return False
        elif next_position == "-":
            return [my_row, my_col], current_matrix, 0
        elif next_position == "P":
            current_matrix[my_row][my_col] = "-"
            return [my_row, my_col], current_matrix, 1


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input().split())


my_coordinates = find_my_cooridnates(n, m, matrix)
matrix[my_coordinates[0]][my_coordinates[1]] = "-"
result = False
touched_opponents = 0
moves_made = 0

while True:
    if touched_opponents == 3:
        break

    command = input()
    if command == 'Finish':
        break

    if command == 'up':
        result = check_my_next_position(my_coordinates[0] - 1, my_coordinates[1], matrix)
    elif command == 'down':
        result = check_my_next_position(my_coordinates[0] + 1, my_coordinates[1], matrix)
    elif command == 'left':
        result = check_my_next_position(my_coordinates[0], my_coordinates[1] - 1, matrix)
    elif command == 'right':
        result = check_my_next_position(my_coordinates[0], my_coordinates[1] + 1, matrix)

    if result:
        my_coordinates, matrix, touches = result
        touched_opponents += touches
        moves_made += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")

