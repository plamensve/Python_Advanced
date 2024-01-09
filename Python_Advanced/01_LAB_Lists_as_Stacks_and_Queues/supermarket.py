command_line = input()
names = []

while command_line != 'End':
    if command_line == 'Paid':
        for name in names:
            print(name)
        names = []
    else:
        names.append(command_line)

    command_line = input()

print(f"{len(names)} people remaining.")