/**
 * You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the 
ending square, that walk over every non-obstacle square exactly once.
 */
class Solution {
    
    private int total = 0;
    
    public int uniquePathsIII(int[][] grid) {
        int total = 0;
        int startX = 0;
        int startY = 0;

        for (int i = 0; i < grid.length; ++i) {
            for (int j = 0; j < grid[i].length; ++j) {
                if (grid[i][j] == 0) {
                    total += 1;
                } else if (grid[i][j] == 1) {
                    startX = i;
                    startY = j;
                }
            }
        }
        dfs(grid, startX, startY, total);
        return this.total;
    }
    
    public void dfs(int[][] grid, int x, int y, int total) {
        // mark 3 as visited
        int[][] directions = new int[][]{{1,0}, {0,1}, {-1,0}, {0,-1}};
        if (grid[x][y] == 2 && total == -1) {
            this.total += 1;
        }
        if (grid[x][y] == 2 && total != 0) {
            return;
        }
        
        int store = grid[x][y];
        grid[x][y] = 3;
        
        for (int[] d : directions) {
            int newX = x + d[0];
            int newY = y + d[1];
            if (newX < 0 || newX >= grid.length || newY < 0 || newY >= grid[0].length) {
                continue;
            }
            if (grid[newX][newY] != 3 && grid[newX][newY] != -1) {
                dfs(grid, newX, newY, total-1);
            }
        }
        grid[x][y] = store;
        
    }
}