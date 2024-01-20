row, col = [int(el) for el in input().split(', ')]

matrix = []

for i in range(row):
    sub_list = []
    for j in (input().split(' ')):
        sub_list.append(j)
    matrix.append(sub_list)

for col_index in range(col):
    col_total = 0
    for row_index in range(row):
        col_total += int(matrix[row_index][col_index])

    print(col_total)



# [
# ['7 1 3 3 2 1']
# ['1 3 9 8 5 6']
# ['4 6 7 9 1 0']
# ]
