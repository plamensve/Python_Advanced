# print(f"Challenges: {', '.join(str(y) for y in challenges)}")

"""
Принтираме от deque и разпакетираме лист -> задача temple_of_doom - 17 June 2023
"""
# -------------------------------------------------------------------------------#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }

"""
Мапинг за движение по матрици
"""
# -----------------------------#
"""
Внимателно проверявай изискванията какво трябва да се принтира!
"""

# --------------------------------- ЗАДАЧИ 2 с МАТРИЦИ#
"""
Откриване на координатите (индексите) в матрица
"""
SIZE = 6
matrix = []
for row in range(SIZE):
    sub_matrix = []
    for col in input().split():
        sub_matrix.append(col)
        if 'E' in sub_matrix:
            position = [row, sub_matrix.index('E')]
    matrix.append(sub_matrix)

# ---------------------------------------------#

"""
Може да се появят проблеми ако се опитвам да закръглям с rounde(). По-доброто решение е, при принтирането на данните
да се закръгли с :.2f и т.н.
"""

"""
Когато излизаме от матрицата и влизаме през срещуположната страна - телепортиране :D
"""


def check_index(next_r, next_c):
    if 0 <= next_r < SIZE and 0 <= next_c < SIZE:
        return next_r, next_c

    elif 0 > next_r and 0 <= next_c < SIZE:
        return next_r + SIZE, next_c
    elif 0 <= next_r == SIZE:
        return next_r - SIZE, next_c

    elif 0 <= next_r < SIZE and 0 > next_c:
        return next_r, next_c + SIZE
    elif 0 <= next_r < SIZE and next_c == SIZE:
        return next_r, next_c - SIZE

# ----------------------------------------------------- #
