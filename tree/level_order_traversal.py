from node import a


def level_order_traversal(root):
    # very similar to breadth first search except slight variation
    queue = [root]

    # store the levels
    result = []
    while len(queue) > 0:
        level = []
        for _ in range(len(queue)):
            current = queue.pop(0)
            level.append(current.value)
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
        result.append(level)
    return result


for i in level_order_traversal(a):
    print(" ".join(map(str, i)))