from collections import deque

altitude = 0
fuel = deque(int(fuel) for fuel in input().split())
consumption_indexes = deque(int(idx) for idx in input().split())
quantities = deque(int(qty) for qty in input().split())
flag = False

while fuel and consumption_indexes and quantities:
    current_fuel = fuel[-1]
    current_c_idx = consumption_indexes[0]
    needed_altitude = quantities[0]
    difference = current_fuel - current_c_idx

    if needed_altitude <= difference:
        current_fuel = fuel.pop()
        current_c_idx = consumption_indexes.popleft()
        needed_altitude = quantities.popleft()
        altitude += 1
        print(f"John has reached: Altitude {altitude}")
        flag = True
    else:
        print(f"John did not reach: Altitude {altitude + 1}")
        print(f"John failed to reach the top.")
        flag = False

        reached_alts = []
        for alt in range(1, altitude + 1):
            reached_alts.append(f'Altitude {alt}')

        if reached_alts:
            print("Reached altitudes:", ', '.join(reached_alts))
            break
        else:
            print(f"John failed to reach the top. John didn't reach any altitude.")
            break

if flag:
    print(f"John has reached all the altitudes and managed to reach the top!")
