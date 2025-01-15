# The Bulbs Problem is a classic problem involving toggling states:
# You are given an array of n bulbs, initially all turned off.
# Each bulb has two states: on (1) and off (0).
# The goal is to turn on all the bulbs, but toggling one bulb may affect others.
# Specifically, when you toggle a bulb at position i:
# It changes its own state (on to off or off to on).
# It may cause a cascading effect on the states of bulbs at other positions.
# The problem typically asks for the
# minimum number of toggles needed to turn all the bulbs on
# or the final state of the bulbs after performing a given sequence of toggles.


def bulbs(arr):
    """
    Approach: for each even flip, the remaining array will remain same so we don't need to iterate it again
    For odd flip, we have to iterate
    :param arr:
    :return:
    """
    cost = 0 # the bit which is flipped
    for i in arr:
        if cost % 2 == 0:
            i = i
        else:
            i = not i
        if i % 2 == 1:
            continue
        else:
            cost += 1
    return cost



# arr = [0, 1, 0, 1]
arr = [0, 0, 0, 0, 1]
print(f"Minimum cost is {bulbs(arr)}")

# Complexity O(n)