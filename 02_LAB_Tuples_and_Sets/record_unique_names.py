number_of_names = int(input())
names_in_set = set()

for _ in range(number_of_names):
    current_name = input()
    names_in_set.add(current_name)

for name in names_in_set:
    print(name)
