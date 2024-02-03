def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row-1, rows):
        return current_row-1, current_col
    if command == 'down' and is_valid(current_row+1, rows):
        return current_row+1, current_col
    if command == 'left' and is_valid(current_col-1, cols):
        return current_row, current_col-1
    if command == 'right' and is_valid(current_col+1, cols):
        return current_row, current_col+1
    return None, None


rows, cols = [int(x) for x in input().split(',')]
field = []
mouse_row, mouse_col = None, None
cheese_cnt = 0
line = ''

for r in range(rows):
    row = list(input())
    field.append(row)
    if 'M' in row:
        mouse_row = r
        mouse_col = row.index('M')
    if 'C' in row:
        cheese_cnt += row.count('C')


while cheese_cnt != 0:
    line = input()
    if line == 'danger':
        break
    next_row, next_col = next_move(line, mouse_row, mouse_col)
    if next_row is None or next_col is None:
        print('No more cheese for tonight!')
        break
    if field[next_row][next_col] == '@':
        continue
    if field[next_row][next_col] == 'T':
        field[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = 'M'
        print("Mouse is trapped!")
        break
    if field[next_row][next_col] == '*':
        field[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = 'M'
        continue
    if field[next_row][next_col] == 'C':
        cheese_cnt -= 1
        field[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = 'M'

else:
    print("Happy mouse! All the cheese is eaten, good night!")

if cheese_cnt and line == 'danger':
    print("Mouse will come back later!")

for row in field:
    print(''.join(row))







