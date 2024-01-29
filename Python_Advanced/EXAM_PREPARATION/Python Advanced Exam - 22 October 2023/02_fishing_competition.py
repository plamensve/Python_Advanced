# Find the starting position of the ship ('S') in the fishing area
def find_starting_position(size, fishing_area):
    for i in range(size):
        for j in range(size):
            if fishing_area[i][j] == 'S':
                return [i, j]
    return None


# Move the ship based on the given command
def move(command, position, fishing_area):
    row, col = position
    fishing_area[row][col] = '-'

    if command == "up":
        position[0] -= 1
    elif command == "down":
        position[0] += 1
    elif command == "left":
        position[1] -= 1
    elif command == "right":
        position[1] += 1

    return position


# Handle boundary conditions when the ship moves
def handle_boundaries(position, size):
    for i in range(2):
        if position[i] < 0:
            position[i] = size - 1
        elif position[i] >= size:
            position[i] = 0


# Handle whirlpool event
def handle_whirlpool(position):
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")


# Handle and print the final results
def handle_results(quota, vortex, fishing_area):
    if quota >= 20:
        print("Success! You managed to reach the quota!")
    elif not vortex:
        lack = 20 - quota
        print(f"You didn't catch enough fish and didn't reach the quota! You need {lack} tons of fish more.")

    if quota > 0:
        print(f"Amount of fish caught: {quota} tons.")

    if not vortex:
        for row in fishing_area:
            print("".join(row))


size = int(input())
fishing_area = []

# Read the fishing area configuration
for _ in range(size):
    row = list(input())
    fishing_area.append(row)

current_position = find_starting_position(size, fishing_area)
quota = 0
whirlpool = False

# Process commands until "collect the nets" is entered
while True:
    command = input()

    if command == "collect the nets":
        break

    current_position = move(command, current_position, fishing_area)
    handle_boundaries(current_position, size)

    current_char = fishing_area[current_position[0]][current_position[1]]

    if current_char.isdigit():
        quota += int(current_char)
    elif current_char == 'W':
        handle_whirlpool(current_position)
        whirlpool = True
        quota = 0
        break
    fishing_area[current_position[0]][current_position[1]] = 'S'

# Print the final results
handle_results(quota, whirlpool, fishing_area)
