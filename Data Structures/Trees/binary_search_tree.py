class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def add_node(self, root, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            if data <= root.data:
                if root.left == None:
                    root.left = new_node
                else:
                    self.add_node(root.left, data)
            if data > root.data:
                if root.right == None:
                    root.right = new_node
                else:
                    self.add_node(root.right, data)

    def pre_order_traversal(self, root):
        if root == None:
            return
        else:
            print(root.data),
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def in_order_traversal(self, root):
        if root == None:
            return
        else:
            self.in_order_traversal(root.left)
            print(root.data),
            self.in_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root == None:
            return
        else:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.data),

    def print_leaf_nodes(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            print(root.data)
        else:
            self.print_leaf_nodes(root.left)
            self.print_leaf_nodes(root.right)

a = BST()
a.add_node(a.root, 3)
a.add_node(a.root, 7)
a.add_node(a.root, 1)
a.add_node(a.root, 5)
a.in_order_traversal(a.root)
print("\n")
a.pre_order_traversal(a.root)
print("\n")
a.post_order_traversal(a.root)
print("\n")
a.print_leaf_nodes(a.root)