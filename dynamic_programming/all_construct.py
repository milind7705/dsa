# Write a function all_construct(target, word_bank) that accepts target and strings
# Return all of the number of ways to produce the word if the word is possible

# TODO the approach is same, just check if the target starts with the word of wordbank,
# if yes then take the suffix of the word and do the recursion


def all_construct(target, word_bank):
    if target == "":
        # returning 2D array is important
        return [[]]

    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            suffix_ways = all_construct(suffix, word_bank)
            # this step is important as we are copying a word to a 2D array's each element
            target_ways = [[word] + sublist for sublist in suffix_ways]
            result = result + target_ways
    return result


def all_construct_memo(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        # returning 2D array is important
        return [[]]

    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            suffix_ways = all_construct_memo(suffix, word_bank, memo)
            # this step is important as we are copying a word to a 2D array's each element
            target_ways = [[word] + sublist for sublist in suffix_ways]
            result = result + target_ways
    memo[target] = result
    return result


print(all_construct("abcdef", ["ab", "abc", "cd", "ef", "def", "abcd"]))
print(
    all_construct_memo(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeez", ["e", "ee", "eee", "eeee", "eeee"]
    )
)
