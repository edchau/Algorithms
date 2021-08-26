"""
You are given the root of a binary tree where each node 
has a value in the range [0, 25] representing the letters 
'a' to 'z'.

Return the lexicographically smallest string that starts 
at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is 
lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        queue = [(root, "")]
        smallest_string = ""
        while len(queue) > 0:
            node, path = queue.pop(0)
            
            if node:
                cur_path = chr(97+node.val)+path
                if not (node.left or node.right):
                    if smallest_string == "" or cur_path < smallest_string:
                        smallest_string = cur_path
                
                queue.append((node.left, cur_path))
                queue.append((node.right, cur_path))
        
        return smallest_string
    