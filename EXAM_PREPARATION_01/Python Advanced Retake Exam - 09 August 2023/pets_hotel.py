def accommodate_new_pets(cap, weight_limit, *pet_info):
    accommodated = {}
    capacity = cap
    are_accommodated = True

    for pet, weight in pet_info:
        if not capacity:
            are_accommodated = False
            break
        if weight <= weight_limit:
            if pet not in accommodated:
                accommodated[pet] = 0
            accommodated[pet] += 1
            capacity -= 1

    final_msg = ''
    if are_accommodated:
        final_msg += f"All pets are accommodated! Available capacity: {capacity}.\n"
    else:
        final_msg += f"You did not manage to accommodate all pets!\n"

    final_msg += f"Accommodated pets:\n"
    if accommodated:
        for k, v in sorted(accommodated.items(), key=lambda s: s[0]):
            final_msg += f"{k}: {v}\n"

    return final_msg[:-1]


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))


















