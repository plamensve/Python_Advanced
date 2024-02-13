from collections import deque

worms = deque([int(w) for w in input().split()])   # -> last symbol
holes = deque([int(h) for h in input().split()])   # -> first symbol

matches = 0
worms_length = len(worms)
while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()
    if current_worm > current_hole:
        if current_worm - 3 > 0:
            worms.append(current_worm - 3)
    elif current_worm < current_hole:
        if current_worm - 3 > 0:
            worms.append(current_worm - 3)

    elif current_worm == current_hole:
        matches += 1

if matches > 0:
    print(f"Matches: {matches}")
else:
    print(f"There are no matches.")

if not worms and matches == worms_length:
    print(f"Every worm found a suitable hole!")
elif not worms and matches != worms_length:
    print(f"Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(map(str, worms))}")

if not holes:
    print(f"Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")