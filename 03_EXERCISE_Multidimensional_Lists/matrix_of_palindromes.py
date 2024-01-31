rows, cols = [int(rows) for rows in input().split(' ')]

matrix = []

for i in range(rows):
    sub_matrix = [f'{chr(97 + i) * 3}']
    for j in range(cols - 1):
        start_symbol = int(i + 97)
        middle_symbol = start_symbol + 1 + j
        end_symbol = start_symbol
        sub_matrix.append(chr(start_symbol) + chr(middle_symbol) + chr(end_symbol))

    matrix.append(sub_matrix)

for el in matrix:
    print(*el)