rows, cols = [int(i) for i in input().split(' ')]

matrix = []

for row in range(rows):
    sub_matrix = []
    for col in input().split(' '):
        sub_matrix.append(col)
    matrix.append(sub_matrix)

counter = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        first_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        under_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        if first_element == next_element == under_element == diagonal_element:
            counter += 1

print(counter)
