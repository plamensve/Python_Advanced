def start_spring(**info):
    information = {}
    result = ''
    for k, v in info.items():
        if v not in information:
            information[v] = []
        information[v].append(k)

    sorted_information_by_len_of_value = sorted(information.items(), key=lambda x: (-len(x[1]), x[1]))
    for tuple_ in sorted_information_by_len_of_value:
        object_a = tuple_[0]
        type_of_object = tuple_[1]

        sorted_elements = sorted(type_of_object)
        result += f"{object_a}:\n"
        for el in sorted_elements:
            result += f"-{el}\n"
    result.strip()
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
