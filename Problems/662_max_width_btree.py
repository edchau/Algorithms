# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Given a binary tree, write a function to get the maximum 
    width of the given tree. The maximum width of a tree is 
    the maximum width among all levels.

    The width of one level is defined as the length between 
    the end-nodes (the leftmost and right most non-null nodes 
    in the level, where the null nodes between the end-nodes 
    are also counted into the length calculation.

    It is guaranteed that the answer will in the range of 
    32-bit signed integer.
    """
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        count = 0
        depth_pos = {}
        
        def dfs(node, depth = 0, pos = 0):
            nonlocal count
            if node:
                depth_pos.setdefault(depth, pos)
                count = max(count, pos - depth_pos[depth] + 1)
                dfs(node.left, depth+1, pos * 2)
                dfs(node.right, depth+1, pos * 2 + 1)
        dfs(root)
        return count