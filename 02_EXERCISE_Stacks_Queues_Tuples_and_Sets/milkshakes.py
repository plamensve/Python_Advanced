from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(y) for y in input().split(', '))

milk_shakes = 0

while True:
    if milk_shakes == 5:
        break
    elif not chocolates:
        break
    elif not cups_of_milk:
        break

    last_chocolate = chocolates.pop()
    first_cup_of_milk = cups_of_milk.popleft()
    if last_chocolate <= 0 and first_cup_of_milk <= 0:
        continue
    elif last_chocolate <= 0:
        cups_of_milk.appendleft(first_cup_of_milk)
        continue
    elif first_cup_of_milk <= 0:
        chocolates.append(last_chocolate)
        continue

    if first_cup_of_milk == last_chocolate:
        milk_shakes += 1
    else:
        cups_of_milk.append(first_cup_of_milk)
        chocolates.append(last_chocolate - 5)

if milk_shakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")