"""
Given the root of a Binary Search Tree (BST), return the 
minimum absolute difference between the values of any 
two different nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return True
        
        stack = []
        prev = None
        min_diff = float('inf')
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if prev != None:
                min_diff = min(min_diff, abs(root.val - prev.val))
            
            prev = root
            root = root.right
            
        return min_diff
        