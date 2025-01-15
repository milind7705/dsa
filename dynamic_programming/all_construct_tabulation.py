# Write a function all_construct(target, word_bank) that accepts target and strings
# Return all of the number of ways to produce the word if the word is possible

# time: O(n ^ m) as there are exponential combinations
# Space: O(n^m)


def all_construct(target, wordbank):
    # create a dp array
    dp = [[] for _ in range(len(target) + 1)]

    # default return the empty list
    dp[0] = [[]]
    for i in range(len(target) + 1):
        for word in wordbank:
            if i + len(word) < len(target) + 1 and target[i : i + len(word)].startswith(
                word
            ):
                # need to add word to each combination preset at dp[i + len(word)]
                # plus need to add
                # print(dp[i])
                # TODO key is first add current word to existing list of dp[i], then think ahead
                new_combinations = [combination + [word] for combination in dp[i]]
                # print(new_combinations)
                # print(dp[i + len(word)])
                dp[i + len(word)] = dp[i + len(word)] + new_combinations
                # print(dp[i + len(word)])
    print(dp)
    return dp[len(target)]


print(all_construct("abcdef", ["ab", "abc", "cd", "ef", "def", "abcd"]))
# print(
#     all_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeez", ["e", "ee", "eee", "eeee", "eeee"]
#     )
# )
