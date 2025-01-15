# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is
# that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# #           [2,4,5,12,7]
# #          2  /    \(non-2)
# #     [5, 12, 7]    [4, 5, 12, 7]
# #       5/     \
# #     [7]      [12, 7]
# #     7/ \
# #    0   0


def rob_recursion(nums):
    # base case , we need two branches one with include and exclude
    if len(nums) == 0:
        return 0

    include_branch = nums[0] + rob_recursion(nums[2:])
    exclude_branch = rob_recursion(nums[1:])

    return max(include_branch, exclude_branch)


def rob_recursion_memo(nums):
    return _rob_recursion_memo(nums, 0, {})


def _rob_recursion_memo(nums, i, memo):
    if i in memo:
        return memo[i]
    if i >= len(nums):
        return 0

    include_branch = nums[i] + _rob_recursion_memo(nums, i + 2, memo)
    exclude_branch = _rob_recursion_memo(nums, i + 1, memo)

    memo[i] = max(include_branch, exclude_branch)
    return memo[i]


def rob_tabulation(nums):
    dp = [0] * (len(nums) + 1)

    # base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[len(nums) - 1]


nums = [2, 7, 9, 3, 1]
print(rob_tabulation(nums))
