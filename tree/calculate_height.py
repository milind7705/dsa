# calculate the height of the tree

from node import a

# recursive


def calculate_height(root):
    if not root:
        return -1
    # if root.left:
    #     calculate_height(root.left)
    # if root.right:
    #     calculate_height(root.right)
    return 1 + max(calculate_height(root.left), calculate_height(root.right))


# iterative


def calculate_height_iterative(root):
    height = 0
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)

        if current.left is None and current.right is None:
            height += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return height


print(calculate_height(a))

# print(calculate_height_iterative(a))
