from collections import deque

time_for_single_task = deque([int(t) for t in input().split()])     # first
task_needed_time = deque([int(h) for h in input().split()])     # last

rubber_ducky_type = {
    'Darth Vader Ducky': 0,             # Between 0-60
    'Thor Ducky': 0,                    # Between 61-120
    'Big Blue Rubber Ducky': 0,         # Between 121-180
    'Small Yellow Rubber Ducky': 0,     # Between 181-240
}

while time_for_single_task and task_needed_time:

    current_single_task = time_for_single_task.popleft()
    current_needed_time = task_needed_time.pop()

    result = current_single_task * current_needed_time

    if 0 <= result <= 60:
        rubber_ducky_type['Darth Vader Ducky'] += 1
    elif 61 <= result <= 120:
        rubber_ducky_type['Thor Ducky'] += 1
    elif 121 <= result <= 180:
        rubber_ducky_type['Big Blue Rubber Ducky'] += 1
    elif 181 <= result <= 240:
        rubber_ducky_type['Small Yellow Rubber Ducky'] += 1
    elif 240 < result:
        decrease = current_needed_time - 2
        task_needed_time.append(decrease)
        time_for_single_task.append(current_single_task)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in rubber_ducky_type.items():
    print(f"{key}: {value}")