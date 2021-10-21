/**
 * Return the maximum total sum that the height of the buildings can be 
 * increased by without changing the city's skyline from any cardinal direction.
 * 
 */
class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int n = grid.length;
        int[] col = new int[n];
        int[] row = new int[n];
        // max for every row and every col
        // max will be highest skyline from 2d direction
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                row[i] = Math.max(row[i], grid[i][j]);
                col[j] = Math.max(col[j], grid[i][j]);
            }
        }
        
        int result = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                result += Math.min(row[i], col[i]) - grid[i][j];
            }
        }
        
        return result;
    }
}