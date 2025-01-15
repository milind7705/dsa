# how_sum(target, numbers), return a combination if the numbers in the array can generate the target_sum
# how_sum(7, [5, 3, 4, 7])
# TODO: build the approach using brute force
#              7
#      / [4,3]/ \  \[7]
#     2    4     3   0 # this level after subtracting the individual elements
#      [4]/ \3   \3
#      0     1   0


def how_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            remainder_result.append(num)  # this is m times as copying array is linear
            memo[target_sum] = remainder_result
            return memo[target_sum]
    memo[target_sum] = None
    return None


print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(300, [7, 14]))

# Time: O(n * m * m)
# Space: O(m*m) # because of array
