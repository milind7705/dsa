# Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column.
# In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots.
# The function should return a number representing the length of the shortest path
# from the starting position to a carrot. You may move up, down, left, or right,
# but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.

grid = [
    ["O", "O", "O", "O", "O"],
    ["O", "X", "O", "O", "O"],
    ["O", "X", "X", "O", "O"],
    ["O", "X", "C", "O", "O"],
    ["O", "X", "X", "O", "O"],
    ["C", "O", "O", "O", "O"],
]

# TODO: you can't pass through walls, that is the main reason here
# TODO this is a variation of breadth first search e.g like shortest path


def closest_carrot(grid, start, end):
    # create a visited set
    visited = {(start, end)}
    queue = [(start, end, 0)]
    while len(queue) > 0:
        row, col, distance = queue.pop(0)

        # first check if the carrot is found at current position
        if grid[row][col] == "C":
            return distance

        # now check for the either distance
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in delta:
            new_row = row + dx
            new_col = col + dy
            # check row in bounds
            row_inbounds = 0 <= new_row < len(grid)
            col_inbounds = 0 <= new_col < len(grid[0])

            # new position
            pos = (new_row, new_col)

            # now do the logic of adding to queue in single step

            if (
                row_inbounds
                and col_inbounds
                and pos not in visited
                and grid[new_row][new_col] != "X"
            ):
                visited.add(pos)
                queue.append((new_row, new_col, distance + 1))
    return -1


print(closest_carrot(grid, 1, 2))
