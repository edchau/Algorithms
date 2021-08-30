"""
You are given the root of a binary tree where each node 
has a value 0 or 1.  Each root-to-leaf path represents a 
binary number starting with the most significant bit.  
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then 
this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented 
by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to 
fit in a 32-bits integer.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0)]
        total = 0
        while len(queue) > 0:
            node, path = queue.pop(0)
            
            if node:
                path *= 2
                if not (node.left or node.right):
                    total += path + node.val
                else:
                    queue.append((node.left, path + node.val))
                    queue.append((node.right, path + node.val))
            
        return total 
      
    # def convert_binary(self, binary):
    #     decimal = 0
    #     for digit in binary: 
    #         decimal *= 2 + int(digit)