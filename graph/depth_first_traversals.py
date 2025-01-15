from graph.graph_representation import adjacency_list_graph


def depth_first_traversal(graph, node):
    print(node)
    for neighbor in graph[node]:
        depth_first_traversal(graph, neighbor)


depth_first_traversal(adjacency_list_graph, "a")


def depth_first_iterative(graph, node):
    stack = [node]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)


depth_first_iterative(adjacency_list_graph, "a")
