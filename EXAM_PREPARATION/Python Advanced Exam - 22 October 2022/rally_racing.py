size = int(input())
racing_number = input()

matrix = []
for r in range(size):
    sub_matrix = []
    for c in input().split():
        sub_matrix.append(c)
    matrix.append(sub_matrix)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

kilometers = 0
position = [0, 0]
finish_line = []
tunnel_coordinates = []
for x in range(len(matrix)):
    for y in range(len(matrix)):
        if matrix[x][y] == 'T':
            tunnel_coordinates.append([x, y])
        if matrix[x][y] == 'F':
            finish_line = [x, y]

command = input()
while True:
    if command == 'End':
        print(f"Racing car {racing_number} DNF.")
        print(f"Distance covered {kilometers} km.")
        matrix[position[0]][position[1]] = 'C'
        for row in matrix:
            print(''.join(row))
        exit()

    next_row = directions[command][0] + position[0]
    next_col = directions[command][1] + position[1]
    next_point = matrix[next_row][next_col]

    if next_point == '.':
        position = [next_row, next_col]
        kilometers += 10

    elif next_point == 'T':
        tunnel_entry = tunnel_coordinates.index([next_row, next_col])
        tunnel_index = 0
        if tunnel_entry == 0:
            tunnel_index = 1
        else:
            tunnel_index = 0
        position = tunnel_coordinates[tunnel_index]
        kilometers += 30
        matrix[tunnel_coordinates[0][0]][tunnel_coordinates[0][1]] = '.'
        matrix[tunnel_coordinates[1][0]][tunnel_coordinates[1][1]] = '.'

    elif next_point == 'F':
        print(f"Racing car {racing_number} finished the stage!")
        print(f"Distance covered {kilometers + 10} km.")
        matrix[finish_line[0]][finish_line[1]] = "C"
        for row in matrix:
            print(''.join(row))
        exit()
    command = input()