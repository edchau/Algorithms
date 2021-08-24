"""
Given an integer n, return the least number of perfect
square numbers that sum to n.

A perfect square is an integer that is the square of an 
integer; in other words, it is the product of some integer 
with itself. For example, 1, 4, 9, and 16 are perfect squares 
while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
"""

import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        dp[1] = 1
        
        for i in range(1, n+1):
            sqrt = (int) (math.sqrt(i))
            
            if sqrt*sqrt == i:
                dp[i] = 1
                continue
            
            for num in range(1, sqrt+1):
                coin = num ** 2
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin]+1)
        
        return dp[n]