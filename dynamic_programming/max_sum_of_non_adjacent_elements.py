# Write a function, non_adjacent_sum, that takes in a list of numbers as an argument.
# The function should return the maximum sum of non-adjacent items in the list.
# There is no limit on how many items can be taken into the sum as long as they are not adjacent.
# For example, given:
#
# [2, 4, 5, 12, 7]
#
# The maximum non-adjacent sum is 16, because 4 + 12.
# 4 and 12 are not adjacent in the list.
#           [2,4,5,12,7]
#          2  /    \(non-2)
#     [5, 12, 7]    [4, 5, 12, 7]
#       5/     \
#     [7]      [12, 7]
#     7/ \
#    0   0
# Time: O(2^n) as there are always two branches to the decision
# Space: O(n) - height of the tree


def non_adjacent_sum(numbers):
    # TODO use classic brute force recursion where one branch will take 1st element, skip 2nd and use rest
    # Second branch will have skipped first element and remaining elements of list

    # Base case is if len of numbers list is zero
    if len(numbers) == 0:
        return 0
    # now create two branches
    include_branch = numbers[0] + non_adjacent_sum(numbers[2:])
    exclude_branch = non_adjacent_sum(numbers[1:])

    return max(include_branch, exclude_branch)


def non_adjacent_sum_memo(numbers):
    return _non_adjacent_sum_memo(numbers, 0)


def _non_adjacent_sum_memo(numbers, i, memo={}):
    # TODO in here use the indexes instead of slice to avoid creating arrays
    # Base case is if i is greater than len of numbers
    if i in memo:
        return memo[i]
    if i >= len(numbers):
        return 0
    # now create two branches
    include_branch = numbers[i] + _non_adjacent_sum_memo(numbers, i + 2, memo)
    exclude_branch = _non_adjacent_sum_memo(numbers, i + 1, memo)

    memo[i] = max(include_branch, exclude_branch)
    return memo[i]
    # Time: O(n) - because of single iteration now after we've done memoization


def non_adjacent_sum_tabulation(numbers):
    dp = [0] * (len(numbers) + 1)

    # base case
    dp[0] = numbers[0]
    dp[1] = max(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        dp[i] = max(dp[i - 1], numbers[i] + dp[i - 2])

    print(dp)
    return dp[len(numbers) - 1]


nums = [2, 4, 5, 12, 7]
print(non_adjacent_sum(nums))  # -> 16

nums = [7, 5, 5, 12]
print(non_adjacent_sum(nums))  # -> 19


print(non_adjacent_sum_memo(nums))  # -> 19

print(non_adjacent_sum_tabulation(nums))
