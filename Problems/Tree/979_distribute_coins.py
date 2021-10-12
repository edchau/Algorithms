"""
You are given the root of a binary tree with n nodes where each 
node in the tree has node.val coins. There are n coins in total 
throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin 
from one node to another. A move may be from parent to child, or 
from child to parent.

Return the minimum number of moves required to make every node 
have exactly one coin.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        self.dfs(root)
        return self.total
    
    def dfs(self, node):
        # postorder, start from bottom and go up
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        self.total += abs(left) + abs(right)
        
        # Leave one coin behind
        return node.val + left + right - 1