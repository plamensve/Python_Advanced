def set_cover(universe, sets):
    chosen_set = []
    while universe:
        best_set = max(sets, key=lambda s: len(universe.intersection(s)))
        chosen_set.append(best_set)
        universe -= best_set

    return chosen_set


universe = {int(el) for el in input().split(', ')}
number_of_sets = int(input())
sets = [{int(s) for s in input().split(', ')} for _ in range(number_of_sets)]

result = set_cover(universe, sets)

print(f"Sets to take ({len(result)}):")
for s in result:
    print('{ ' + f"{', '.join(str(x) for x in sorted(s))}" + ' }')
