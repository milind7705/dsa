# The Permutation Problem refers to generating all possible arrangements (permutations)
# of a given set of elements, such as numbers or characters in a string.
# It's a fundamental problem in combinatorics and is widely used in programming interviews and algorithmic challenges.

# Input: [1, 2, 3]
# [
#     [1, 2, 3],
#     [1, 3, 2],
#     [2, 1, 3],
#     [2, 3, 1],
#     [3, 1, 2],
#     [3, 2, 1]
# ]


def permute(nums):
    """
    Common pattern is backtracking and backtracking involves recursion
    :param nums:
    :return:
    """
    def backtrack(start, result):

        if start == len(nums):
            result.append(nums.copy())
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1, result)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0, result)
    return result


nums = [1, 2, 3]
print(permute(nums))