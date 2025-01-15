# Write a function, intersection, that takes in two lists, a,b, as arguments.
# The function should return a new list containing elements that are in both of the two lists.
#
# You may assume that each input list does not contain duplicate elements.

def intersection(list1, list2):
    # brute force solution is to use two loops
    # result = []
    # for i in list1:
    #     if i in list2:
    #         result.append(i)
    # return result

    # Optimized code will use set datastructure to make this code O(n + m) and space O(n)
    # We are using set because adding to set takes O(1), searching in set takes O(1)
    # result = []
    # unique_elements = set()
    # for i in list1:
    #     unique_elements.add(i)
    # for i in list2:
    #     if i in unique_elements:
    #         result.append(i)
    # return result

    # shortcut
    unique_elements = set(list1)
    return [ item for item in list2 if item in unique_elements ]




print(intersection([4,2,1,6], [3,6,9,2,10]) )# -> [2,6]



a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
print(intersection(a, b)) # -> [0,1,2,3,..., 49999]
