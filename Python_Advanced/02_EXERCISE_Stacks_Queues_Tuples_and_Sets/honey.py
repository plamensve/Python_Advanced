from collections import deque

bees = deque(x for x in input().split())
nectar = [y for y in input().split()]
symbols = deque(input().split())
honey = 0

while True:
    if not bees:
        break
    elif not nectar:
        break
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if int(current_bee) > int(current_nectar):
        bees.appendleft(current_bee)
    else:
        current_symbol = symbols.popleft()

        if current_symbol == '+':
            plus = int(current_bee) + int(current_nectar)
            honey += plus

        elif current_symbol == '-':
            minus = abs(int(current_bee) - int(current_nectar))
            honey += minus

        elif current_symbol == '*':
            multiply = int(current_bee) * int(current_nectar)
            honey += multiply

        elif current_symbol == '/':
            if bees != 0 and nectar != 0:
                divide = int(current_bee) / int(current_nectar)
                honey += divide

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

# --------------------------------------SECOND SOLUTION----------------------------- 100 POINTS

# from collections import deque
#
# bees = deque(int(x) for x in input().split())
# nectar = [int(x) for x in input().split()]
# symbols = deque(input().split())
#
# total_honey = 0
#
# functions = {
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b if b != 0 else 0,
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
# }
#
# while bees and nectar:
#     curr_bee = bees.popleft()
#     curr_nectar = nectar.pop()
#
#     if curr_nectar < curr_bee:
#         bees.appendleft(curr_bee)
#     else:
#         total_honey += abs(functions[symbols.popleft()](curr_bee, curr_nectar))
#
# print(f"Total honey made: {total_honey}")
#
# if bees:
#     print(f"Bees left: {', '.join(str(x) for x in bees)}")
#
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
