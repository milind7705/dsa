###### Need to REDO this problem #######

# The Minimum Number of Moves to Seat Together problem involves
# finding the minimum number of moves required to seat people together in a row of seats.
# Given a string "x" represents the occupied seat and "." represents empty seat.

# Input: "..x..x."
# Output: 2
# Explanation:
# - Move the first `x` to the nearest `.` → cost = 1
# - Move the second `x` to the nearest `.` → cost = 1
# Total cost = 1 + 1 = 2.

# Input: "x.x.x."
# Output: 2
# Explanation:
# - Move the first `x` (at index 0) to the nearest `.` (at index 1) → cost = 1.
# - Move the second `x` no movement -> cost = 0
# - Move the third `x` (at index 4) to the next nearest `.` (at index 5) → cost = 1.
# Total cost = 1 + 0 + 1 = 2.

def min_moves_to_seat_together(seats: str) -> int:
    # Find all occupied seat indices
    occupied_seats = [i for i, val in enumerate(seats) if val == "x"]
    # If there are no occupied seats or just one, no moves are needed
    if len(occupied_seats) <= 1:
        return 0
    # Find the median index among occupied seats
    median_index = len(occupied_seats) // 2
    print(median_index)
    # now median position will give the position in the original list
    median_position = occupied_seats[median_index]
    print(median_position)
    # For occupied_positions = [0, 2, 4], target_block = [1,2,3]
    # Align around the median:
    # We want final positions to be a contiguous block.
    # Let the block start at (median_pos - median_index), so that
    # the occupant currently at median_pos doesn't have to move.
    start = median_position - median_index
    print(start)
    moves = 0
    for i, pos in enumerate(occupied_seats):
        moves += abs(pos - (start + i))

    # Calculate total moves needed
    return moves

# Example usage:
input_str = "x.x.x."
print(min_moves_to_seat_together(input_str))  # Expected output: 2



# arrangement = "x.x.x."
# arrangement = "..x.x"
# print(f"Minimum number of moves for seating together: {min_moves_to_seat_together(arrangement)}")