"""
Given the root of a binary search tree, rearrange the tree in 
in-order so that the leftmost node in the tree is now the root 
of the tree, and every node has no left child and only one right child.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        stack = []
        
        new_node = TreeNode()
        new_tree = new_node
        
        prev = None
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            # new_node.val = root.val
            new_node.right = TreeNode(root.val)
            new_node = new_node.right
            
            root = root.right
        
        return new_tree.right
            
            