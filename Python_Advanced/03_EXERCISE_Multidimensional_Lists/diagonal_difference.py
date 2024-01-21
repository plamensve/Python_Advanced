rows = int(input())

matrix = [[int(el) for el in input().split(' ')]for _ in range(rows)]

primary = [matrix[i][i] for i in range(rows)]
secondary = [matrix[j][rows - j - 1] for j in range(rows)]

print(abs(sum(primary) - sum(secondary)))