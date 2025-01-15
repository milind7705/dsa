from node import a


def breadth_first_search(root):
    # breadth first search is always iterative
    result = []
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.value)
        queue.append(current.left) if current.left else None
        queue.append(current.right) if current.right else None
    return result


# print(breadth_first_search(a))
