import os

def create_file():
    with open(file_path, "w"):
        pass

def add_in_file():
    with open(file_path, "a") as f:
        f.write(content + "\n")

def replace_in_file():
    try:
        with open(file_path, "r+") as f:
            file_data = f.read()

            file_data = file_data.replace(old_string, new_string)
            f.seek(0)
            f.write(file_data)    

    except FileNotFoundError:
        print("An error occurred")

def del_file():
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("An error occurred")
        
path_to_root = os.path.dirname(os.path.abspath(__file__))

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    
    name = command[1]
    file_path = os.path.join(path_to_root, name)

    if command[0] == "Create":
        create_file()
    elif command[0] == "Add":
        content = command[2]
        add_in_file()
    elif command[0] == "Replace":
        old_string, new_string = command[2], command[3]
        replace_in_file()
    elif command[0] == "Delete":
        del_file()
