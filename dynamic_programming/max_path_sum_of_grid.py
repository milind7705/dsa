# Write a function, max_path_sum, that takes in a grid as an argument.
# The function should return the maximum sum possible by traveling a path
# from the top-left corner to the bottom-right corner.
# You may only travel through the grid by moving down or right.
#
# You can assume that all numbers are non-negative.

# Use recursion, get all path and then find max. In this case, we need to check only for down and right path.


def max_path_sum(grid):
    # Always start with 0, 0
    return _max_path_sum_memo(grid, 0, 0)


def _max_path_sum(grid, r, c):
    # find the base cases
    # if out of bounds return -inf as this problem is for max
    if r == len(grid) or c == len(grid[0]):
        return float("-inf")

    # second base case : if this is last element, return that element
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    # initiate recursion
    down = _max_path_sum(grid, r + 1, c)
    right = _max_path_sum(grid, r, c + 1)
    # add the current edge i.e current value and max of both
    return grid[r][c] + max(down, right)


def _max_path_sum_memo(grid, r, c, memo={}):
    pos = (r, c)
    if pos in memo:
        return memo[pos]
    # find the base cases
    # if out of bounds return -inf as this problem is for max
    if r == len(grid) or c == len(grid[0]):
        return float("-inf")

    # second base case : if this is last element, return that element
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    # initiate recursion
    down = _max_path_sum_memo(grid, r + 1, c, memo)
    right = _max_path_sum_memo(grid, r, c + 1, memo)
    # add the current edge i.e current value and max of both
    memo[pos] = grid[r][c] + max(down, right)
    return memo[pos]


# Time: O(r * c) # Only need to calculate r*c objects
# Space: O(r * c) # number of keys in the memo object

grid = [
    [1, 3, 12],
    [5, 1, 1],
    [3, 6, 1],
]
# print(max_path_sum(grid))


# Tabulation is little simple, we need to store the max at the grid element so calculations will be easier
def max_path_sum_tabulation(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # base case add the grid[0][0] directly to dp table
    dp[0][0] = grid[0][0]

    # then populate the first row
    for i in range(1, cols):
        dp[0][i] = dp[0][i - 1] + grid[0][i]

    # populate first column
    for i in range(1, rows):
        dp[i][0] = dp[0][0] + grid[i - 1][0]

    # Now create calculations for other values, each entity represents the max to get that point
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    return dp[rows - 1][cols - 1]
    # Time: O(m * n)
    # Space: O(m * n)


print(max_path_sum_tabulation(grid))
