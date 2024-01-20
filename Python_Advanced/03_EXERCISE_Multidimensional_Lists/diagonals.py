rows = int(input())

matrix = [[int(el) for el in input().split(', ')] for i in range(rows)]

primary = [matrix[el][el] for el in range(rows)]
secondary = [matrix[el][rows - el - 1] for el in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(y) for y in secondary)}. Sum: {sum(secondary)}")

