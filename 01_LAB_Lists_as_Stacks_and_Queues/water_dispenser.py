from collections import deque
starting_quantity = int(input())
people_on_queue = deque()

names = input()
while names != 'Start':
    people_on_queue.append(names)

    names = input()

command = input()
while command != 'End':
    if command.isdigit():
        person_name = people_on_queue.popleft()
        if starting_quantity >= int(command):
            starting_quantity -= int(command)
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    else:
        current_command = command.split(' ')
        refill, quantity = current_command[0], current_command[1]
        starting_quantity += int(quantity)

    command = input()

print(f"{starting_quantity} liters left")