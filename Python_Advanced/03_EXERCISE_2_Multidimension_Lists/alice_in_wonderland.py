def index_is_valid(n_row, n_col):
    if 0 <= next_row < size and 0 <= next_col < size:
        return True


size = int(input())
matrix = []
bags_of_tea = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[alice_pos[0]][alice_pos[1]] = "*"

command = input()
while True:
    next_row = alice_pos[0] + directions[command][0]
    next_col = alice_pos[1] + directions[command][1]
    check_index = index_is_valid(next_row, next_col)

    if not check_index:
        print(f"Alice didn't make it to the tea party.")
        break

    elif matrix[next_row][next_col] == 'R':
        print(f"Alice didn't make it to the tea party.")
        matrix[next_row][next_col] = '*'
        break
    else:
        if matrix[next_row][next_col].isdigit():
            bags_of_tea += int(matrix[next_row][next_col])
            matrix[next_row][next_col] = '*'
            alice_pos = [next_row, next_col]
        else:
            alice_pos = [next_row, next_col]
            matrix[next_row][next_col] = '*'

    if bags_of_tea >= 10:
        print(f"She did it! She went to the party.")
        matrix[next_row][next_col] = '*'
        break

    command = input()

for el in matrix:
    print(*el)
