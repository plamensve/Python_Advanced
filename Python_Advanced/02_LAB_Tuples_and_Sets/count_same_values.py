numbers = tuple([float(element) for element in input().split()])
counter = {}

for el in numbers:
    if el not in counter:
        counter[el] = numbers.count(el)

for k, v in counter.items():
    print(f"{k} - {v} times")