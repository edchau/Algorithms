"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest 
path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        queue = [(root, 1)]
        
        while len(queue) > 0:
            node, depth = queue.pop(0)
            
            if node:
                if not node.left and not node.right:
                    return depth
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
                
        return 0