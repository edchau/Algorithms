"""
Given an array of non-negative integers arr, you are initially 
positioned at start index of the array. When you are at index i, 
you can jump to i + arr[i] or i - arr[i], check if you can reach 
to any index with value 0.

Notice that you can not jump outside of the array at any time.
"""

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if start >= 0 and start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start] # mark as visited
            return arr[start] == 0 or self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
        return False