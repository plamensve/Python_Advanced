coins = [int(c) for c in input().split(', ')]
target_sum = int(input())
my_dict = {}
sorted_target = sorted(coins, reverse=True)

while sorted_target:
    idx = 0

    coin = sorted_target[idx]
    result_a = target_sum // sorted_target[idx]

    if result_a > 0:
        my_dict[sorted_target[idx]] = result_a

    target_sum -= coin * result_a
    sorted_target.pop(idx)

if target_sum != 0:
    print('Error')
else:
    print(f"Number of coins to take: {sum(my_dict.values())}")
    for k, v in my_dict.items():
        print(f"{v} coin(s) with value {k}")
