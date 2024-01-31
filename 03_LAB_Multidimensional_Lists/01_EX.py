row, col = input().split(', ')

total_sum = 0
matrix = []

for i in range(int(row)):
    sub_list = []
    for j in input().split(', '):
        total_sum += int(j)
        sub_list.append(int(j))
    matrix.append(sub_list)

print(total_sum)
print(matrix)