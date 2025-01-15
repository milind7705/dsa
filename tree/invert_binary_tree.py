# Given the root node of a binary tree, transform the tree by swapping each node’s left and right subtrees,
# thus creating a mirror image of the original tree. Return the root of the transformed tree.

from node import a
from breadth_first_search import breadth_first_search

# def invert_binary_tree(root):
#     if not root:
#         return None
#     # recursively invert the left subtree
#     if root.left:
#         invert_binary_tree(root.left)
#
#     #  # recursively invert the left subtree
#     if root.right:
#         invert_binary_tree(root.right)
#     # Actual inverting
#     root.left, root.right = root.right, root.left
#     return root


def invert_binary_tree_iterative(root):
    # same as breadth first search but now we need to swap
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        current.left, current.right = current.right, current.left

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return root


tree = invert_binary_tree_iterative(a)
print(breadth_first_search(tree))
