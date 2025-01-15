from node import a
import math


def max_path_sum(root):
    if not root:
        return -math.inf
    if not root.left and not root.right:
        return root.value
    return root.value + max(max_path_sum(root.left), max_path_sum(root.right))


print(max_path_sum(a))
