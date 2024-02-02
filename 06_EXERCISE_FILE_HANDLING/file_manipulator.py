import os
command = input()

while command != 'End':
    current_command = command.split('-')
    action, *info = current_command

    if action == 'Create':
        path = os.path.join('..', 'test', info[0])
        with open(path, 'w'): pass

    elif action == 'Add':
        path = os.path.join('..', 'test', info[0])
        with open(path, 'a') as file:
            file.write(f"{info[1]}\n")

    elif action == "Replace":
        path = os.path.join('..', 'test', info[0])
        try:
            with open(path, "r+") as file:
                text = file.read()
                text = text.replace(info[1], info[2])
                file.seek(0)
                file.write(text)
                file.truncate()
        except FileNotFoundError:
            print(f"An error occurred!")

    elif action == "Delet":
        path = os.path.join('..', 'test', info[0])
        try:
            os.remove(path)
        except FileNotFoundError:
            print(f"An error occurred!")

    command = input()
