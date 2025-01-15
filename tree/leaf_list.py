# Write a function, leaf_list, that takes in the root of a binary tree and
# returns a list containing the values of all leaf nodes in left-to-right order.

from node import a


def leaf_list(root):
    if not root:
        return []

    left_values = leaf_list(root.left)
    right_values = leaf_list(root.right)
    if not root.left and not root.right:
        return [root.value]
    return [*left_values, *right_values]


def leaf_list_iterative(root):
    result = []
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        if not current.left and not current.right:
            result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


print(leaf_list(a))
print(leaf_list_iterative(a))
