# Write a function, most_frequent_char, that takes in a string as an argument.
# The function should return the most frequent character of the string.
# If there are ties, return the character that appears earlier in the string.
#
# You can assume that the input string is non-empty.

from collections import Counter
def most_frequent_character(string):
    # Just like anagram create the counter dict
    # In case of tie, we have to iterate the initial string to store the best using counts
    # and check if current char is greater than best frequency
    count = Counter(string)

    best = None

    for char in string:
        if best is None or count[char] > count[best]:
            best = char

    return best

print(most_frequent_character("bumblebee"))