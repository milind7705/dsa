# Given an array of meeting time intervals where each interval is represented as [start, end],
# find the minimum number of meeting rooms required to hold all meetings.
# Input: [[0, 30], [5, 10], [15, 20]]
# Output: 2
# Explanation: Meeting [0, 30] overlaps with both [5, 10] and [15, 20]. We need 2 rooms.

# Input: [[7, 10], [2, 4]]
# Output: 1
# Explanation: No meetings overlap, so only 1 room is needed.

def count_meeting_room(meetings):
    """
    approach: notice the change of events. When there is start time, we have to add 1 to the tuple.
    When there is an end, we have to add -1 to the tuple.
    Sort the array.
    Now while iterating, we can store the min variable for min meeting rooms
    :param meetings:
    :return:
    """
    data = []
    for start, end in meetings:
        data.append((start, 1))
        data.append((end, -1))
    data.sort()
    print(data)
    min_room = 0
    curr = 0

    for _, change in data:
        curr += change
        min_room = max(min_room, curr)
    return min_room

meetings = [[0, 30], [5, 10], [15, 20]]
print(f"Minimum number to accommodate these meeting rooms: {count_meeting_room(meetings)}")

