"""
Given an m x n binary matrix mat, return the distance 
of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(mat)
        n = len(mat[0])
        
        queue = []
        directions = [(1, 0), (0, 1), (0, -1), (-1,0)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    # keep track of unmarked cells
                    mat[i][j] = float('inf')
        
        
        # start from all 0's at once and expand out to find 1
        # then update that matrix cell with the 1
        while len(queue) > 0:
            x, y = queue.pop(0)
            for d in directions:
                new_x = x + d[0]
                new_y = y + d[1]

                # don't update 0 or any values less than current + 1
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or mat[new_x][new_y] <= mat[x][y] + 1:
                    continue
                
                queue.append((new_x, new_y))
                mat[new_x][new_y] = mat[x][y] + 1
                
        return mat