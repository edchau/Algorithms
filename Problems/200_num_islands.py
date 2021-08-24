"""
Given an m x n 2D binary grid grid which represents a map of 
'1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    self.bfs(grid, visited, (i,j))
                    count += 1
        return count
                
        
    def bfs(self, grid, visited, start):
        queue = [start]
        visited[start[0]][start[1]] = True
        directions = [(1, 0), (0, 1), (0, -1), (-1,0)]
        
        while len(queue) > 0:
            pos = queue.pop(0)
            
            for d in directions:
                x_new = pos[0] + d[0]
                y_new = pos[1] + d[1]
                if self.check_bounds(grid, x_new, y_new):
                    if not visited[x_new][y_new] and grid[x_new][y_new] == "1":
                        queue.append((x_new, y_new))
                        visited[x_new][y_new] = True
                                 
    def check_bounds(self, grid, x, y):
        return x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0
                                     
                                     