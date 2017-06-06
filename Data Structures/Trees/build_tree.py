class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
class Tree(object):
  def __init__(self):
    self.root = None
    
  def built_tree(self):
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6);
    root.right.right = Node(7);
    root.left.left.left = Node(8);
    root.left.left.right = Node(9);
    root.left.right.left = Node(10);
    root.left.right.right = Node(20);
    root.left.right.left.left = Node(11);
    root.left.right.left.right = Node(30);
    
    self.root = root
    
    return self.root

  def pre_order_traversal(self, node):
    if node is not None:
      print(node.data)
      self.pre_order_traversal(node.left)
      self.pre_order_traversal(node.right)

  def print_tree(self):
    self.pre_order_traversal(self.root)

tree = Tree()
root = tree.built_tree()
tree.print_tree()
