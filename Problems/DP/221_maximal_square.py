"""
Given an m x n binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return 
its area.
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for i in range(rows):
            for j in range(cols):
                # each cell represents how the largest square that
                # can be made up to that cell, (each of the cells above, left, and diag
                # must be at least 1's so we get the minimum value)
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                # this will count the max side length we get
                max_side = max(max_side, dp[i][j])
                
        return max_side ** 2