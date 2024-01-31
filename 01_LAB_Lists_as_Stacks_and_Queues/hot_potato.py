from collections import deque

names = input().split(' ')
toss = int(input())

names_in_queue = deque()
for name in names:
    names_in_queue.append(name)

while len(names_in_queue) > 1:

    for rotation in range(1, toss):
        child = names_in_queue.popleft()
        names_in_queue.append(child)

    burn = names_in_queue.popleft()
    print(f"Removed {burn}")

print(f"Last is {names_in_queue[0]}")