# def factorial_num(number, start_num):   # -> Започваме да умножаваме 1 * 2 * 3 * 4 * 5
#     if start_num == number:
#         return start_num
#
#     return start_num * factorial_num(number, start_num + 1)
#
#
# num = int(input())
# print(factorial_num(num, 1))

# ---------------------- SECOND SOLUTION ----------------- #

def factorial_num(number):   # -> Започваме да умножаваме 5 * 4 * 3 * 2 * 1
    if number == 0:
        return 1
    result = number * factorial_num(number - 1)
    return result


num = int(input())
print(factorial_num(num))
