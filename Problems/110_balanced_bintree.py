"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every 
node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, 0) != -1
            
    def check(self, node, depth):
        if node == None:
            return depth
        left = self.check(node.left, depth+1)
        right = self.check(node.right, depth+1)

        if abs(left-right) > 1 or left == -1 or right == -1:
            return -1

        return max(left, right)
