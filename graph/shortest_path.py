edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]


def build_graph(edges):
    graph = {}
    for edge in edges:
        nodeA, nodeB = edge
        if nodeA not in graph:
            graph[nodeA] = []
        if nodeB not in graph:
            graph[nodeB] = []
        graph[nodeA].append(nodeB)
        graph[nodeB].append(nodeA)
    return graph


# print(build_graph(edges))


def shortest_path(edges, nodeA, nodeB):
    # TODO: key here is breadth first search,
    # Add the element to the queue along with the initial path distance
    # while exploring, increment that distance.
    # This algo is intuitive as breadth first take care of minimum logic
    # hence we don't need to calculate the min path
    graph = build_graph(edges)
    queue = [[nodeA, 0]]
    visited = set(nodeA)
    while len(queue) > 0:
        current, distance = queue.pop(0)
        if current == nodeB:
            return distance
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])

    return -1


print(shortest_path(edges, "w", "z"))
