from collections import deque

armours_que = deque([int(x) for x in input().split(',')])
strikes_stack = [int(x) for x in input().split(',')]

monsters_defeated = 0
while armours_que and strikes_stack:
    current_armour = armours_que.popleft()
    current_strike = strikes_stack.pop()
    if current_strike >= current_armour:
        monsters_defeated += 1
        current_strike -= current_armour
        if strikes_stack:
            strikes_stack[-1] += current_strike
        elif not strikes_stack and current_strike > 0:
            strikes_stack.append(current_strike)
    else:
        current_armour -= current_strike
        armours_que.append(current_armour)

if not armours_que:
    print("All monsters have been killed!")
if not strikes_stack:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_defeated}")

