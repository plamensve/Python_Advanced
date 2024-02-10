def check_deposit_or_rock(current_matrix, rover, current_deposits):
    position = current_matrix[rover[0]][rover[1]]
    if position in ['W', 'M', 'C']:
        print(f"{current_deposits[position][0]} deposit found at ({rover[0]}, {rover[1]})")
        current_deposits[position][1] += 1
    elif position == 'R':
        return 'broken'
    return current_deposits


matrix = []
deposits = {'W': ['Water', 0], 'M': ['Metal', 0], 'C': ['Concrete', 0]}
rover_coordinates = []
is_broken = False

for _ in range(6):
    matrix.append((input().split()))

for row in range(6):
    found_rover = False
    for col in range(6):
        if matrix[row][col] == 'E':
            rover_coordinates = [row, col]
            found_rover = True
            break
    if found_rover:
        break

commands = input().split(", ")
for c in commands:
    if c == 'up':
        if rover_coordinates[0] > 0:
            rover_coordinates[0] -= 1
        else:
            rover_coordinates[0] = 5
    if c == 'down':
        if rover_coordinates[0] < 5:
            rover_coordinates[0] += 1
        else:
            rover_coordinates[0] = 0
    if c == 'left':
        if rover_coordinates[1] > 0:
            rover_coordinates[1] -= 1
        else:
            rover_coordinates[1] = 5
    if c == 'right':
        if rover_coordinates[1] < 5:
            rover_coordinates[1] += 1
        else:
            rover_coordinates[1] = 0
    result_after_checking_the_land = check_deposit_or_rock(matrix, rover_coordinates, deposits)
    if result_after_checking_the_land == 'broken':
        is_broken = True
        break
    deposits = result_after_checking_the_land

if is_broken:
    print(f"Rover got broken at ({rover_coordinates[0]}, {rover_coordinates[1]})")
if deposits['W'][1] >= 1 and deposits['M'][1] >= 1 and deposits['C'][1] >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
