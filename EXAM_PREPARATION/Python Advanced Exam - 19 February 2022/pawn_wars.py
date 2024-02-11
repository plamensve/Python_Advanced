def chess_position(pos_row, pos_col):
    coordinates = [pos_row, pos_col]
    for r in range(SIZE):
        for c in range(SIZE):
            letter = chr(c + 97)
            number = 8 - r
            if [r, c] == coordinates:
                return f"{letter}{number}"


def check_win_white(pos_row, pos_col):
    if matrix[pos_row - 1][pos_col - 1] == 'b':
        matrix[pos_row - 1][pos_col - 1] = 'w'
        matrix[pos_row][pos_col] = '-'
        print(f"Game over! White win, capture on {chess_position(pos_row - 1, pos_col - 1)}.")
        return True

    if matrix[pos_row - 1][pos_col + 1] == 'b':
        matrix[pos_row - 1][pos_col + 1] = 'w'
        matrix[pos_row][pos_col] = '-'
        print(f"Game over! White win, capture on {chess_position(pos_row - 1, pos_col + 1)}.")
        return True


def check_win_black(pos_row, pos_col):
    if matrix[pos_row + 1][pos_col - 1] == 'w':
        matrix[pos_row + 1][pos_col - 1] = 'b'
        matrix[pos_row][pos_col] = '-'
        print(f"Game over! Black win, capture on {chess_position(pos_row + 1, pos_col - 1)}.")
        return True

    if matrix[pos_row + 1][pos_col + 1] == 'w':
        matrix[pos_row + 1][pos_col + 1] = 'b'
        matrix[pos_row][pos_col] = '-'
        print(f"Game over! Black win, capture on {chess_position(pos_row + 1, pos_col + 1)}.")
        return True


def white_queen(pos_row, pos_col):
    if pos_row - 1 == 0:
        print(f"Game over! White pawn is promoted to a queen at {chess_position(pos_row - 1, pos_col)}.")
        matrix[pos_row - 1][pos_col] = 'w'
        matrix[pos_row][pos_col] = '-'
        return True


def black_queen(pos_row, pos_col):
    if pos_row + 1 == 7:
        print(f"Game over! Black pawn is promoted to a queen at {chess_position(pos_row + 1, pos_col)}.")
        matrix[pos_row + 1][pos_col] = 'b'
        matrix[pos_row][pos_col] = '-'
        return True


SIZE = 8
matrix = []
for row in range(SIZE):
    add_row = list(input().split())
    matrix.append(add_row)
    if 'b' in add_row:
        black_position = [row, add_row.index('b')]
    if 'w' in add_row:
        white_position = [row, add_row.index('w')]

turn = 1
while True:

    if turn % 2 != 0:
        if check_win_white(white_position[0], white_position[1]):
            break
        elif white_queen(white_position[0], white_position[1]):
            break
        else:
            matrix[white_position[0]][white_position[1]] = '-'
            white_position = [white_position[0] - 1, white_position[1]]
            matrix[white_position[0]][white_position[1]] = 'w'

    else:
        if check_win_black(black_position[0], black_position[1]):
            break
        elif black_queen(black_position[0], black_position[1]):
            break
        else:
            matrix[black_position[0]][black_position[1]] = '-'
            black_position = [black_position[0] + 1, black_position[1]]
            matrix[black_position[0]][black_position[1]] = 'b'

    turn += 1
