# You have intercepted a secret message encoded as a string of numbers.
# The message is decoded via the following mapping:
#
# "1" -> 'A'
#
# "2" -> 'B'
#
# ...
#
# "25" -> 'Y'
#
# "26" -> 'Z'
#
# However, while decoding the message,
# you realize that there are many different ways you can decode the message
# because some codes are contained in other codes ("2" and "5" vs "25").
#
# For example, "11106" can be decoded into:
#
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Input: s = "226"
#
# Output: 3
#
# Explanation:
#
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

def decode_ways(string):
    # we can take first character if it is non-zero
    #and for second character there is a condition that it should be either 1 or 2 followed by 0-6
    dp = {len(string): 1}

    def dfs(i):
        if i in dp:
            return dp[i]

        # if string starts with zero, return zero
        if i == "0":
            return 0

        # pass the i + 1 to dfs
        res = dfs(i + 1)
        if (i + 1) < len(string) and (string[i] == "1" or string[i] == "2" and string[i + 1] in "0123456"):
            res += dfs(i + 2)
        dp[i] = res
        return res
    return dfs(0)

print(decode_ways("226"))


def num_decodings(s):
    n = len(s)
    def decode(i):
        # base case
        if i == n:
            return 1

        if s[i] == "0":
            return 0

        result = 0

        if 1 <= int(s[i]) <= 9:
            result += decode(i + 1)

        if i + 1 < n and  10 <= int(s[i: i + 2]) <= 26:
            result += decode(i + 2)

        return result

    return decode(0)

print(num_decodings("226"))