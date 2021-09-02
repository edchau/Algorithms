"""
Given the root of a binary tree, return the 
length of the diameter of the tree.

The diameter of a binary tree is the length of 
the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented 
by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        self.diameter = 0
        self.dfs(root)
        return self.diameter
        
    def dfs(self, root):
        if not root:
            return 0
        
        left_trav, right_trav = self.dfs(root.left), self.dfs(root.right)
        left, right = 0, 0
        if root.left:
            left = 1 + left_trav
        if root.right:
            right = 1 + right_trav
        
        self.diameter = max(self.diameter, left + right)
        return max(left, right)