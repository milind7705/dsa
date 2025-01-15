# can_sum(target, numbers), return true if the numbers in the array can generate the target_sum
# can_sum(7, [5, 3, 4, 7])


def can_sum(target_sum, numbers):
    # TODO tabulate it and store T at 0 because 0 can be taken for no combination can_sum(0, [..]) => True
    # Then add the true to the numbers position
    dp = [False] * (target_sum + 1)
    dp[0] = True

    for i in range(target_sum + 1):
        if dp[i] == True:
            for num in numbers:
                if i + num < target_sum + 1:
                    dp[i + num] = True
    return dp[target_sum]


print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(300, [7, 14]))

# Time: O(m * n)
# Space: O(m)
