row = int(input())
col = row

matrix = []

for i in range(row):
    sub_list = []
    for j in input().split():
        sub_list.append(int(j))
    matrix.append(sub_list)

index = 0
total_sum = 0
for x in range(len(matrix)):
    if x == index:
        total_sum += matrix[x][index]
        index += 1
print(total_sum)