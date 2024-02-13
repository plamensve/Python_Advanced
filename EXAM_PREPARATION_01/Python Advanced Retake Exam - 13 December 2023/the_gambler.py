size = int(input())
amount = 100

matrix = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    sub_matrix = []
    for col in input():
        sub_matrix.append(col)
        if 'G' in sub_matrix:
            position = [row, sub_matrix.index('G')]
    matrix.append(sub_matrix)

lost = False
matrix[position[0]][position[1]] = '-'
command = input()
while command != 'end':
    next_row = directions[command][0] + position[0]
    next_col = directions[command][1] + position[1]
    next_symbol = matrix[next_row][next_col]
    last_pos = [position[0], position[1]]

    if 0 > next_row:
        break
    elif next_row >= size:
        break
    elif 0 > next_col:
        break
    elif next_col >= size:
        break

    if next_symbol == 'W':
        amount += 100
    elif next_symbol == 'P':
        amount -= 200
        if amount <= 0:
            print("Game over! You lost everything!")
            lost = True
            break

    elif next_symbol == 'J':
        amount += 100000
        print(f"You win the Jackpot!")
        break

    elif next_symbol == '-':
        matrix[next_row][next_col] = 'G'

    position = [next_row, next_col]
    matrix[next_row][next_col] = 'G'
    matrix[last_pos[0]][last_pos[1]] = '-'
    command = input()

if not lost:
    print(f"End of the game. Total amount: {amount}$")
    for el in matrix:
        print(''.join(el))