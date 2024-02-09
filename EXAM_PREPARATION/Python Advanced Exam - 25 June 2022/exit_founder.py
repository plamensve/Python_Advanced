from collections import deque

names = deque([name for name in input().split(', ')])
row_and_col_size = 6

matrix = []
for row in range(row_and_col_size):
    sub_matrix = []
    for col in input().split():
        sub_matrix.append(col)
    matrix.append(sub_matrix)

rest = {
    'Tom': False,
    'Jerry': False,
}
while True:
    position = input()
    current_player = names.popleft()
    current_position = matrix[int(position[1])][int(position[4])]

    if rest[current_player]:
        rest[current_player] = False
        names.append(current_player)
        continue

    if current_position == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif current_position == 'T':
        print(f"{current_player} is out of the game! The winner is {''.join(names)}.")
        break

    elif current_position == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        rest[current_player] = True
        names.append(current_player)

    elif current_position == '.':
        names.append(current_player)
