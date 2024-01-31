square_matrix_rows = int(input())

matrix = []

for i in range(square_matrix_rows):
    data = [int(el) for el in input().split(' ')]
    matrix.append(data)

total_sum = 0
for row_index in range(square_matrix_rows):
    for col_index in range(square_matrix_rows):
        if row_index == col_index:
            total_sum += matrix[row_index][col_index]

print(total_sum)