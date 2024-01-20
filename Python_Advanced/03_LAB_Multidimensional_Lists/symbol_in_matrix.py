rows_and_cols = int(input())

matrix = []

for i in range(rows_and_cols):
    data = [el for el in input()]
    matrix.append(data)

searched_element = input()

flag = False
for j in range(rows_and_cols):
    for y in range(rows_and_cols):
        if matrix[j][y] == searched_element:
            print(f"({j}, {y})")
            flag = True
            exit()

if not flag:
    print(f"{searched_element} does not occur in the matrix")