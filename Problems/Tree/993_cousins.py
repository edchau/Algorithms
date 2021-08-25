"""
Given the root of a binary tree with unique values and the values of two 
different nodes of the tree x and y, return true if the nodes corresponding 
to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with 
different parents.

Note that in a binary tree, the root node is at the depth 0, and children of 
each depth k node are at the depth k + 1.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        queue = [(root, 1, 0)]
        depth_found = 0
        parent_found = 0
        while len(queue) > 0:
            node, depth, parent = queue.pop(0)
            
            if node.val == x or node.val == y:
                if depth_found == depth and parent != parent_found:
                    return True
                depth_found = depth
                parent_found = parent
            
            if node:
                if node.left:
                    queue.append((node.left, depth+1, node.val))
                if node.right:
                    queue.append((node.right, depth+1, node.val))
        
        return False