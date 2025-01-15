# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climb_stairs(n):
    return _climb_stair(n, 0)


def _climb_stair(n, i, memo={}):
    if i in memo:
        return memo[i]
    # base case
    if i == n:
        return 1

    if i > n:
        return 0

    memo[i] = _climb_stair(n, i + 1, memo) + _climb_stair(n, i + 2, memo)
    return memo[i]


print(climb_stairs(3))


# Tabulation
def climb_stairs_tabulation(n):
    # just check the last n-1 and n-2 steps and add those in dp array
    dp = [0] * (n + 1)

    # base cases
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
    return dp[n]


print(climb_stairs_tabulation(3))
