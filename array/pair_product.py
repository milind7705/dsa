# Write a function, pair_product, that takes in a list and a target product as arguments.
# The function should return a tuple containing a pair of indices whose elements multiply to the given target.
# The indices returned must be unique.
#
# Be sure to return the indices, not the elements themselves.
#
# There is guaranteed to be one such pair whose product is the target.

def pair_product(numbers, target_product):
    # same approach as the last problem. Add current number and index to hashmap
    # calculate the complement and check if it is in the current array
    previous_nums = {}

    for index, num in enumerate(numbers):
        previous_nums[num] = index

        complement = target_product / num
        if complement in previous_nums:
            return previous_nums[complement], index



print(pair_product([3, 2, 5, 4, 1], 8)) # -> (1, 3)


numbers = [ i for i in range(1, 6001) ]
print(pair_product(numbers, 35994000)) # -> (5998, 5999)
