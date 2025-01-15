from node import a


def inorder_traversal(root):
    # This results in visiting the nodes of a Binary Search Tree (BST) in ascending order.
    if not root:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)


def inorder_iterative(root):
    # this is a little different where we need to traverse via a current
    if not root:
        return []
    stack = []
    result = []
    current = root

    while current or len(stack) > 0:

        # traverse the current till left is reached and add to stack
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result


# print(inorder_traversal(a))
# print(inorder_iterative(a))


def preorder(root):
    # This traversal is useful for creating a copy of the tree or serializing it.
    if not root:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def preorder_iterative(root):
    # same as depth first search algo
    result = []
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        result.append(current.value)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return result


def post_order_iterative(root):
    # use the same thing as preorder but use second stack to reverse the process
    result = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        result.append(current)
        # note the order here, first left then right. adjust in the interviews
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    # now use result as a stack
    output = []
    while len(result) > 0:
        output.append(result.pop().value)
    return output


print(preorder(a))

print(preorder_iterative(a))


def postorder(root):
    # This traversal is useful in applications like deleting the tree,
    # evaluating expressions, or understanding dependencies.
    if not root:
        return []

    return postorder(root.left) + postorder(root.right) + [root.value]


# print(postorder(a))
# print(post_order_iterative(a))
