# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        head_root = root
        if root:
            q = []
            q.append(root)
            print(q)
            while(q):
                root = q.pop(0)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                left = root.left
                right = root.right
                root.left = right
                root.right = left
            return head_root
