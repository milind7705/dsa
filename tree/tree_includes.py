from node import a


# def tree_includes(root, target):
#     if not root:
#         return False
#     if root.value == target:
#         return True
#     return tree_includes(root.left, target) or tree_includes(root.right, target)
#
# print(tree_includes(a, 7))


def tree_includes_iterative(root, target):
    queue = [root]
    while len(queue) > 0:
        current = queue.pop()
        if current.value == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False


print(tree_includes_iterative(a, 2))
