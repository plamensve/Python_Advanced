def accommodate_new_pets(capacity, weight_limit: float, *info):
    accommodated_pets = {}
    result = []

    for pet_info in info:
        pet_type = pet_info[0]
        weight = pet_info[1]
        if capacity <= 0:
            result.append(f"You did not manage to accommodate all pets!")
            break
        if weight > weight_limit:
            continue
        if pet_type in accommodated_pets:
            accommodated_pets[pet_type] += 1
            capacity -= 1
        else:
            accommodated_pets[pet_type] = 1
            capacity -= 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")
    result.append(f"Accommodated pets:")

    [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(accommodated_pets.items())]
    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))











