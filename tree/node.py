class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#                  1
#               /    \
#              2       3
#            /   \      \
#           4     5      6

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
h = Node(7)

a.left = b
a.right = c
b.left = d
# c.right = f
b.right = e
# c.left = h
# c.right = f
# f.left = h
# d.left = f
