# Write a function count_construct(target, word_bank) that accepts target and strings
# Return count of the number of ways to produce the word if the word is possible

# TODO the approach is same, just check if the target starts with the word of wordbank,
# if yes then take the suffix of the word and do the recursion


def count_construct(target, word_bank):
    if target == "":
        return 1
    count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if count_construct(suffix, word_bank) == 1:
                count += 1
    return count


def count_construct_memo(target, word_bank, memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if count_construct_memo(suffix, word_bank, memo) == 1:
                count += 1
    memo[target] = count
    return count


print(count_construct("abcdef", ["ab", "abc", "c", "def", "abc"]))
print(
    count_construct_memo(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeee"]
    )
)
