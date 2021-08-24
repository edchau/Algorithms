"""
Inorder Traversal
If tree is BST, in order will return nondecreasing
order
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
        if root == None:
            return True
        
        stack = []
        prev = None
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # add to list if doing inorder
            if prev != None and root.val <= prev.val:
                return False
            prev = root
            root = root.right
        
        return True
        