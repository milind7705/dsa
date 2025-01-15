# Write a function, all_tree_paths, that takes in the root of a binary tree.
# The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.
#
# The order within an individual path must start at the root and end at the leaf,
# but the relative order among paths in the outer list does not matter.
#
# You may assume that the input tree is non-empty.
# TODO: this is complicated problem, read carefully

from node import a


def all_tree_paths(root):
    def depth_first_search(root, path, result):
        if not root:
            return
        path.append(root.value)
        if root.left is None and root.right is None:
            result.append(list(path))

        depth_first_search(root.left, path, result)
        depth_first_search(root.right, path, result)

        path.pop()  # this is to backtrack after considering the current path

    result = []  # to store the list of list of paths
    depth_first_search(root, [], result)  # passing empty list for individual path
    return result


print(all_tree_paths(a))
