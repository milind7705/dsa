# best_sum(target, numbers), return a combination if the numbers in the array can generate the target_sum
# best_sum(7, [5, 3, 4, 7])


def best_sum(target_sum, numbers):
    dp = [None] * (target_sum + 1)

    dp[0] = []

    for i in range(target_sum + 1):
        if dp[i] is not None:
            for num in numbers:
                if i + num < target_sum + 1:
                    combination = dp[i] + [num]
                    # print(dp[i + num])
                    # this not dp[i + num] is intuitive because it checks for both nulls and empty []
                    if not dp[i + num] or len(combination) < len(dp[i + num]):
                        dp[i + num] = combination
    # print(dp)
    return dp[target_sum]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(100, [5, 3, 4, 25]))
