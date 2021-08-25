"""
A path in a binary tree is a sequence of nodes where 
each pair of adjacent nodes in the sequence has an edge
connecting them. A node can only appear in the sequence
at most once. Note that the path does not need to pass 
through the root.

The path sum of a path is the sum of the node's values in 
the path.

Given the root of a binary tree, return the maximum path 
sum of any path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum 
of 2 + 1 + 3 = 6.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if not node:
            return 0
        left_traverse = self.dfs(node.left)
        right_traverse = self.dfs(node.right)
        left = max(left_traverse, 0)
        right = max(right_traverse, 0)
        
        max_gain = left + right + node.val
        self.max_sum = max(self.max_sum, max_gain)
        
        
        return max(left, right) + node.val