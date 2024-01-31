class ValueCannotBeNegative(Exception):
    pass


value_number = int(input())
if value_number < 0:
    raise ValueCannotBeNegative
