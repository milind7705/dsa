# There are n mice and n holes located on a number line. Each mouse can move to a hole,
# and the goal is to minimize the maximum distance any mouse has to travel.

# Inputs:
# mice: An array of integers representing the positions of the mice on the number line.
# holes: An array of integers representing the positions of the holes on the number line.

# Output:
# The minimum possible value of the maximum distance a mouse has to travel to reach a hole.

def assign_mice_to_holes(mice, holes):
    """
    Approach is assign mice as per their sorted order to each holes.
    Because if the mouse crosses i.e. from 0 to nth position, the distance increses and we don't want that
    :param mice:
    :param holes:
    :return:
    """
    mice.sort()
    holes.sort()

    # now calculate the maximum distance
    max_distance = 0
    for i in range(len(mice)):
        max_distance = max(max_distance, abs(mice[i] - holes[i]))
    return max_distance


mice = [3, 2, -4]
holes = [0, -2, 4]

print(f"The minimum possible maximum distance a mouse has to travel: {assign_mice_to_holes(mice, holes)} ")