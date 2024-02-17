from collections import deque

money = deque([int(m) for m in input().split()])  # last
price = deque([int(p) for p in input().split()])  # first
food = 0
while money and price:

    current_money = money.pop()
    current_price = price.popleft()

    if current_money == current_price:
        food += 1
    elif current_money > current_price:
        diff = current_money - current_price
        food += 1
        if money:
            money[-1] += diff
        else:
            money.append(diff)
    elif current_money < current_price:
        pass

if food >= 4:
    print(f"Gluttony of the day! Henry ate {food} foods.")

if 1 < food < 4:
    print(f"Henry ate: {food} foods.")

if food == 1:
    print(f"Henry ate: {food} food.")

if food <= 0:
    print(f"Henry remained hungry. He will try next weekend again.")