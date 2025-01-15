# TODO tabulation recipe always comes up with an array
# initialize the array of n+1 elements with zero
# iterate and add previous 2 values to current i
# This works as the problem can be solved like tree structure


# 0  1  2  3  4  5  6 7
# -> add zero to the next ones, but starting from 2
def fib_tabulation(n):

    if n <= 1:
        return n
    dp = [0] * (n + 1)  # n + 1 array position initialization
    # base case
    dp[0] = 0
    dp[1] = 1

    # the catch to avoid array out of bounds error is to iterate from 2 till n+1
    # and use i-X things
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fib_tabulation(6))  # 8
print(fib_tabulation(50))  # 12586269025

# Time: O(n)
# Space: O(n)
