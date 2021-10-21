"""
The n-queens puzzle is the problem of placing n queens on 
an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the 
n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the 
n-queens' placement, where 'Q' and '.' both indicate a queen 
and an empty space, respectively.

O(N!)
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self.backtrack([-1]*n, 0, [], res)
        return res
        
    
    def backtrack(self, cols, idx, path, res):
        if idx == len(cols):
            res.append(path)
            return
        
        for i in range(len(cols)):
            # queen i is placed in col idx
            cols[idx] = i
            if self.is_valid(cols, idx):
                place = "." * len(cols)
                self.backtrack(cols, idx+1, path+[place[:i]+"Q"+place[i+1:]], res)
    
    
    def is_valid(self, cols, idx):
        for i in range(idx):
            # [1, 2, 3, 4]
            # if 4 - 1 == 4 - 1
            # diagonals are checked by checking
            # which row the queen should not be in (idx - i) 
            # compared to the queen number (which
            # gives the row)
            # if diagonals or same column
            if abs(cols[i]-cols[idx]) == idx - i or cols[i] == cols[idx]:
                return False
        return True
        