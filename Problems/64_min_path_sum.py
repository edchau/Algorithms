"""

Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right, which 
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at 
any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                current = dp[i][j]
                
                if i+1 < m:
                    dp[i+1][j] = min(dp[i+1][j], current+grid[i+1][j])
                if j+1 < n:
                    dp[i][j+1] = min(dp[i][j+1], current+grid[i][j+1])
        
        return dp[m-1][n-1]