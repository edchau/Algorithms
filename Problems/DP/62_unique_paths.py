"""
62. Unique Paths
A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point 
in time. The robot is trying to reach the bottom-right 
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

i.e.
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i+1 < m:
                    dp[i+1][j] += dp[i][j]
                if j+1 < n:
                    dp[i][j+1] += dp[i][j]
        return dp[m-1][n-1]

