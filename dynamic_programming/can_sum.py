# can_sum(target, numbers), return true if the numbers in the array can generate the target_sum
# can_sum(7, [5, 3, 4, 7])
# TODO: build the approach using brute force
#           7
#      / T/ \  \T
#     2  4   3   0 # this level after subtracting the individual elements
#      4/ \3  \3
#      0   1   0


def can_sum(target_sum, nums, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in nums:
        remainder = target_sum - num
        if can_sum(remainder, nums):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


print(can_sum(7, [5, 3, 4, 7]))

print(can_sum(300, [7, 14]))

# complexity for brute force: O(n^m)
# Memoized complexity: O(m*n)
