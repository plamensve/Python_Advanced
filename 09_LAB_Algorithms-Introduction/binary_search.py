def binary_search(nums: list, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = nums[mid_idx]

        if mid_el == target:
            return mid_idx
        elif mid_el > target:
            right = mid_idx - 1
        elif mid_el < target:
            left = mid_idx + 1

    return -1


nums = [int(n) for n in input().split()]
target = int(input())
print(binary_search(nums, target))
