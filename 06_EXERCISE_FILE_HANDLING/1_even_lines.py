with open("text_files/text.txt", "r") as working_file:
    text = working_file.readlines()

symbols = ("-", ",", ".", "!", "?")

for row in range(0, len(text), 2):

    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")

    print(text[row][::-1])

# with open("text_files/text.txt", "r") as working_file:
#     for row, line in enumerate(working_file.readlines()):
#         if row % 2 == 0:
#             for ch in "-,.!?":
#                 line = line.replace(ch, "@")
#             print(" ".join(reversed(line.split())))
