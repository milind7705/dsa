# The Unique Paths with Obstacles problem is a variation of the Unique Paths problem
# where some cells in the grid are obstacles, and the robot cannot pass through these cells.


def count_paths_memo(grid):
    return _count_path_recursive(grid, 0, 0)


def _count_path_recursive(grid, r, c, memo={}):
    # here we need to traverse entire tree and return 0 or 1 if the path exists
    # as usual first inbounds and outbounds check
    pos = (r, c)
    if pos in memo:
        return memo[pos]
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == "X":
        return 0

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    down_count = _count_path_recursive(grid, r + 1, c)
    right_count = _count_path_recursive(grid, r, c + 1)
    memo[pos] = down_count + right_count
    return memo[pos]


grid = [
    ["O", "O", "X"],
    ["O", "O", "O"],
    ["O", "O", "O"],
]
# print(count_paths_memo(grid)) # -> 5


def count_paths_tabulation(grid):

    # again this is pretty similar to other tabulation problems
    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == "X" or grid[rows - 1][cols - 1] == "X":
        return 0

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # base case is 0 , 0
    dp[0][0] = 1

    # traverse the first row
    for i in range(1, cols):
        dp[0][i] = dp[0][i - 1] if grid[0][i] == "O" else 0

    # populate the columns
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] if grid[i][0] == "O" else 0

    # now iterate everything
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if grid[i][j] == "O" else 0

    return dp[rows - 1][cols - 1]


print(count_paths_tabulation(grid))
