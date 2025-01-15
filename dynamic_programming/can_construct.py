# Write a function can_construct(target, word_bank) that accepts target and strings
# Return true if the word is possible

# TODO the approach is same, just check if the target starts with the word of wordbank,
# if yes then take the suffix of the word and do the recursion


def can_construct_without_memoization(target, word_bank):
    if target == "":
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[
                len(word) :
            ]  # additional * m is because of copying of array
            if can_construct_without_memoization(suffix, word_bank):
                return True
    return False


# Time: m- target length, n - number of words O(n^m * m)
# Space: O(m * m)


def can_construct(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


# Time: O( n * m * m)
# Space: O (m * m)

print(can_construct("a", ["b"]))
print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(
    can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeee"])
)
