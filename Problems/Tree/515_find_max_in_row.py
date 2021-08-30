"""
Given the root of a binary tree, return an array of the 
largest value in each row of the tree (0-indexed).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        queue = [(root, 0)]
        row_max = [float('-inf')]
        
        while len(queue) > 0:
            node, depth = queue.pop(0)
            
            if node:
                if depth == len(row_max):
                    row_max.append(float('-inf'))
                row_max[depth] = max(row_max[depth], node.val)
                
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
                
        return row_max
                    
                