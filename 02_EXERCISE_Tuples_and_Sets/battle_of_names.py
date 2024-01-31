number_of_lines = int(input())
even_set = set()
odd_set = set()

for line in range(1, number_of_lines + 1):
    current_name = input()
    char_name_sum = 0
    for char in current_name:
        result = ord(char)
        char_name_sum += result
    char_name_result = char_name_sum // line
    if char_name_result % 2 == 0:
        even_set.add(char_name_result)
    else:
        odd_set.add(char_name_result)

if sum(even_set) == sum(odd_set):
    print(*odd_set.union(even_set), sep=', ')

elif sum(even_set) > sum(odd_set):
    print(*odd_set.symmetric_difference(even_set), sep=', ')

elif sum(even_set) < sum(odd_set):
    print(*odd_set.difference(even_set), sep=', ')

