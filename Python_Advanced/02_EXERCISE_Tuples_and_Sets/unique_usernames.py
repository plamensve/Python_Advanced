number_of_usernames = int(input())

user_names = set()

for _ in range(number_of_usernames):
    current_username = input()
    user_names.add(current_username)

for user in user_names:
    print(user)