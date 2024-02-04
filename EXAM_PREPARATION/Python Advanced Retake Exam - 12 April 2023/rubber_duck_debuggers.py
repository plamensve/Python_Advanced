from collections import deque


def the_range(number: int):
    for k, v in duck_type.items():
        if v[0] <= number <= v[1]:
            v[2] += 1
            return True
    tasks_number.append(current_task - 2)
    needed_time.append(current_time)


needed_time = deque([int(t) for t in input().split()])
tasks_number = deque([int(n) for n in input().split()])

duck_type = {
    'Darth Vader Ducky': [0, 60, 0],  # -> range 0-60, 0 - counter of ducks
    'Thor Ducky': [61, 120, 0],
    'Big Blue Rubber Ducky': [121, 180, 0],
    'Small Yellow Rubber Ducky': [181, 240, 0]
}

while needed_time and tasks_number:
    current_time = needed_time.popleft()
    current_task = tasks_number.pop()
    result = current_time * current_task
    the_range(result)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded: ")
for k, v in duck_type.items():
    print(f"{k}: {v[2]}")