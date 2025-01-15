# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

#TODO call the logic twice, first by skipping first house so that we can pick last house
# second is skip the last house so that we can pick first house

def rob_helper(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    dp = [0] * (len(nums) + 1)

    # base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    return dp[len(nums) - 1]

def rob_house_ii(nums):
    # note that nums[0] is needed as what if there is only single house? [1]
    return max(nums[0], rob_helper(nums[1:]), rob_helper(nums[:-1]))

nums = [1,2,3,1]
print(rob_house_ii(nums))