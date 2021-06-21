# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    687. Longest Univalue Path
    Given a binary tree, find the length of the longest path where each node in the path has the same value. 
    This path may or may not pass through the root.
    The length of path between two nodes is represented by the number of edges between them.
              1
             / \
            4   5
           / \   \
          4   4   5
          Output: 2
    """
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.count = 0
        
        def find_longest(node):
            if not node:
                return 0
            left_path = find_longest(node.left)
            right_path = find_longest(node.right)
            left = right = 0
            
            if node.left and node.val == node.left.val:
                left = left_path + 1
            if node.right and node.val == node.right.val:
                right = right_path + 1
            self.count = max(self.count, left + right)
            # return max(left, right)
        
        
        find_longest(root)
        return self.count