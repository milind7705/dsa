# number of ways to travel from top-left to bottom-right of the grid.
# You can only move down or right
# Grid is m*n
# TODO : DP first needs to be solved using brute force method and then only think of optimization
# Think of base cases first


def grid_traveller(m, n, memo={}):
    key = f"{m},{n}"
    if key in memo:
        return memo[key]
    # if both of the m and n is 1, the ways is 1.
    if m == 1 and n == 1:
        return 1

    # if either m or n, means 2,0 will have 0
    if m == 0 or n == 0:
        return 0

    # down will be m - 1 and right will be n - 1
    memo[key] = grid_traveller(m - 1, n, memo) + grid_traveller(m, n - 1, memo)
    return memo[key]


print(grid_traveller(2, 3))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))
