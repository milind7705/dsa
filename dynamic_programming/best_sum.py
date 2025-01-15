# best_sum(target, numbers), return a combination if the numbers in the array can generate the target_sum
# best_sum(7, [5, 3, 4, 7])
# TODO: build the approach using brute force
#              7
#      / [4,3]/ \  \[7]
#     2    4     3   0 # this level after subtracting the individual elements
#      [4]/ \3   \3
#      0     1   0


def best_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_sum = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = remainder_combination + [num]  # array copying is n times
            if shortest_sum is None or len(combination) < len(shortest_sum):
                shortest_sum = combination
    memo[target_sum] = shortest_sum
    return shortest_sum


# print(best_sum(7, [5, 3, 4, 7]))
# print(best_sum(100, [1, 5, 3, 4, 25]))

# Complexity: m - targetSum n- numbers
# Brute force: n^m * m
# Memoized solution: O (n * m * m) Space: O(m * m)


def amount(numbers, target_sum):
    if target_sum == 0:
        return 0

    if target_sum < 0:
        return None

    shortest_sum = float("inf")
    for num in numbers:
        remainder = target_sum - num
        # print(remainder)
        remainder_count = amount(numbers, remainder)
        if remainder_count is not None and remainder_count >= 0: # this greater than zero is for [2] and target 3
            current_count = 1 + remainder_count
            shortest_sum = min(shortest_sum, current_count)
    return shortest_sum if shortest_sum != float("inf") else -1

print(amount([1], 0))
print(amount([2], 3))
print(amount([5, 3, 4, 7], 7))
print(amount([5, 3, 4, 7], 7))



# def best_sum_tabulation(target_sum, numbers):
#     # First set the dp array with target_sum + 1
#     dp = [float("inf")] * (target_sum + 1)
#
#     # Base case is zero can be made with no combination
#     dp[0] = 0
#
#     for i in range(target_sum + 1):
#         # if dp[i] is not None:
#         for num in numbers:
#             if i + num < target_sum + 1:
#                 dp[i + num] = min(dp[i], dp[i] + num)  # additional m is for copying
#     print(dp)
#     return dp[target_sum]
#
# print(best_sum_tabulation(7, [1,2,3]))