grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L"],
]


def explore(grid, r, c, visited):
    # TODO: first always guard for the corner case to avoid out of bounds errors
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return False
    # if water is found, return false
    if grid[r][c] == "W":
        return False
    pos = (r, c)
    if pos in visited:
        return False
    visited.add(pos)
    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)
    # TODO: true suggest an island has reached
    return True


def island_count(grid):
    # TODO: this is classic graph problem. The grid is not essentially square so need to manage row and columns
    # TODO first appraoch the problem directly and then add visited
    count = 0
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # this helper function should be recursive
            if explore(grid, r, c, visited):
                count += 1
    return count


print(island_count(grid))
