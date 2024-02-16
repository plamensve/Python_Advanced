from collections import deque

tools = deque([int(t) for t in input().split()])  # first
substance = deque([int(s) for s in input().split()])  # last
challenges = [int(c) for c in input().split()]

while True:
    if not challenges:
        print(f"Harry found an ostracon, which is dated to the 6th century BCE.")
        if tools:
            for tool in tools:
                print(tool)

        if substance:
            for subs in substance:
                print(f"Substances: {subs}")
        exit()

    if not tools or not substance:
        break

    current_tool = tools.popleft()
    current_substance = substance.pop()
    result = current_tool * current_substance

    for ch in challenges:
        if ch == result:
            challenges.remove(ch)
            break
    else:
        tools.append(current_tool + 1)
        if current_substance - 1 > 0:
            substance.append(current_substance - 1)

print(f"Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")

if substance:
    print(f"Substance: {', '.join(map(str, substance))}")

if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
