rows, cols = [int(el) for el in input().split(', ')]


def valid_index(col, row):
    if row < rows and col < cols:
        return True


matrix = []

for i in range(rows):
    sub_list = []
    for j in input().split(', '):
        sub_list.append(int(j))
    matrix.append(sub_list)

max_sum = 0
mini_matrix_a = []
mini_matrix_b = []

for y in range(rows):
    for x in range(cols):
        indexes_is_valid = valid_index(x + 1, y + 1)

        if indexes_is_valid:
            first_element = matrix[y][x]
            second_element = matrix[y][x + 1]
            third_element = matrix[y + 1][x]
            forth_element = matrix[y + 1][x + 1]

            result = first_element + second_element + third_element + forth_element

            if result > max_sum:
                max_sum = result
                mini_matrix_a = [first_element, second_element]
                mini_matrix_b = [third_element, forth_element]

print(*mini_matrix_a)
print(*mini_matrix_b)
print(max_sum)
