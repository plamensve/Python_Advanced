def negative_vs_positive(*args):
    negative = 0
    positive = 0
    string_line = ""
    for num in args:
        if num < 0:
            negative += num
        else:
            positive += num

    if abs(negative) > positive:
        string_line += "The negatives are stronger than the positives"
    else:
        string_line += "The positives are stronger than the negatives"
    return f"{negative}\n{positive}\n{string_line}"


numbers = [int(i) for i in input().split()]
print(negative_vs_positive(*numbers))

# SOLUTION 2

# def negative_vs_positive(nums: list):
#     positive = sum(int(i) for i in nums if i > 0)
#     negative = sum(int(i) for i in nums if i < 0)
#
#     print(negative)
#     print(positive)
#
#     if positive > abs(negative):
#         print(f"The positives are stronger than the negatives")
#     else:
#         print(f"The negatives are stronger than the positives")
#
#
# numbers = [int(i) for i in input().split()]
# negative_vs_positive(numbers)
