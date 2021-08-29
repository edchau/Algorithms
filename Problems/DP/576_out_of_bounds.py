"""
There is an m x n grid with a ball. The ball is initially at the position 
[startRow, startColumn]. You are allowed to move the ball to one of the 
four adjacent cells in the grid (possibly out of the grid crossing the grid 
boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the 
number of paths to move the ball out of the grid boundary. Since the answer 
can be very large, return it modulo 109 + 7.
"""
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        count = 0
        dp[startRow][startColumn] = 1
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for _ in range(maxMove):
            # to make sure current values are not overwritten
            temp_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for dx, dy in directions:
                        x_new, y_new = i + dx, j + dy
                        if x_new >= 0 and x_new < m and y_new >= 0 and y_new < n:
                            temp_dp[i][j] += dp[x_new][y_new]
                        else:
                            count += dp[i][j]
            dp = temp_dp
        
        return count % (10**9 + 7)