string_line = input()

chars_of_string_line = []
new_set = set()

for char in string_line:
    chars_of_string_line.append(char)

for char in tuple(chars_of_string_line):
    new_set.add(char)
for x in sorted(new_set):
    print(f"{x}: {chars_of_string_line.count(x)} time/s")

# ---------------------- 1 solution---------------------
# text = input.txt()
#
# for symbol in sorted(set(text)):
#     print(f"{symbol}: {text.count(symbol)} time/s")

# ---------------------- 2 solution----------------------
# occurrences = {}
#
# for symbol in input.txt():
#     occurrences[symbol] = occurrences.get(symbol, 0) + 1
#
# for symbol, times in sorted(occurrences.items()):  # (("a", 1), ("b", 3))
#     print(f"{symbol}: {times} time/s")
