"""
You are given the root of a binary tree. We 
install cameras on the tree nodes where each 
camera at a node can monitor its parent, itself, 
and its immediate children.

Return the minimum number of cameras needed to monitor
all nodes of the tree.

 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.val = 0
        return (self.dfs(root) == 0) + self.val
        
    
    # Greedy DFS
    # 0: leaf
    # 1: parent of a leaf, with a camera on this node.
    # 2: covered without camera on node
    def dfs(self, root):
        if root == None:
            return 2
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if left == 0 or right == 0:
            self.val += 1
            return 1
        
        if left == 1 or right == 1:
            return 2
        else:
            return 0

        