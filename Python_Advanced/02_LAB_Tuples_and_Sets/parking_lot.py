number_of_commands = int(input())
parking_set = set()

for x in range(number_of_commands):
    command = input().split(', ')
    info, reg_number = command

    if info == 'IN':
        parking_set.add(reg_number)

    elif info == 'OUT':
        if reg_number in parking_set:
            parking_set.remove(reg_number)

if parking_set:
    for car in parking_set:
        print(car)
else:
    print(f'Parking Lot is Empty')