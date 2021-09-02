"""
On an n x n chessboard, a knight starts at the cell 
(row, column) and attempts to make exactly k moves. 
The rows and columns are 0-indexed, so the top-left 
cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, 
as illustrated below. Each move is two cells in a 
cardinal direction, then one cell in an orthogonal direction.
"""
class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        dp = [[0]*n for _ in range(n)]
        moves = [(-2,1), (2,1), (2,-1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        
        dp[row][column] = 1
        for _ in range(k):
            # ensure current dp prob is not overwritten
            temp = [[0]*n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for m in moves:
                            new_row = r + m[0]
                            new_col = c + m[1]
                            if new_row >= 0 and new_col >= 0 and new_row < n and new_col < n:
                                temp[new_row][new_col] += dp[r][c] / 8.0
            dp = temp
        
    
        prob = 0.0
        for r in range(n):
            for c in range(n):
                prob += dp[r][c]
        return prob