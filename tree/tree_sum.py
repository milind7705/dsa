from node import a


def tree_sum_recursive(root):
    if not root:
        return 0
    leftSum = tree_sum_recursive(root.left) if root.left else 0
    rightSum = tree_sum_recursive(root.right) if root.right else 0
    return root.value + leftSum + rightSum


print(tree_sum_recursive(a))
