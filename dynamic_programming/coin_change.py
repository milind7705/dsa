# Write a function, counting_change, that takes in an amount and a list of coins.
# The function should return the number of different ways it is possible
# to make change for the given amount using the coins.
#
# You may reuse a coin as many times as necessary.


# For example,
#
# counting_change(4, [1,2,3]) -> 4
#
# There are four different ways to make an amount of 4:
#
# 1. 1 + 1 + 1 + 1
# 2. 1 + 1 + 2
# 3. 1 + 3
# 4. 2 + 2

# This is not a blind recursion problem. Here we can't use all subtrees as it will cause duplicates
# The below subtree we were thinking is WRONG:
#                   4
#           1/        2|   3\
#          3           2      1
#      1/  2|  3\     1/ \2    1|
#      2     1    0    1   0     0
#    1/ 2\   1|        1|
#    1    0   0         0
#    1|
#    0

# This needs to consider the each coin denominations in the each loop

#                       4
# coin=1         0/    1|     2\     4\
#                4       3      2       0
# coin=2      0/ 1| 2\ 0/ 1\   0/ 1\
#            4    2  0 3    1  2    0
#coin=3    0/ 1\      0/ \1
#          4    1     3    0

def counting_change(amount, coins):

    def _counting_change(amount, coins, i, memo):
        key = (amount, i)
        if key in memo:
            return memo[key]
        # if target_sum matches return 1
        if amount == 0:
            return 1

        if i == len(coins):
            return 0

        coin = coins[i]
        total_ways = 0
        for qty in range(0, (amount//coin) + 1):
            remainder = amount - (qty * coin)
            total_ways += _counting_change(remainder, coins, i + 1, memo)
        memo[key] = total_ways
        return memo[key]

    return _counting_change(amount, coins, 0, {})

print(counting_change(4, [1, 2, 3]))