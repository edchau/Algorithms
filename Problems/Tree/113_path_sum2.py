"""
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node 
values in the path equals targetSum. Each path should be
returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and 
ending at any leaf node. A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        queue = [(root, 0, [])]
        paths = []
        while len(queue) > 0:
            node, val, path = queue.pop(0)
            
            if node:
                if not (node.left or node.right):
                    if val + node.val == targetSum:
                        paths.append(path + [node.val])
            
                queue.append((node.left, val + node.val, path + [node.val]))
                queue.append((node.right, val + node.val, path + [node.val]))
        
        return paths