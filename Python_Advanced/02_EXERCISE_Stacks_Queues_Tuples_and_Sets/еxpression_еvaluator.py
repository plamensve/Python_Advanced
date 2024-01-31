from collections import deque
from math import floor

expression = deque(input().split())
index = 0

while index < len(expression):
    element = expression[index]
    if element == "-":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif element == "+":
        for _ in range(index - 1):  # -1 -> everything but the symbol
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
    elif element == "/":
        for _ in range(index - 1):  # -1 -> everything but the symbol
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif element == "*":
        for _ in range(index - 1):  # -1 -> everything but the symbol
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))

    if element in "/*+-":
        del expression[1]
        index = 1
    index += 1

print(floor(int(expression[0])))