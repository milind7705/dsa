# Given an integer array nums, find a
# subarray
#  that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# The trick here is to use min and max, because of negative numbers.
# when we encounter a number, we will multiply and store to min and max

def max_product_subarray(numbers):
    result = max(numbers) # for the worst case
    currMin, currMax = 1, 1

    for num in numbers:
        print(f"max: {currMax} min: {currMin}")
        temp = currMax * num
        currMax = max(num * currMax, num * currMin, num)
        currMin = min(temp , num * currMin, num)
        result = max(result, currMax)
    return result

nums = [-2,3,-4]
print(max_product_subarray(nums))