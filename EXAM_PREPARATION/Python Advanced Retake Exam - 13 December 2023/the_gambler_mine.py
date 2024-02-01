amount = 100


def last_pos():
    matrix[current_row][current_col] = '-'


def valid_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    else:
        print(f"Game over! You lost everything!")
        exit()


def pos_loot(loot: str):
    global amount
    if loot == 'W':
        amount += 100
        matrix[g_pos[0]][g_pos[1]] = 'G'

    elif loot == 'P':
        amount -= 200
        if amount <= 0:
            print(f"Game over! You lost everything!")
            exit()

    elif loot == 'J':
        amount += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {amount}$")
        matrix[g_pos[0]][g_pos[1]] = 'G'
        [print(''.join(el)) for el in matrix]
        exit()


size = int(input())
matrix = [[j for j in input()] for i in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

g_pos = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'G':
            g_pos = [row, col]

while True:
    command = input()
    if command == 'end':
        break

    current_row = g_pos[0]
    current_col = g_pos[1]
    next_row = directions[command][0] + current_row
    next_col = directions[command][1] + current_col
    g_pos = [next_row, next_col]

    if command == 'down':
        last_pos()
        valid_index(next_row, next_col)
        if valid_index:
            loot = matrix[next_row][next_col]
            pos_loot(loot)

    elif command == 'up':
        last_pos()
        valid_index(next_row, next_col)
        if valid_index:
            loot = matrix[next_row][next_col]
            pos_loot(loot)

    elif command == 'left':
        last_pos()
        valid_index(next_row, next_col)
        if valid_index:
            loot = matrix[next_row][next_col]
            pos_loot(loot)

    elif command == 'right':
        last_pos()
        valid_index(next_row, next_col)
        if valid_index:
            loot = matrix[next_row][next_col]
            pos_loot(loot)

print(f"End of the game. Total amount: {amount}$")
matrix[g_pos[0]][g_pos[1]] = 'G'
[print(''.join(el)) for el in matrix]
