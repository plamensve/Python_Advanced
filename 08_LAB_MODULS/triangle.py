def triangle(number):

    for x in range(1, number + 1):
        for y in range(1, x + 1):
            print(y, end=' ')
        print()

    for j in range(number, 1, -1):
        for l in range(1, j):
            print(l, end=' ')
        print()