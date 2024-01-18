row, col = (int(el) for el in input().split(', '))
# [
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# ]
total_amount = 0
matrix = []

for i in range(row):
    row_data = [int(el) for el in input().split(', ')]
    total_amount += sum(row_data)
    matrix.append(row_data)

print(total_amount)
print(matrix)

