def calculate_numbers(list_with_nums, idx=0):
    if idx == len(list_with_nums) - 1:
        return list_with_nums[idx]

    return list_with_nums[idx] + calculate_numbers(list_with_nums, idx + 1)


numbers = [int(x) for x in input().split()]
print(calculate_numbers(numbers))
