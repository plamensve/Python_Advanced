rows = int(input())

matrix = []

for i in range(rows):
    data = [int(el) for el in input().split(', ')]
    matrix.append(data)

flatten = []
for row in matrix:
    for el in row:
        flatten.append(el)
print(flatten)