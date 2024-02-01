from collections import deque

monsters_armor = deque([int(arm) for arm in input().split(',')])
soldier_dmg = deque([int(dmg) for dmg in input().split(',')])
killed_monsters = 0

while monsters_armor and soldier_dmg:
    current_monster = monsters_armor.popleft()
    current_soldier = soldier_dmg.pop()

    if current_soldier >= current_monster:
        diff = current_soldier - current_monster
        killed_monsters += 1
        if soldier_dmg:
            soldier_dmg[-1] += diff
        elif not soldier_dmg and diff > 0:
            soldier_dmg.append(diff)
    else:
        monster_decrease_armor = current_monster - current_soldier
        monsters_armor.append(current_monster - monster_decrease_armor)


if not monsters_armor:
    print(f"All monsters have been killed!")
if not soldier_dmg:
    print(f"The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
