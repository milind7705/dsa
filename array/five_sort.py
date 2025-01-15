# Write a function, five_sort, that takes in a list of numbers as an argument.
# The function should rearrange elements of the list such that all 5s appear at the end.
# Your function should perform this operation in-place by mutating the original list.
# The function should return the list.
#
# Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.

def five_sort(numbers):
    # linear approach is two pointers
    # First i at start and j at the end
    # iterate till i and j crosses
    # if j is 5 do j -= 1
    # if i is 5 , do the swapping
    # in either case, do i + 1
    i = 0
    j = len(numbers) - 1

    while i <= j:
        if numbers[j] == 5:
            j -= 1
        elif numbers[i] == 5:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
        else:
            i += 1
    return numbers


print(five_sort([12, 5, 1, 5, 12, 7]))
# -> [12, 7, 1, 12, 5, 5]
