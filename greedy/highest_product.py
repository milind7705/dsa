# Given an array of integers, find the highest product that can be achieved
# by multiplying three distinct numbers from the array.

# Input: [1, 10, 2, 6, 5, 3]
# Output: 300
# Explanation: The highest product is 10 × 6 × 5 = 300.

# Input: [-10, -10, 5, 2]
# Output: 500
# Explanation: The highest product is -10 × -10 × 5 = 500 (two negatives make a positive).

def highest_product(arr):
    """
    Logic is sort first.
    Then find the last 3 elements in case of all positive integers
    OR
    last one and first 2 in case of both negative numbers
    :param arr:
    :return:
    """
    arr = sorted(arr)

    hi3 = arr[-1] * arr[-2] * arr[-3]
    low2_hi1 = arr[0]* arr[1] * arr[-1]

    return max(hi3, low2_hi1)

arr = [-10, -10, 5, 2]
print(f"Highest product {highest_product(arr)}")