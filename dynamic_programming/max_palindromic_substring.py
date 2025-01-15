# Given a string s, return the longest palindromic substring in s.

# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"

#TODO need to practice this more, the logic here is we will iterate the string
# in each iteration, we will have another loop check for palindrome and store it's indexes
# From solution, it looks simple as approach is simple but it is tricky to come up with

def longest_palindrome_substring(string):

    res = ""
    res_length = 0

    for i in range(len(string)):
        # for odd behavior of palindrome
        l = i
        r = i

        while l >= 0 and r < len(string) and string[l] == string[r]:
            # do the logic of matching length and storing string
            # r - l + 1 is the length of string
            if (r - l + 1) > res_length:
                res_length = (r - l + 1)
                res = string[l: r + 1]
            l -= 1
            r += 1
        # for even behaviour
        l = i
        r = i + 1

        while l >= 0 and r < len(string) and string[l] == string[r]:
            # do the logic of matching length and storing string
            # r - l + 1 is the length of string
            if (r - l + 1) > res_length:
                res_length = (r - l + 1)
                res = string[l: r + 1]
            l -= 1
            r += 1
    return res


s = "babad"
print(longest_palindrome_substring(s))