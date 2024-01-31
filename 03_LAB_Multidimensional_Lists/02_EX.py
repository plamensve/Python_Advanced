rows = int(input())

matrix = []
for i in range(rows):
    data = [int(j) for j in input().split(', ') if int(j) % 2 == 0]
    matrix.append(data)
print(matrix)