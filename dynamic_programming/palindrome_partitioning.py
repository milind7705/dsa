# Given a string s, partition s such that every
# substring
#  of the partition is a
# palindrome
# . Return all possible palindrome partitioning of s.

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

def is_palindrome(s):
    return s == s[::-1]


def palindrome_partitioning(s):

    def generate_partition(start):
        # If we've partitioned the entire string
        if start == len(s):
            return [[]] # Base case: return an empty partition

        if start in memo:
            return memo[start]

        partitions = []

        for end in range(start, len(s)):
            if is_palindrome(s[start:end + 1]):  # Check if string[start:end+1] is a palindrome
                substring = s[start: end + 1]
                print(f"Start: {start}  End: {end}")
                print(substring)
                # recursively partition next substring
                for sub_partition in generate_partition(end + 1):
                    print(sub_partition)
                    partitions.append([substring] + sub_partition)
        memo[start] = partitions
        return partitions
    memo = {}
    # generate at the start of the index
    return generate_partition(0)


print(palindrome_partitioning("aab"))


# BACKTRACKING SOLUTION

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def palindrome_partition(s):
    """
    Partition the string into all possible palindrome partitions.

    Args:
        s (str): The input string.

    Returns:
        List[List[str]]: A list of partitions where each partition is a list of palindromic substrings.
    """
    def backtrack(start, path):
        # If we've reached the end of the string, add the current path to results
        if start == len(s):
            results.append(path[:])
            return

        # Explore all possible partitions
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)  # Choose
                backtrack(end, path)   # Explore
                path.pop()             # Unchoose

    results = []
    backtrack(0, [])
    return results