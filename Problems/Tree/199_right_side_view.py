"""
Given the root of a binary tree, imagine yourself standing on 
the right side of it, return the values of the nodes you can see 
ordered from top to bottom.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        right_side = []
        self.traverse_right(root, right_side, 0)
        return right_side
    
    def traverse_right(self, node, right_side, depth):
        if node:
            if len(right_side) == depth:
                right_side.append(node.val)
            
            self.traverse_right(node.right, right_side, depth+1)
            self.traverse_right(node.left, right_side, depth+1)