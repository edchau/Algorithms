"""
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order 
traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf 
value in its left and right subtree, respectively.

Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.
"""

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [float('inf')]
        result = 0
        
        for val in arr:
            # while the peek is less than current,
            # add that to result (pair two lowest vals)
            # since branches are in order
            while stack[-1] <= val:
                top = stack.pop()
                result += top * min(val, stack[-1])
            stack.append(val)
        
        while len(stack) > 2:
            result += stack.pop() * stack[-1]
        return result
        