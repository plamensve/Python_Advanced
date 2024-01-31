row = int(input())

matrix = []

for i in range(row):
    data = [int(el) for el in input().split(', ')]
    matrix.extend(data)

print(matrix)
