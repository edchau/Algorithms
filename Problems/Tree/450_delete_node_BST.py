"""
Given a root node reference of a BST and a key, delete the node 
with the given key in the BST. Return the root node reference 
(possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)?

 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        if root.val == key:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, root.val)
 
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        return root
    
    def find_min(self, root):
        while root.left:
            root = root.left
        return root