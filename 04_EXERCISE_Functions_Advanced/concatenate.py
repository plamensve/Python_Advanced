def concatenate(*args, **kwargs):
    first_string = ''
    for el in args:
        first_string += el

    for k, v in kwargs.items():
        first_string = first_string.replace(k, v)
    return first_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))