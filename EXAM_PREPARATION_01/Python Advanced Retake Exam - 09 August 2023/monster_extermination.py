from collections import deque

armor = deque([int(a) for a in input().split(',')])     # first symbol
dmg = deque([int(d) for d in input().split(',')])       # last symbol
killed_monsters = 0

while armor and dmg:

    current_armor = armor.popleft()
    current_dmg = dmg.pop()

    diff = current_dmg - current_armor

    if current_dmg >= current_armor:
        killed_monsters += 1
        if dmg:
            dmg[-1] += diff
        elif not dmg and diff > 0:
            dmg.append(diff)

    elif current_dmg < current_armor:
        armor.append(current_armor - current_dmg)

if not armor:
    print(f"All monsters have been killed!")
if not dmg:
    print(f"The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
