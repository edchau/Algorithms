"""
Given a binary tree, find the lowest common ancestor (LCA) 
of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The 
lowest common ancestor is defined between two nodes p 
and q as the lowest node in T that has both p and q as
 descendants (where we allow a node to be a descendant 
 of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.find_LCA(root, p, q)
    
    def find_LCA(self, node, p, q):
        if node == None:
            return None
        
        if node.val == p.val or node.val == q.val:
            return node
    
        left = self.find_LCA(node.left, p, q)
        right = self.find_LCA(node.right, p, q)
        
        if left != None and right != None:
            return node
        
        if left != None:
            return left
        
        if right != None:
            return right
        
        return None
        
        
        
        
        