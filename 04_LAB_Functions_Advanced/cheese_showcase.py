def sorting_cheeses(**kwargs):
    sorted_element = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), (kvp[1])))
    result = ''
    for cheese, quantities in sorted_element:
        result += cheese + "\n"
        for quantity in sorted(quantities, reverse=True):
            result += str(quantity) + "\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
