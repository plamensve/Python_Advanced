from collections import deque

# Initialize altitude names
altitude_names = deque(["Altitude 1", "Altitude 2", "Altitude 3", "Altitude 4"])

# Read input sequences
fuel = list(map(int, input().split()))
consumption_index = deque(map(int, input().split()))
needed_fuel_amount = deque(map(int, input().split()))

# Initialize altitudes with values
altitudes_with_values = {}
for key in altitude_names:
    if needed_fuel_amount:
        value = needed_fuel_amount.popleft()
        altitudes_with_values[key] = value

# Initialize reached altitudes
reached_altitudes = []

# Main loop
while fuel and consumption_index and altitudes_with_values:
    current_level = altitude_names[0]
    current_fuel = fuel[-1]
    additional_consumption = consumption_index[0]
    difference = current_fuel - additional_consumption

    if difference >= altitudes_with_values[current_level]:
        fuel.pop()
        consumption_index.popleft()
        reached_altitudes.append(current_level)
        del altitudes_with_values[current_level]
        altitude_names.popleft()
        print(f"John has reached: {current_level}")
    else:
        fuel.pop()
        consumption_index.popleft()
        altitude_names.popleft()
        print(f"John did not reach: {current_level}")
        break

# Output results
if not altitudes_with_values:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    if reached_altitudes:
        print("Reached altitudes: ", end="")
        print(", ".join(reached_altitudes))
    else:
        print("John didn't reach any altitude.")
