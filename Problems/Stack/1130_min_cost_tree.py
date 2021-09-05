"""
Among all possible binary trees considered, return the 
smallest possible sum of the values of each non-leaf node. 
It is guaranteed this sum fits into a 32-bit integer.

Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has 
non-leaf node sum 32.
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
            while stack[-1] <= val:
                top = stack.pop()
                result += top * min(val, stack[-1])
            stack.append(val)
        while len(stack) > 2:
            result += stack.pop() * stack[-1]
        return result
        