rows, cols = [int(i) for i in input().split(' ')]

matrix = [[int(el) for el in input().split(' ')] for _ in range(rows)]

total_sum = float('-inf')
sub_matrix = []

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        a_0_0 = matrix[row_index][col_index]
        a_1_0 = matrix[row_index + 1][col_index]
        a_2_0 = matrix[row_index + 2][col_index]

        b_0_1 = matrix[row_index][col_index + 1]
        b_1_1 = matrix[row_index + 1][col_index + 1]
        b_2_1 = matrix[row_index + 2][col_index + 1]

        c_0_2 = matrix[row_index][col_index + 2]
        c_1_2 = matrix[row_index + 1][col_index + 2]
        c_2_2 = matrix[row_index + 2][col_index + 2]

        result = a_0_0 + a_1_0 + a_2_0 + b_0_1 + b_1_1 + b_2_1 + c_0_2 + c_1_2 + c_2_2

        if result > total_sum:
            total_sum = result
            sub_matrix = [[a_0_0, b_0_1, c_0_2], [a_1_0, b_1_1, c_1_2], [a_2_0, b_2_1, c_2_2]]

print(f"Sum = {total_sum}")
for el in sub_matrix:
    print(*el)
