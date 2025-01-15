# Given a binary tree, you need to compute the length of the tree’s diameter.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# Note: The length of the path between two nodes is represented by the number of edges between them.


# TODO: in case of non-root path, it consists either in left or right subtree
# This problem is little complicated

from node import a


def calculate_diameter(root):
    # base case
    if not root:
        return 0

    # 1 is added to accomodate edge
    left_subtree_height = 1 + calculate_height(root.left)
    right_subtree_height = 1 + calculate_height(root.right)

    through_root_height = left_subtree_height + right_subtree_height

    return max(
        through_root_height,
        calculate_diameter(root.left),
        calculate_diameter(root.right),
    )


def calculate_height(root):
    if not root:
        return -1

    return 1 + max(calculate_height(root.left), calculate_height(root.right))


print(calculate_diameter(a))
