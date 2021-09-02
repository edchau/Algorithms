"""
Given an integer n, break it into the sum of k positive integers, 
where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        possible_int = [i for i in range(1, n)]
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        
        for i in range(n+1):
            for num in possible_int:
                if i + num < n+1:
                    dp[i+num] = max(dp[i+num], num*dp[i])
                    
        return dp[n]