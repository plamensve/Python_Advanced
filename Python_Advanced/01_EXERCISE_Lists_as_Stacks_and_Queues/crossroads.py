from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
cars_passed = 0
car_accident = False

green = green_light_duration
free_window = free_window_duration
while True:
    command = input()

    if command == 'END':
        break

    if command != 'green':
        cars.append(command)
        green = green_light_duration
        free_window = free_window_duration
    else:
        for car in cars.copy():
            if green > 0 and len(car) <= green:
                green -= len(car)
                cars.popleft()
                cars_passed += 1

            elif 0 < green <= len(car):
                needed_time = green + free_window
                if needed_time < len(car):
                    index_of_hit = needed_time - len(car)
                    car_name = str(car)
                    hit_char = car_name[index_of_hit]
                    car_accident = True
                    print(f"A crash happened!\n{car} was hit at {hit_char}.")
                    break
                else:
                    green = 0
                    free_window = 0
                    cars.popleft()
                    cars_passed += 1
            else:
                break
if not car_accident:
    print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")