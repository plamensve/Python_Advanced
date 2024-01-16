number_of_lines = int(input())
first_set = set()
second_set = set()
intersection = []

for _ in range(number_of_lines):
    ranges = input().split('-')
    first_list, second_list = ranges[0], ranges[1]
    fist_start, first_end = first_list.split(',')
    second_start, second_end = second_list.split(',')

    for x in range(int(fist_start), int(first_end) + 1):
        first_set.add(x)

    for y in range(int(second_start), int(second_end) + 1):
        second_set.add(y)

    result = first_set.intersection(second_set)
    if len(intersection) < len(result):
        intersection = list(result)
        first_set.clear(), second_set.clear()
    else:
        first_set.clear(), second_set.clear()
        continue

print(f"Longest intersection is {intersection} with length {len(intersection)}")