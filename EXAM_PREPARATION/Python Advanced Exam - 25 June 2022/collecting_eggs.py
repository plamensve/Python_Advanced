from collections import deque

egg_size = deque([int(e) for e in input().split(', ')])
paper_size = deque([int(p) for p in input().split(', ')])

box_count = 0
box_size = 0

while egg_size and paper_size:
    first_egg = egg_size.popleft()
    last_paper = paper_size.pop()
    sum_of_egg_and_paper = first_egg + last_paper

    if first_egg == 13:
        first_paper = paper_size.popleft()
        paper_size.appendleft(last_paper)
        paper_size.append(first_paper)

    elif first_egg <= 0:
        paper_size.append(last_paper)

    elif sum_of_egg_and_paper <= 50:
        box_count += 1
    else:
        continue

if box_count > 0:
    print(f"Great! You filled {box_count} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if paper_size:
    print(f"Pieces of paper left:",', '.join(map(str, paper_size)))
if egg_size:
    print(f"Eggs left:",', '.join(map(str, egg_size)))
