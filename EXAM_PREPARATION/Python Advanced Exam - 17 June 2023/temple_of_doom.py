from collections import deque

tools = deque([int(t) for t in input().split()])
substance = deque([int(s) for s in input().split()])
challenges = deque([int(c) for c in input().split()])

while tools and substance:
    current_tool = tools.popleft()
    current_substance = substance.pop()
    result = current_tool * current_substance
    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substance.append(current_substance)

if not challenges:
    print(f"Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print(f"Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(y) for y in tools)}")

if substance:
    print(f"Substances: {', '.join(str(y) for y in substance)}")

if challenges:
    print(f"Challenges: {', '.join(str(y) for y in challenges)}")