from collections import deque

programmers = deque(map(int, input().split()))
tasks = list(map(int, input().split()))
givenDucks = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while programmers and tasks:
    current_programmer = programmers.popleft()
    current_task = tasks.pop()
    time_taken = current_programmer * current_task

    if 0 < time_taken <= 60:
        givenDucks["Darth Vader Ducky"] += 1
    elif 60 < time_taken <= 120:
        givenDucks["Thor Ducky"] += 1
    elif 120 < time_taken <= 180:
        givenDucks["Big Blue Rubber Ducky"] += 1
    elif 180 < time_taken <= 240:
        givenDucks["Small Yellow Rubber Ducky"] += 1
    else:
        programmers.append(current_programmer)
        tasks.append(current_task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")
for key, value in givenDucks.items():
    print(key + ": " + str(value))