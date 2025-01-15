# all_sum(target, numbers), return a combination if the numbers in the array can generate the target_sum
# all_sum(7, [5, 3, 4, 7])
# TODO: build the approach using brute force
#              7
#      / [4,3]/ \  \[7]
#     2    4     3   0 # this level after subtracting the individual elements
#      [4]/ \3   \3
#      0     1   0
# TODO this is very intuitive


def all_sum(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return [[]]

    if target_sum < 0:
        return None

    all_combination = []
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = all_sum(remainder, numbers, memo)
        if remainder_combination is not None:
            for combination in remainder_combination:
                all_combination.append(combination + [num])
    memo[target_sum] = all_combination if all_combination else None
    return memo[target_sum]


print(all_sum(7, [5, 3, 4, 7]))
print(all_sum(21, [1, 5, 3, 4, 25]))

# Complexity: m - targetSum n- numbers
# Brute force: n^m * m
# Memoized solution: O (n * m * m) Space: O(m * m)
