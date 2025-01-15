graph = {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}


def explore_size(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)
    size = 1
    for neighbor in graph[current]:
        size += explore_size(graph, neighbor, visited)
    return size


def largest_component(graph):
    # traverse the indices of graph
    visited = set()
    largest = float("-inf")
    for neighbor in graph:
        size = explore_size(graph, neighbor, visited)
        if size > largest:
            largest = size
    return largest


print(largest_component(graph))
