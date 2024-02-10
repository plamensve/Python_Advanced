from collections import deque

bowls = deque([int(b) for b in input().split(', ')])  # -> last symbol
customers = deque([int(c) for c in input().split(', ')])  # -> first symbol

while True:
    if not bowls or not customers:
        break

    current_bowl = bowls.pop()
    current_customer = customers.popleft()

    if current_bowl == current_customer:
        continue

    elif current_bowl > current_customer:
        diff_b = current_bowl - current_customer
        bowls.append(diff_b)

    elif current_bowl < current_customer:
        diff_c = current_customer - current_bowl
        customers.appendleft(diff_c)

if not customers:
    print(f"Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls))}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")
