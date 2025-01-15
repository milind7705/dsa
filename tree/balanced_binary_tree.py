# The Balanced Binary Tree problem involves determining whether a binary tree is height-balanced.
# The height of left and right subtree differs by at most 1
# The following tree is balanced by definition
#         1
#        /  \
#       2     3
#            /
#           4

from node import a


def calculate_height(root):
    if not root:
        return -1

    return 1 + max(calculate_height(root.left), calculate_height(root.right))


def is_balanced_binary_tree(root):
    # propogate the heights through to the last and check the absolute difference
    if not root:
        return True

    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced_binary_tree(root.left) and is_balanced_binary_tree(root.right)


print(is_balanced_binary_tree(a))
