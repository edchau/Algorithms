"""
Given an integer n, return the number of structurally unique BST's 
(binary search trees) which has exactly n nodes of unique values from 1 to n.
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for root in range(1, i+1):
                nums_left = root - 1
                nums_right = i - root
                dp[i] += dp[nums_left] * dp[nums_right]
        return dp[n]
        
        
#         dp = [1]
#         for i in range(1, n+1):
            

#         if n <= 1:
#             return 1
        
#         total = 0
#         for root in range(1, n+1):
#             num_left = root - 1
#             num_right = n - root
#             total += self.numTrees(num_left) * self.numTrees(num_right)
            
#         return total

        
        