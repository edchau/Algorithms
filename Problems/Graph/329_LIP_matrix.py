"""
Given an m x n integers matrix, return the length of the 
longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, 
up, or down. You may not move diagonally or move outside the boundary 
(i.e., wrap-around is not allowed).
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == 0:
            return 0
        
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        in_degree = [[0] * cols for _ in range(rows)] 
        
        for x in range(rows):
            for y in range(cols):
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] < matrix[x][y]:
                            in_degree[x][y] += 1
                            
        queue = []
        for x in range(rows):
            for y in range(cols):
                if in_degree[x][y] == 0:
                    queue.append((x, y))
        
        path = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                x, y = queue.pop(0)
                for direction in directions:
                    nx, ny = x + direction[0], y+direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] > matrix[x][y]:
                            in_degree[nx][ny] -= 1
                            if in_degree[nx][ny] == 0:
                                queue.append((nx, ny))
            path += 1
        return path
                
                