"""
Given the root of a Binary Search Tree (BST), return 
the minimum difference between the values of any two 
different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """     
        stack = []
        min_diff = float('inf')
        prev = None
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            if prev != None:
                min_diff = min(root.val - prev.val, min_diff)
            
            prev = root
            root = root.right
        
        return min_diff