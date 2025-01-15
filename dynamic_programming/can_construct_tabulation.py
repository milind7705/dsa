# Write a function can_construct(target, word_bank) that accepts target and strings
# Return true if the word is possible
# m: target n: number of words in wordbank
# Time: O(m * n * m)
# Last m comes from line 1: target[i+len(word)]
# Space: O(m)


def can_construct(target, word_bank):
    # first create a table of length target + 1
    # each reachable position will store true
    # this means if ab can be made, position of 0 > 1 > 2 = True i.e. pos 2 has True

    dp = [False] * (len(target) + 1)
    # base case
    dp[0] = True

    for i in range(len(target) + 1):
        if dp[i] == True:
            for word in word_bank:
                if i + len(word) < len(target) + 1 and target[
                    i : i + len(word)
                ].startswith(word):
                    dp[i + len(word)] = True

    print(dp)
    return dp[len(target)]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(
    can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeee"])
)
