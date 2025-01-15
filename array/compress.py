# Write a function, compress, that takes in a string as an argument.
# The function should return a compressed version of the string
# where consecutive occurrences of the same characters are compressed into the
# number of occurrences followed by the character. Single character occurrences should not be changed.

# def compress(string):
#     result = ""
#     i = j = 0
#
#     # fast pointer is j
#     while j < len(string):
#         if string[j] == string[i]:
#             j += 1
#         else:
#             number = j - i
#             if number == 1:
#                 number = ""
#             result += f"{number}{string[i]}"
#             i = j
#     # for the last iteration
#     result += f"{j - i}{string[i]}"
#     return result

def compress(string):
    # Add some new character to the string
    string += "!"
    result = []
    i = j = 0

    while j < len(string):
        if string[j] == string[i]:
            j += 1
        else:
            number = j - i
            if number == 1:
                result.append(string[i])
            else:
                result.append(str(number))
                result.append(string[i])
            i = j
    return "".join(result)
    # Time: O(n) Space: O(n)

print(compress('ccaaatsss')) # -> '2c3at3s'
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'))
# -> '127y'
