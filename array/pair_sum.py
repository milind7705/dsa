# Write a function, pair_sum, that takes in a list and a target sum as arguments.
# The function should return a tuple containing a pair of indices whose elements sum to the given target.
# The indices returned must be unique.
#
# Be sure to return the indices, not the elements themselves.
#
# There is guaranteed to be one such pair that sums to the target.


def pair_sum(numbers, target_sum):
    # brute force is to use two loops
    # The second loop starts with i+1 to avoid duplicate checking
    # for i in range(len(numbers)):
    #     for j in range(i + 1 , len(numbers)):
    #         if numbers[i] + numbers[j] == target_sum:
    #             return (i, j)

    # Second approach is iterate once, create a complement.
    # If complement is in the dict, that means we found the pair.
    # If not found, populate the dict with number
    # For input [3, 2, 5, 4, 1], previous_nums = { 3:0, 2:1 }. At 5, we will have complement in dict so return it
    previous_nums = {}

    for index, num in enumerate(numbers):
        complement = target_sum - num
        if complement in previous_nums:
            return previous_nums[complement], index

        previous_nums[num] = index



print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)


numbers = [ i for i in range(1, 6001) ]
print(pair_sum(numbers, 11999)) # -> (5998, 5999)
