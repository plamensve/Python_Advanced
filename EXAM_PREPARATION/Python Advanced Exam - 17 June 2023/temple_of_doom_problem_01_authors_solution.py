from collections import deque

tools_que = deque([int(t) for t in input().split()])
substances_stack = [int(s) for s in input().split()]
challenges = [int(c) for c in input().split()]

while challenges and substances_stack:
    current_tool = tools_que.popleft()
    current_substance = substances_stack[-1]
    current_product = current_tool * current_substance
    if current_product in challenges:
        challenges.remove(current_product)
        substances_stack.pop()
        continue
    current_tool += 1
    tools_que.append(current_tool)
    substances_stack[-1] -= 1
    if substances_stack[-1] == 0:
        substances_stack.pop()

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools_que:
    print(f"Tools: {', '.join([str(t) for t in tools_que])}")
if substances_stack:
    print(f"Substances: {', '.join([str(s) for s in substances_stack])}")
if challenges:
    print(f"Challenges: {', '.join([str(c) for c in challenges])}")


