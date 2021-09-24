"""
Given an array nums of integers, we need to find 
the maximum possible sum of elements of the array 
such that it is divisible by three.
"""

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * 3
        
        for n in nums:
            for i in dp[:]:
                dp[(i + n) % 3] = max(dp[(i + n) % 3], i + n)
        
        return dp[0]