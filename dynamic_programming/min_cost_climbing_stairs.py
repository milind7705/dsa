# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.


# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.


# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.


def min_cost_climbing_stairs(cost):
    return min(_min_cost_climbing_stairs(cost, 0), _min_cost_climbing_stairs(cost, 1))


def _min_cost_climbing_stairs(cost, i):
    if i >= len(cost):
        return 0

    return cost[i] + min(
        _min_cost_climbing_stairs(cost, i + 1), _min_cost_climbing_stairs(cost, i + 2)
    )


cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]


print(min_cost_climbing_stairs(cost))


def min_cost_climbing_stairs_tabulation(cost):
    dp = [0] * (len(cost) + 1)

    # base cases as no cost needed to start from 0 and 1
    dp[0] = 0
    dp[1] = 0

    # recurrence relation
    # dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2)]

    for i in range(2, len(cost) + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    # print(dp)
    return dp[len(cost)]


print(min_cost_climbing_stairs_tabulation(cost))
