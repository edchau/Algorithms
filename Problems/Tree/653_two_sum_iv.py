"""
Given the root of a Binary Search Tree and a target number k, 
return true if there exist two elements in the BST such that
their sum is equal to the given target.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = [root]
        
        complements = set()
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                comp = k - node.val
                if comp in complements:
                    return True
                complements.add(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        return False