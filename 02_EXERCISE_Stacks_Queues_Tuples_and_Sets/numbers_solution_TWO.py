first_sequence = set(x for x in input().split())
second_sequence = set(y for y in input().split())

number_of_lines = int(input())

for _ in range(number_of_lines):
    command, info, *data = input().split()

    if command == 'Add' and info == 'First':
        [first_sequence.add(element) for element in data]

    elif command == 'Add' and info == 'Second':
        [second_sequence.add(element) for element in data]

    elif command == 'Remove' and info == 'First':
        [first_sequence.discard(element) for element in data]

    elif command == 'Remove' and info == 'Second':
        [second_sequence.discard(element) for element in data]

    elif command == 'Check' and info == 'Subset':
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))


new_first_set = set(int(x) for x in first_sequence)
print(*sorted(new_first_set), sep=', ')
new_second_set = set(int(y) for y in second_sequence)
print(*sorted(new_second_set), sep=', ')
