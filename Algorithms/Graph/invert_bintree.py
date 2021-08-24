class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Leetcode 226
def invert_b_tree(root):
    if root == None:
        return root
    left = invert_b_tree(root.left)
    right = invert_b_tree(root.right)
    root.left = right
    root.right = left


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.right = TreeNode(7)


invert_b_tree(a)