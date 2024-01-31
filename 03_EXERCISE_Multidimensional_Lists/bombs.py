def index_is_valid(row, col):
    if rows > row >= 0 and rows > col >= 0:
        return True


rows = int(input())

matrix = [[int(el) for el in input().split()] for i in range(rows)]

indexes = input()

current_index = indexes.split(' ')
for i in current_index:
    coordinate = i.split(',')
    x = int(coordinate[0])
    y = int(coordinate[1])

    if matrix[x][y] > 0:
        a = index_is_valid(x - 1, y)
        if a:
            result_a = matrix[x - 1][y] - matrix[x][y]
            if matrix[x - 1][y] > 0:
                matrix[x - 1][y] = result_a

        b = index_is_valid(x - 1, y + 1)
        if b:
            result_b = matrix[x - 1][y + 1] - matrix[x][y]
            if matrix[x - 1][y + 1] > 0:
                matrix[x - 1][y + 1] = result_b

        c = index_is_valid(x, y + 1)
        if c:
            result_c = matrix[x][y + 1] - matrix[x][y]
            if matrix[x][y + 1] > 0:
                matrix[x][y + 1] = result_c

        d = index_is_valid(x + 1, y + 1)
        if d:
            result_d = matrix[x + 1][y + 1] - matrix[x][y]
            if matrix[x + 1][y + 1] > 0:
                matrix[x + 1][y + 1] = result_d

        e = index_is_valid(x + 1, y)
        if e:
            result_e = matrix[x + 1][y] - matrix[x][y]
            if matrix[x + 1][y] > 0:
                matrix[x + 1][y] = result_e

        f = index_is_valid(x + 1, y - 1)
        if f:
            result_f = matrix[x + 1][y - 1] - matrix[x][y]
            if matrix[x + 1][y - 1] > 0:
                matrix[x + 1][y - 1] = result_f

        g = index_is_valid(x, y - 1)
        if g:
            result_g = matrix[x][y - 1] - matrix[x][y]
            if matrix[x][y - 1] > 0:
                matrix[x][y - 1] = result_g

        h = index_is_valid(x - 1, y - 1)
        if h:
            result_h = matrix[x - 1][y - 1] - matrix[x][y]
            if matrix[x - 1][y - 1] > 0:
                matrix[x - 1][y - 1] = result_h

        matrix[x][y] = 0

alive_cells = 0
total_sum = 0

for i in matrix:
    for el in i:
        if el > 0:
            alive_cells += 1
            total_sum += el

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_sum}")
for el in matrix:
    print(*el)

# ------------------ SECOND SOLUTRION --------------------------------------

# n = int(input())

# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# coordinates = ((int(x) for x in c.split(",")) for c in input().split()) # 1,2  3,4  5,6 => ["1,2", "3,4", "5, 6"] =>
# # ((1, 2), (3, 4), (5, 6))
#
# for row, col in coordinates:
#     if matrix[row][col] <= 0:
#         continue
#
#     bomb_value = matrix[row][col]
#
#     for x in range(-1, 2):  # -1 0 1
#         for y in range(-1, 2):  # -1 0 1
#             r, c = row + x, col + y
#
#             if 0 <= r < n and 0 <= c < n:
#                 matrix[r][c] -= bomb_value if matrix[r][c] > 0 else 0
#
# alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]
#
# print(f"Alive cells: {len(alive_cells)}")
# print(f"Sum: {sum(alive_cells)}")
#
# [print(*row) for row in matrix]
