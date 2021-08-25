"""
Given the root of a binary tree, return the 
sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the 
binary tree, with values 9 and 15 respectively.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        queue = [(root, False)]
        sum_left = 0
        
        while len(queue) > 0:
            node, left = queue.pop(0)
            
            if node:
                if not (node.left or node.right):
                    if left:
                        sum_left += node.val
                else:
                    queue.append((node.left, True))
                    queue.append((node.right, False))
                    
        return sum_left
        