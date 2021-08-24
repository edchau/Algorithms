"""
Given the root of a binary tree, return the postorder 
traversal of its nodes' values.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        order = []
        self.traverse(root, order)
        return order

    def traverse(self, node, order):
        if node == None:
            return
        
        self.traverse(node.left, order)
        self.traverse(node.right, order)
        order.append(node.val)