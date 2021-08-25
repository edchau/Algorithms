"""
Given the root of a binary tree, return all root-to-leaf 
paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        queue = [(root, str(root.val))]
        
        paths = []
        while len(queue) > 0:
            node, path = queue.pop(0)
            
            if node:
                if not(node.left or node.right):
                    paths.append(path)
                
                if node.left:
                    queue.append((node.left, path + "->" + str(node.left.val)))
                if node.right:
                    queue.append((node.right, path + "->" + str(node.right.val)))
        
        return paths
        