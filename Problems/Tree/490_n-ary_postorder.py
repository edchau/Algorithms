"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        traversal = []
        self.bfs(root, traversal)
        return traversal
    
    def bfs(self, root, traversal):
        if root == None:
            return
        if root.children == None:
            traversal.append(root.val)
            return
        
        for child in root.children:
            self.bfs(child, traversal)
        
        traversal.append(root.val)