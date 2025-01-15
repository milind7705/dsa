# Write a function count_construct(target, word_bank) that accepts target and strings
# Return count of the number of ways to produce the word if the word is possible
# Time: O(m * n * m)
# Space: O(m)


def count_construct(target, wordbank):
    # construct a table
    dp = [0] * (len(target) + 1)

    # base case
    dp[0] = 1

    for i in range(len(target) + 1):
        # if dp[i] != 0:
        for word in wordbank:
            if i + len(word) < len(target) + 1 and target[i : i + len(word)].startswith(
                word
            ):
                dp[i + len(word)] += dp[i]
    print(dp)
    return dp[len(target)]


print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "c", "def", "abc"]))
print(
    count_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeee"]
    )
)
