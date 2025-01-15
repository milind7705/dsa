
def is_anagram(string1, string2):
    return count_chars(string1) == count_chars(string2)

def count_chars(string):
    count = {}

    for char in string:
        if char not in count:
            count[char] = 0
        count[char] += 1

    return count

from collections import Counter

def is_anagram_counter(string1, string2):
    return Counter(string1) == Counter(string2)
    # Time: O(n) as counter involves n times iteration over string
    # Space: O(k) where k is number of unique characters

print(is_anagram("dalda", "aldda"))

print(is_anagram_counter("dalda", "aldda"))