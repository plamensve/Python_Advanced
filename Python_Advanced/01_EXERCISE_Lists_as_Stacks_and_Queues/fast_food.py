from collections import deque

quantity_of_food = int(input())

orders = deque([int(x) for x in input().split()])
biggest_order = max(orders)

print(biggest_order)
for order in orders.copy():
    if quantity_of_food >= order:
        quantity_of_food -= order
        orders.popleft()
        if not orders:
            print(f"Orders complete")
    else:
        print(f"Orders left: {' '.join(map(str, orders))}")
        break
