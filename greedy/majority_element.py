# You are given an array of size n
# A majority element is an element that appears more than ⌊n/2⌋
# ⌊n/2⌋ times in the array. Your task is to determine the majority element, if it exists.

# Input: [3, 3, 4, 2, 3, 3, 3]
# Majority Element: 3 (appears 5 times out of 7).

from collections import Counter

def majority_element_naive(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i] + 1
        if count[i] > len(arr) // 2:
            return i
    return None

def majority_element_counter(arr):
    x = Counter(arr)
    for key, val in x.items():
        if val > len(arr) // 2:
            return key
    return None

def majority_element_sort(arr):
    """
    If array is sorted, the majority will always occur at the middle
    :param arr:
    :return:
    """
    arr.sort()
    candidate = arr[len(arr)//2]
    if arr.count(candidate) > len(arr)//2:
        return candidate
    return None


arr = [3, 3, 4, 2, 3, 3, 3]
# print(f"Majority element naive: {majority_element_naive(arr)}")
# print(f"Majority element naive: {majority_element_counter(arr)}")
print(f"Majority element naive: {majority_element_sort(arr)}") # least optimized as O(nlog(n))