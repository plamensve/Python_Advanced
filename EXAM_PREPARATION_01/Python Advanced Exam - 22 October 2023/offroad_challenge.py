from collections import deque

fuel = deque([int(f) for f in input().split()])  # -> last symbol
consumption = deque([int(c) for c in input().split()])  # -> first symbol
altitude = deque([int(a) for a in input().split()])
reached_altitude = []
altitude_num = 0
fail = False

while fuel and consumption and altitude:
    current_fuel = fuel.pop()
    current_consumption = consumption.popleft()
    diff = current_fuel - current_consumption

    current_altitude = altitude.popleft()

    if diff >= current_altitude:
        altitude_num += 1
        reached_altitude.append(f"Altitude {altitude_num}")
        print(f"John has reached: Altitude {altitude_num}")
    else:
        print(f"John did not reach: Altitude {altitude_num + 1}")
        fail = True
        break

if fail:
    print(f"John failed to reach the top.")
    if reached_altitude:
        print(f"Reached altitudes: {', '.join(reached_altitude)}")
    else:
        print(f"John didn't reach any altitude.")
if not fail and len(reached_altitude) == 4:
    print(f"John has reached all the altitudes and managed to reach the top!")
    exit()

if not fuel and not fail:
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitude)}")
