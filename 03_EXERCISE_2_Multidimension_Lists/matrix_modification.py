def index_is_valid(row, col): # -> int
    if rows > row >= 0 and rows > col >= 0:
        return True


rows = int(input())

matrix = [[int(el) for el in input().split()]for row in range(rows)]

command = input()
while command != 'END':
    current_command = command.split()
    action, r, c, number = current_command[0], int(current_command[1]), int(current_command[2]), int(current_command[3])

    if index_is_valid(r, c):

        if action == 'Add':
            matrix[r][c] += number

        elif action == 'Subtract':
            matrix[r][c] -= number
    else:
        print(f"Invalid coordinates")

    command = input()

[print(*el) for el in matrix]