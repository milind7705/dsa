from graph.graph_representation import adjacency_list_graph


def breadth_first_iterative(graph, node):
    queue = [node]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)


breadth_first_iterative(adjacency_list_graph, "a")
