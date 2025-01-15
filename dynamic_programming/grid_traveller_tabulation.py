# TODO gridtraveller is where m*n grid is there, we need 2D array to traverse
# Base case is grid[1][1] = 1. If we get this 1, we will add it to right neighbor and down neighbor


def grid_traveller(m, n):
    # initialize this way only for 2D array, else it will be a shallow copy of rows
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[1][1] = 1

    # iterate through m + 1 and n + 1
    for i in range(m + 1):
        for j in range(n + 1):
            current = dp[i][j]
            if i + 1 < m + 1:
                dp[i + 1][j] += current
            if j + 1 < n + 1:
                dp[i][j + 1] += current
    return dp[m][n]


# Time: O(m*n)
# Space: O(m*n)

print(grid_traveller(2, 3))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))
