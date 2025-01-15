# You are given an array arr of n integers, and an integer k.
# You can perform at most k swaps to rearrange the elements in arr.
# Your task is to return the lexicographically largest permutation of the array.

# NOTE: array will have all numbers from 1 to N, nothing is missing.
# Input: arr = [4, 3, 2, 1], k = 2
# Output: [4, 3, 1, 2]
# Explanation: By swapping 2 and 1 in two moves, we get the largest permutation.


# Input: arr = [1, 2, 3, 4], k = 1
# Output: [4, 2, 3, 1]
# Explanation: Swap 1 and 4 to maximize the first element.


def find_largest_permutation(arr, k):
    """
    First find the length to find the max element.
    Store the values in the dictionary based on its location.
    Every iteration check the position as well as the key.
    :param arr:
    :param k:
    :return:
    """
    i = 0
    _max = len(arr) # 5
    d = {val: i for i, val in enumerate(arr)}
    print(d)
    while k and i < len(arr):
        j = d[_max] # if 5 is at right position i.e. highest, do nothing
        if i == j:
            pass
        else:
            # if not at right position, swap
            k -= 1
            arr[i], arr[j] = arr[j], arr[i]
            d[arr[i]], d[arr[j]] = d[arr[j]], d[arr[i]]
            print(d)
        i += 1
        _max -= 1
    return arr


arr = [1, 2, 3, 4, 5]

k = 3

print(f"Largest lexicographic permutation {find_largest_permutation(arr, k)}")

# Time: O(n)
# Space: O(n)
