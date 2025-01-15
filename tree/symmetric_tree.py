# Given the root of a binary tree, check whether it is a symmetric tree.
# A symmetric tree refers to a tree that is the mirror of itself, i.e., symmetric around its root.

from node import a


# def is_symmetric_tree(root):
#     if not root:
#         return True
#
#     def is_mirror(left, right):
#         # if left and right both are empty, that means the return value is true
#         if not left and not right:
#             return True
#         # if either is empty, then it's not symmetric
#         if not left or not right:
#             return False
#
#         # check if current nodes are equal and subtrees are mirrors
#         # check left.left and right.right/ left.right and right.left
#         return (
#             left.value == right.value
#             and is_mirror(left.left, right.right)
#             and is_mirror(left.right, right.left)
#         )
#
#     return is_mirror(root.left, root.right)


# print(is_symmetric_tree(a))

from collections import deque


def is_symmetric_tree_iterative(root):
    # iterative is just like the queue approach
    if not root:
        return True
    queue = deque([root.left, root.right])

    while len(queue) > 0:
        left = queue.popleft()
        right = queue.popleft()

        if not left and not right:
            continue  # continue is where we keep iterating

        # check of asymmetry
        if not left or not right:
            return False

        if left.value != right.value:
            return False

        # now add it to queue
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
    return True


print(is_symmetric_tree_iterative(a))
