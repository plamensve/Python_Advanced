rows, cols = [int(i) for i in input().split(' ')]

matrix = []

for y in range(rows):
    sub_matrix = []
    for j in input().split(' '):
        sub_matrix.append(j)
    matrix.append(sub_matrix)

command = input()
while command != 'END':
    current_command = command.split(' ')
    try:
        action, row1, col1, row2, col2 = current_command[0], int(current_command[1]), int(current_command[2]), int(
            current_command[3]), int(current_command[4])

        if int(row1) < rows and int(row2) < rows and int(col1) < cols and int(col2) < cols:
            firs_element = matrix[row1][col1]
            second_element = matrix[row2][col2]
            matrix[row2][col2] = firs_element
            matrix[row1][col1] = second_element
            for element in matrix:
                print(*element)
        else:
            print(f"Invalid input!")
    except:
        print('Invalid input!')

    command = input()
