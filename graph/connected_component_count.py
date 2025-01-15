graph = {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}


def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    # This True is important, that means the component has been explored
    return True


def connected_component_count(graph):
    visited = set()
    count = 0
    # TODO: need two loops, one is for key and other loop is for values
    for neighbor in graph:
        # print(neighbor)
        if explore(graph, neighbor, visited):
            count += 1
    return count


print(connected_component_count(graph))
