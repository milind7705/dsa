from node import a
import math


def tree_min_recursive(root):
    if not root:
        return math.inf

    return min(
        root.value, tree_min_recursive(root.left), tree_min_recursive(root.right)
    )


print(tree_min_recursive(a))
