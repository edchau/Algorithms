"""
Given the root of a binary tree, return the lowest common ancestor of 
its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, 
the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with 
the largest depth such that every node in S is in the subtree with root A.
Note: This question is the same as 865: 
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.find_deepest_LCA(root, 0)[0]
    
    
    def find_deepest_LCA(self, root, depth):
        if not root:
            return root, depth
        
        left, left_depth = self.find_deepest_LCA(root.left, depth+1)
        right, right_depth = self.find_deepest_LCA(root.right, depth+1)
        
        if left_depth > right_depth:
            return left, left_depth
        elif right_depth > left_depth:
            return right, right_depth
        
        # equal depths (LCA since this is the condition for deepest node)
        # otherwise, we return the subtree that has a deeper node
        return root, left_depth