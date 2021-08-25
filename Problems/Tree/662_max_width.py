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
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 1, 1)]
        
        left_most_node = {1: 1}
        
        width = 1
        
        while len(queue) > 0:
            node, pos, depth = queue.pop(0)

            if node:
                if depth not in left_most_node:
                    left_most_node[depth] = pos

                queue.append((node.left, pos*2, depth + 1))
                queue.append((node.right, pos*2+1, depth + 1))
                width = max(width, pos - left_most_node[depth] + 1)

        return width