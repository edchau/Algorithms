"""
Given the root of a binary tree, return the level order 
traversal of its nodes' values. (i.e., from left to right, 
level by level).

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [(root, 0)]
        order = []
        
        while len(queue) > 0:
            node, depth = queue.pop()
            
            if node:
                if len(order) == depth:
                    order.append([])
                
                order[depth] += [node.val]
                
                queue.append((node.right, depth+1))
                queue.append((node.left, depth+1))
                
        return order