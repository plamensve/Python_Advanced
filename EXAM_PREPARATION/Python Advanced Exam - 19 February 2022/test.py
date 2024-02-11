size = 8
coordinates = [5, 0]
for r in range(size):
    for c in range(size):
        letter = chr(c + 97)
        number = 8 - r
        if [r, c] == coordinates:
            print(f"{letter}{number}")
