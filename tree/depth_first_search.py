from node import a

# Iterative depth first search

# def depth_first_search_iterative(root):
#     result = []
#     stack = [root]
#     while len(stack) > 0:
#         current = stack.pop()
#         result.append(current.value)
#         stack.append(current.right) if current.right else None
#         stack.append(current.left) if current.left else None
#     return result


# print(depth_first_search_iterative(a))


def depth_first_recursive(root):
    if not root:
        return []

    leftValues = depth_first_recursive(root.left)
    rightValues = depth_first_recursive(root.right)
    return [root.value, *leftValues, *rightValues]


# print(depth_first_recursive(a))
