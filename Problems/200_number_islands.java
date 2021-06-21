class Solution {
    public int numIslands(char[][] grid) {
        /**
        Given a 2d grid map of '1's (land) and '0's (water), 
        count the number of islands. An island is surrounded 
        by water and is formed by connecting adjacent lands 
        horizontally or vertically. You may assume all four 
        edges of the grid are all surrounded by water.
        **/

        if (grid.length == 0) {
            return 0;
        }
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int count = 0;
        
        for (int i = 0; i < grid.length; ++i) {
            for (int j = 0; j < grid[i].length; ++j) {
                if (!visited[i][j] && grid[i][j] == '1') {
                    count += 1;
                    dfs(i, j, visited, grid);
                }
            }
        }
        return count;
    }

    public void dfs(int i, int j, boolean[][] visited, char[][] grid) {
        visited[i][j] = true;
        int[] rowShift = {-1,0,1,0};
        int[] colShift = {0,-1,0,1};
        for (int k = 0; k < 4; ++k) {
            if (checkBounds(i+rowShift[k], j+colShift[k], visited, grid)) {
                dfs(i+rowShift[k], j+colShift[k], visited, grid);
            }
        }
    }
    
    public boolean checkBounds(int i, int j, boolean[][] visited, char[][] grid) {
        return (i >= 0 && j >= 0 
                && i < visited.length 
                && j < visited[0].length
                && !visited[i][j]
                && grid[i][j] == '1');   
    }
}