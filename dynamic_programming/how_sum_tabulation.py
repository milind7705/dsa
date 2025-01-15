# how_sum(target, numbers), return a combination if the numbers in the array can generate the target_sum
# how_sum(7, [5, 3, 4, 7])


def how_sum(target_sum, numbers):
    # First set the dp array with target_sum + 1
    dp = [None] * (target_sum + 1)

    # Base case is zero can be made with no combination
    dp[0] = []

    for i in range(target_sum + 1):
        if dp[i] is not None:
            for num in numbers:
                if i + num < target_sum + 1:
                    dp[i + num] = dp[i] + [num]  # additional m is for copying
    # print(dp)
    return dp[target_sum]


print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(300, [7, 14]))

# Time: O(m * n * m)
# Space: O(m^2)
