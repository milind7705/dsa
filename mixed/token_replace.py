# Write a function, token_replace, that takes in a dictionary of tokens and a string.
# The function should return a new string where tokens are replaced.
#
# Tokens are enclosed in a pair of '$'.
# You can assume that the input string is properly formatted
# and '$' is not used in the string except to enclose a token.
# Tokens should be replaced from left to right in the string (see test_05).

# tokens = {
#   '$LOCATION$': 'park',
#   '$ANIMAL$': 'dog',
# }
# token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# # -> 'Walk the dog in the park!'

def token_replace(s, tokens):
    # Use two pointers strategy. First pointer is at first index and next is at i + 1
    # They key here is i will point to first $ and j will point to last dollar of the token
    # Once that is met, do the pointers adjustment
    i = 0
    j = i + 1
    output = ""
    # Only loop is till i
    while i < len(s):
        if s[i] != "$":
            output += s[i]
            i += 1
            j = i + 1
        elif s[j] != "$":
            j = j + 1
        else:
            token = s[i: j + 1]
            output += tokens[token]
            i = j + 1
            j = i + 1
    return output



tokens = {
  '$LOCATION$': 'park',
  '$ANIMAL$': 'dog',
}

print(token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens))

tokens = {
  '$second$': 'beta',
  '$first$': 'alpha',
  '$third$': 'gamma',
}
print(token_replace('$first$second$third$', tokens))
# -> 'alphasecondgamma'
