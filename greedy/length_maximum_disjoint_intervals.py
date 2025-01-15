# You are given a list of intervals, where each interval is represented as [start, end].
# Your task is to find the largest set of intervals such that no two intervals overlap.
# Input: [[1, 3], [2, 4], [4, 5]]
# Output: 2
# Explanation: The maximum set of disjoint intervals is [[1, 3], [3, 5]].

def length_of_maximum_disjoing_intervals(arr):
    """
    This is purely greedy problem where hypothesis is sort by end key.
    If our start is less than or equal to end key, do nothing
    else make the current interval our previous and next
    :param arr:
    :return:
    """
    arr.sort(key=lambda x: x[1])
    print(arr)
    prev_start, prev_end = arr[0]
    count = 1
    for start, end in arr:
        if start <= prev_end:
            pass
        else:
            prev_start, prev_end = start, end
            count += 1
    return count

# arr = [[1, 3], [2, 4], [4, 5]]
arr = [[1, 3], [3, 4], [4, 5]]
print(f"Length of disjoint interval: {length_of_maximum_disjoing_intervals(arr)}")

