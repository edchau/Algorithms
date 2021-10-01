"""
You are given the root node of a binary search tree (BST) and a value to 
insert into the tree. Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long 
as the tree remains a BST after insertion. You can return any of them.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        
        cur = root
        while(True):
            if cur.val <= val:
                if cur.right != None:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
            else:
                if cur.left != None:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
                
        return root