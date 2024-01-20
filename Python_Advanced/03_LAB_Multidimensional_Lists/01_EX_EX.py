row, col = [int(x) for x in input().split(', ')]
total_sum = 0

matrix = []

for i in range(row):
    sub_list = []
    for j in input().split(', '):
        sub_list.append(int(j))
        total_sum += int(j)
    matrix.append(sub_list)

print(total_sum)
print(matrix)