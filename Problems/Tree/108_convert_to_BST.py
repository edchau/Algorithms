"""
Given an integer array nums where the elements are sorted 
in ascending order, convert it to a height-balanced binary 
search tree.

A height-balanced binary tree is a binary tree in which the 
depth of the two subtrees of every node never differs by more than one.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.convert_BST(0, len(nums), nums)
    
    def convert_BST(self, left, right, nums):
        if left == right:
            return None
        mid = (left+right) // 2
        
        node = TreeNode(nums[mid])
        node.left = self.convert_BST(left, mid, nums)
        node.right = self.convert_BST(mid+1, right, nums)
        
        return node