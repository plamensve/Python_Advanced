from collections import deque

energy = deque([int(e) for e in input().split()])  # -> first element
box = deque([int(b) for b in input().split()])  # -> last element

spent_energy = 0
turn = 1
toys = 0
while box and energy:
    current_energy = energy.popleft()
    current_box = box.pop()
    if current_energy < 5:
        box.append(current_box)
        continue

    if turn % 3 == 0:
        needed_energy = current_box * 2
        if current_energy >= needed_energy:
            diff = current_energy - needed_energy
            energy.append(diff + 1)
            toys += 2
            spent_energy += needed_energy
        else:
            energy.append(current_energy * 2)
            box.append(current_box)

    if turn % 5 == 0:
        if current_energy >= current_box:
            diff = current_energy - current_box
            spent_energy += current_box
            energy.append(diff)
        else:
            energy.append(current_energy * 2)
            box.append(current_box)

    if turn % 3 != 0 and turn % 5 != 0:
        if current_energy >= current_box:
            diff = current_energy - current_box
            energy.append(diff + 1)
            toys += 1
            spent_energy += current_box
        else:
            box.append(current_box)
            energy.append(current_energy * 2)

    turn += 1

print(f"Toys: {toys}")
print(f"Energy: {spent_energy}")
if energy:
    print(f"Elves left: {', '.join(map(str, energy))}")
if box:
    print(f"Boxes left: {', '.join(map(str, box))}")
