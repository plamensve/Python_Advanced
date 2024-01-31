number_of_lines = int(input())
set_of_elements = set()

for x in range(number_of_lines):
    current_line = input().split(' ')
    for element in current_line:
        set_of_elements.add(element)

for element in set_of_elements:
    print(element)