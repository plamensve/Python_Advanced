from collections import deque


def check_worm_fit(worm, hole):
    if worm == hole:
        return str('1')
    else:
        if worm - 3 > 0:
            worms.append(worm - 3)
            return str('0')
        else:
            return str('0')


def all_worms_fit():
    if worms_length == matches:
        return True


worms = deque([int(i) for i in input().split()])
holes = deque([int(j) for j in input().split()])
matches = 0
worms_length = len(worms)

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()
    match = check_worm_fit(current_worm, current_hole)
    matches += int(match)


if matches > 0:
    print(f"Matches: {matches}")
else:
    print(f"There are no matches.")


if worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")
else:
    check_fit = all_worms_fit()
    if check_fit:
        print(f"Every worm found a suitable hole!")
    else:
        print(f"Worms left: none")

if holes:
    print(f"Holes left: {', '.join(str(y) for y in holes)}")
else:
    print(f"Holes left: none")