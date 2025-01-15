# The Permutation II Problem is a variant of the permutations problem
# where the input array may contain duplicate elements.
# The goal is to generate all unique permutations of the input array,
# ensuring that duplicate permutations are not included in the result.

# Input: [1, 1, 2]
# [
#     [1, 1, 2],
#     [1, 2, 1],
#     [2, 1, 1]
# ]

def permutation_with_duplicates(input):

    def backtrack(start, result):
        if start == len(input):
            result.append(input.copy())
            return
        seen = set()  # set to capture used element
        for i in range(start, len(input)):
            if input[i] in seen:
                continue
            seen.add(input[i])
            input[start], input[i] = input [i], input[start]
            backtrack(start + 1, result)
            input[start], input[i] = input[i], input[start]

    result = []
    input.sort()
    backtrack(0, result)
    return result


input =  [1, 1, 2]

print(f"Permutations without duplicates: {permutation_with_duplicates(input)}")
