"""
Given the root of a binary tree, determine if it is a 
valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with 
keys less than the node's key.
The right subtree of a node contains only nodes with 
keys greater than the node's key.
Both the left and right subtrees must also be 
binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = []
        self.traverse_inorder(root, inorder)
        print(inorder)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False
        return True
        
    def traverse_inorder(self, root, inorder):
        if root == None:
            return
        self.traverse_inorder(root.left, inorder)
        inorder.append(root.val)
        self.traverse_inorder(root.right, inorder)