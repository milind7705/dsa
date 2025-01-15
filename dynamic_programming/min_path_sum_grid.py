# The Minimum Path Sum in a Grid problem involves finding the path
# from the top-left corner to the bottom-right corner of a 2D grid
# that minimizes the sum of the values of the cells. You can only move down or right at any point in time.


def min_path_sum_tabulation(grid):
    # let's solve using tabulation
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = grid[0][0]

    # populate the first row
    for i in range(1, cols):
        dp[0][i] = dp[0][i - 1] + grid[0][i]

    # populate first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[rows - 1][cols - 1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]


print(min_path_sum_tabulation(grid))
