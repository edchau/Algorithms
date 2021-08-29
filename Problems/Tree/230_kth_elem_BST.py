"""
Given the root of a binary search tree, and an integer k,
 return the kth (1-indexed) smallest element in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while root != None or len(stack) >= 0:
            while root != None:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            
            root = root.right
            
            