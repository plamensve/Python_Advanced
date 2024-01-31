board_size = int(input())
matrix = [[i for i in input()] for size in range(board_size)]

positions = [1, 2, -1, -2]
knight_position = [(row, col) for col in positions for row in positions if abs(row) != abs(col)]


knight_for_remove = 0
while True:
    knight_with_most_attacks = []
    max_attacks = 0
    for r in range(board_size):
        for c in range(board_size):
            if matrix[r][c] == 'K':
                attacks = 0

                for pos in knight_position:
                    attack_r = r + pos[0]
                    attack_c = c + pos[1]

                    if 0 <= attack_r < board_size and 0 <= attack_c < board_size:
                        if matrix[attack_r][attack_c] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks = [r, c]

    if knight_with_most_attacks:
        matrix[knight_with_most_attacks[0]][knight_with_most_attacks[1]] = "0"
        knight_for_remove += 1
    else:
        break

print(knight_for_remove)