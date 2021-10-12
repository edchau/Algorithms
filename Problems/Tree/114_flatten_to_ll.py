"""
Given the root of a binary tree, flatten the tree into a 
"linked list":

The "linked list" should use the same TreeNode class where 
the right child pointer points to the next node in the list 
and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order 
traversal of the binary tree.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        node = root
        
        while node != None:
            if node.left:
                pre = node.left
                
                while pre.right:
                    pre = pre.right
                
                # set greatest link to right of subtree
                pre.right = node.right
                # set right pointer to the left to match
                node.right = node.left
                # set left to none (want link list to be going right)
                node.left = None
            
            node = node.right