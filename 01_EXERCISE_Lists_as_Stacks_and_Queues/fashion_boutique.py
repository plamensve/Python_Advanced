from collections import deque

clothes_in_the_box = deque([int(x) for x in input().split(' ')])
capacity_of_rack = int(input())
number_of_racks = 1
current_rack = 0

for clothe in clothes_in_the_box.copy():
    pop_clothe = clothes_in_the_box.pop()
    if current_rack + pop_clothe <= capacity_of_rack:
        current_rack += int(pop_clothe)
    else:
        number_of_racks += 1
        current_rack = pop_clothe

print(number_of_racks)
