# Given an integer array nums, return true if you can partition the array
# into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

def partition_equal_subset(nums):
    # in this problem we need to find the target sum as both partition will have total/2 sum
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target_sum = total_sum // 2
    n = len(nums)

    def partition_subset(i, target, memo):
        pos = (i, target)
        if pos in memo:
            return memo[pos]
        # base cases
        if target == 0:
            return True

        # negative case if target is negative
        if target < 0 or i == n:
            return False

        # recursive include and exclude the current element
        # look at the second part . Here we are considering nums[i] and making targetsum as 10
        # in second recursive call not considering hence targetsum is 11
        result = partition_subset(i + 1, target - nums[i], memo) or partition_subset(i + 1, target, memo)
        memo[pos] = result
        return memo[pos]

    return partition_subset(0, target_sum, {})


nums = [1,5,11,5]
nums = [1,2,3,5,17,6,14,12,6]
print(partition_equal_subset(nums))