from collections import deque

caffeine = deque([int(c) for c in input().split(', ')])
energy_drinks = deque([int(ed) for ed in input().split(', ')])
max_caffeine = 0

while caffeine and energy_drinks:
    if max_caffeine > 300:
        break

    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    result = current_caffeine * current_energy_drink

    if result + max_caffeine <= 300:
        max_caffeine += result

    else:
        energy_drinks.append(current_energy_drink)
        if max_caffeine - 30 < 0:
            max_caffeine = 0
        else:
            max_caffeine -= 30

if not energy_drinks:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
    print(f"Stamat is going to sleep with {max_caffeine} mg caffeine.")
else:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
    print(f"Stamat is going to sleep with {max_caffeine} mg caffeine.")