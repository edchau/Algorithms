"""
A robot is located at the top-left corner of a m x n 
grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point 
in time. The robot is trying to reach the bottom-right 
corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. 
How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in 
the grid.
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i + 1 < m:
                    dp[i+1][j] += dp[i][j]
                    
                if j + 1 < n:
                    dp[i][j+1] += dp[i][j]

        return dp[m-1][n-1]
