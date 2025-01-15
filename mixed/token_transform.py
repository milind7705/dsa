# Write a function, token_transform, that takes in a dictionary of tokens and a string.
# In the dictionary, the replacement values for a token may reference other tokens.
# The function should return a new string where tokens are replaced with their fully evaluated string values.
#
# Tokens are enclosed in a pair of '$'.
# You can assume that the input string is properly formatted and "$" is not used in the string except to enclose a token.
#
# You may assume that there are no circular token dependencies.

# tokens = {
#   '$LOCATION$': '$ANIMAL$ park',
#   '$ANIMAL$': 'dog',
# }
# token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# # -> 'Walk the dog in the dog park!'

# tokens = {
#   '$0$': "$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$",
#   '$1$': "$2$$2$$2$$2$$2$$2$$2$$2$$2$",
#   '$2$': "$3$$3$$3$$3$$3$$3$$3$",
#   '$3$': "$4$$4$$4$$4$$4$$4$",
#   '$4$': "$5$$5$$5$$5$$5$",
#   '$5$': "$6$$6$$6$$6$",
#   '$6$': "$7$$7$$7$",
#   '$7$': "$8$$8$",
#   '$8$': "",
# }
# token_transform("z$0$z$0$z$0$z$0$z$0$z$0$z", tokens)
# # -> 'zzzzzzz'

def token_transform(s, tokens):
    # Approach is you can't do two level checking because of input above.
    # There needs to be exhaustive checking for the token using recursion
    # This is similar to graph problem and depth first search
    # Use the same approach as previous one and use recursion for each token replacement and memoization
    i = 0
    j = i + 1
    output = ""

    while i < len(s):
        if s[i] != "$":
            output += s[i]
            i += 1
            j = i + 1
        elif s[j] != "$":
            j = j + 1
        else:
            token = s[i: j + 1]
            value = tokens[token]
            evaluated_value = token_transform(value, tokens)
            tokens[value] = evaluated_value
            output += evaluated_value
            i = j + 1
            j = i + 1
    # print(tokens)
    return output
# Time: O(n ^ m) exponential because of last example
# Space: O(n ^ m) we have to store that many examples

tokens = {
  '$LOCATION$': '$ANIMAL$ park',
  '$ANIMAL$': 'dog',
}
print(token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens))


tokens = {
  '$0$': "$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$",
  '$1$': "$2$$2$$2$$2$$2$$2$$2$$2$$2$",
  '$2$': "$3$$3$$3$$3$$3$$3$$3$",
  '$3$': "$4$$4$$4$$4$$4$$4$",
  '$4$': "$5$$5$$5$$5$$5$",
  '$5$': "$6$$6$$6$$6$",
  '$6$': "$7$$7$$7$",
  '$7$': "$8$$8$",
  '$8$': "",
}
print(token_transform("z$0$z$0$z$0$z$0$z$0$z$0$z", tokens))
# # -> 'zzzzzzz'
