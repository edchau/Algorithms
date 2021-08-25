"""
Given the root of a binary tree, check whether it is a 
mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.compare(root, root)
    
    def compare(self, left, right):
        if left == None and right == None:
            return True
        if left != None and right != None:
            if left.val == right.val:
                return self.compare(left.left, right.right) and self.compare(left.right, right.left)
            
        return False