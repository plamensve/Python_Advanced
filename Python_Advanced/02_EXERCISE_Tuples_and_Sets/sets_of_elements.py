length_ot_sets = [int(num) for num in input().split(' ')]
first_set = set()
second_set = set()

for num in range(length_ot_sets[0]):
    current_number = int(input())
    first_set.add(current_number)

for num in range(length_ot_sets[1]):
    current_number = int(input())
    second_set.add(current_number)

intersection = first_set.intersection(second_set)
for num in intersection:
    print(num)