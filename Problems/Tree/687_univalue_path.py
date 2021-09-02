"""
687. Longest Univalue Path
Given the root of a binary tree, return the length of the longest path, 
where each node in the path has the same value. This path may or may 
not pass through the root.

The length of the path between two nodes is represented by the number 
of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.length = 0
        self.dfs(root)
        return self.length
            
    def dfs(self, node):
        if not node:
            return 0
        
        left_traverse, right_traverse = self.dfs(node.left), self.dfs(node.right)
        left, right = 0, 0
        if node.left and node.left.val == node.val:
            left = 1 + left_traverse
        if node.right and node.right.val == node.val:
            right = 1 + right_traverse
        
        # left + right bc one path as seen in example 2
        self.length = max(self.length, left + right)
        
        # if we go down one path, we cannot take the other
        return max(left, right)
        