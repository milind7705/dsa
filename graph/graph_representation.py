# graph is represented as adjacency list
adjacency_list_graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}


#   a -> b -> d -> f
#   |
#   c - > e

# edge list of undirected graph
# Every pair represents a connection between the two nodes
edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]
