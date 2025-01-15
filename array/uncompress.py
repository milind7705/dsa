# Write a function, uncompress, that takes in a string as an argument.
# The input string will be formatted into multiple groups according to the following pattern:
# <number><char>
#
# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char'
# of a group is repeated 'number' times consecutively.
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def uncompress(string):
    # approach is two pointers
    # e.g. 2a1b
    # Initialize i and j to zero, start j as fast pointer till length of string
    # if element at j is number, keep incrementing
    #If we encounter non-number at j, append to the result with s[i:j] * s[j]
    # Note s[i:j] represents the number i.e. 2, 20 etc
    # Finally update the j pointer to +1 and i pointer to j

    result = ""
    numbers = "0123456789"
    i = j = 0

    while j < len(string):
        if string[j] in numbers:
            j += 1
        else:
            number = int(string[i:j])
            result += string[j] * number # this is linear and because of that incresing complexity
            # AS string are immutable and replace will create separate string
            j += 1
            i = j
    return result

def uncompress(string):
    result = [] # lists are mutable so appending won't impact anything
    i = j = 0
    numbers = "0123456789"

    while j < len(string):
        if string[j] in numbers:
            j += 1
        else:
            number = int(string[i:j])
            result.append(string[j] * number)
            j += 1
            i = j
    return "".join(result) # this will not create problem as it is outside the loop


# Complexity: n - number of groups m - maximum number in any ground = O(n * m)
# e.g. 1000p1000q, here complexity is not defined by len of string but by numbers attached to the group
# Space: O(n * m)

print(uncompress("4s2b")) # -> 'ssssbb'
print(uncompress("2c3a1t")) # -> 'ccaaat'
