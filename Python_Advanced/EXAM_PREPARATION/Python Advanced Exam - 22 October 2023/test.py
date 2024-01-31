string = input().split()
new_string = []

# Предполагам, че входът винаги ще има поне 4 елемента
for i in range(4):
    new_substring = ""
    for el in string:
        new_substring += el[i]
    new_string.append(new_substring)

print(new_string)