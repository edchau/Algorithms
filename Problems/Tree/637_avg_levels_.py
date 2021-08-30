"""
Given the root of a binary tree, return the average 
value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        rows = []
        queue = [(root, 0)]
        while len(queue) > 0:
            node, depth = queue.pop(0)
            
            if node:
                if depth == len(rows):
                    rows.append([node.val])
                else:
                    rows[depth].append(node.val)
                
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
    
        averages = []
        for row in rows:
            averages.append(sum(row) / (float(len(row))))
        return averages
        