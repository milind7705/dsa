from graph.graph_representation import edges


# first convert the edges into a graph


def create_graph(edges):
    graph = {}
    for edge in edges:
        vertex1, vertex2 = edge
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []
        # as there is an edge, we need to populate both vertices to show an edge
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
    return graph


# print(create_graph(edges))


def has_path(graph, nodeA, nodeB, visited):
    # the order of this condition doesn't matter
    if nodeA in visited:
        return False
    visited.add(nodeA)
    if nodeA == nodeB:
        return True
    for neighbor in graph[nodeA]:
        if has_path(graph, neighbor, nodeB, visited):
            return True
    return False


def undirected_path(edges, nodeA, nodeB):
    graph = create_graph(edges)
    print(has_path(graph, nodeA, nodeB, set()))


undirected_path(edges, "i", "k")
