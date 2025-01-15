grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
]


def explore(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return 0

    if grid[r][c] == "W":
        return 0

    pos = (r, c)
    if pos in visited:
        return 0
    size = 1
    visited.add(pos)
    size += explore(grid, r - 1, c, visited)
    size += explore(grid, r + 1, c, visited)
    size += explore(grid, r, c - 1, visited)
    size += explore(grid, r, c + 1, visited)
    return size


def minimum_island(grid):
    min_size = float("inf")
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore(grid, r, c, visited)
            # 0 comparison is needed because of line 17, it returns zero and we don't want that
            if size > 0 and size < min_size:
                min_size = size
    return min_size


print(minimum_island(grid))
