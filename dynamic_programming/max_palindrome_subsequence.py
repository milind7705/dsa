# Write a function, max_palin_subsequence, that takes in a string as an argument.
# The function should return the length of the longest subsequence of the string that is also a palindrome.
#
# A subsequence of a string can be created by deleting any characters of the string,
# while maintaining the relative order of characters.


# TODO this looks tricky but not that tricky at all.
# we need to use recursion here. Example lxuul.
# Starting with this string, we will first check first and last characters
# and if they match, add 2 and continue with removing those .
# If they don't match, two branches to be created one is with start word and one is end word
#                    lxuul
#                      |2
#                     xuu
#                    /   \
#                   uu    xu (need to do max at this level)
#                 2 |     / \
#                  ""    x    u
#                  0     1    1


def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string) - 1)


def _max_palin_subsequence(string, i, j, memo={}):
    pos = (i, j)
    if pos in memo:
        return memo[pos]
    # 2 base cases
    # if both characters i.e. both indexes represents same characters, return 1
    if i == j:
        return 1
    # if i crosses j, that means no palindrome found
    if i > j:
        return 0

    # actual checking of string logic
    if string[i] == string[j]:
        memo[pos] = 2 + _max_palin_subsequence(string, i + 1, j - 1)
    else:
        # if not matched, then we have 2 branches and do max
        memo[pos] = max(
            _max_palin_subsequence(string, i + 1, j),
            _max_palin_subsequence(string, i, j - 1),
        )
    return memo[pos]


print(max_palin_subsequence("xyzaxxzy"))  # -> 6
