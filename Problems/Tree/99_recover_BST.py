"""
You are given the root of a binary search tree (BST), 
where exactly two nodes of the tree were swapped by mistake. 
Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. 
Could you devise a constant space solution?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        stack = []
        prev = TreeNode(float('-inf'))
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if first == None and prev.val >= root.val:
                first = prev
            if first != None and prev.val >= root.val:
                second = root
            
            prev = root
            root = root.right
        
        first.val, second.val = second.val, first.val