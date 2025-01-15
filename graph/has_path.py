# if there is a path between two nodes in the graph.
# TODO: this is a directed graph so it's fine not to detect cycle

from graph.graph_representation import adjacency_list_graph


def has_path(graph, start, end):
    if start == end:
        return True
    for neighbor in graph[start]:
        if has_path(graph, neighbor, end) == True:
            return True

    return False


print(has_path(adjacency_list_graph, "b", "a"))


def has_path_iterative(graph, start, end):
    # use breadth first code
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


print(has_path_iterative(adjacency_list_graph, "b", "e"))
