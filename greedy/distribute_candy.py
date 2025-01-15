# You are given an array of integers ratings where ratings[i] represents the rating of the i'th
#   child. You need to distribute candies to these children such that:
#
# Each child gets at least one candy.
# Children with a higher rating than their neighbors receive more candies than their neighbors.
# Return the minimum number of candies required to satisfy these conditions.

# Input: ratings = [1, 0, 2]
# Output: 5
# Explanation: Candies distributed as [2, 1, 2]. Total = 5.

# Input: ratings = [1, 2, 2]
# Output: 4
# Explanation: Candies distributed as [1, 2, 1]. Total = 4.

def distribute_candies(ratings):
    """
    First traverse from left to right scanning if the rating of kid present on the left is greater,
    if yes, then improve the ratings.
    Second traverse from right to left to check if the rating of kid present on the right is greater,
    if yes, then take the max of earlier rating and add 1 to it
    :param ratings:
    :return:
    """
    length = len(ratings)
    candies = [1] * length

    for i in range(1, length):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(length - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    print(candies)
    return sum(candies)

ratings = [1, 0, 2]
# ratings = [1, 2, 2]
print(f"Minimum number of candies required: {distribute_candies(ratings)}")