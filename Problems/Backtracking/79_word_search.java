/**
 * Given an m x n grid of characters board and a string word, return 
 * true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same 
letter cell may not be used more than once.
 * 
 */

// O(m*n*4L) where L is length of word
class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; ++i) {
            for (int j = 0; j < board[0].length; ++j) {
                if (word.charAt(0) == board[i][j]) {
                    if (dfs(board, word, i, j, 0)) {
                        return true;
                    }   
                }
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, String word, int i, int j, int ind) {
        if (word.length() == ind) {
            return true;
        }
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(ind)) {
            return false;
        }
        
        int[][] directions = new int[][]{{1,0}, {0,1}, {-1,0}, {0,-1}};
        char c = board[i][j];
        board[i][j] = ' ';
        boolean found = false;
        for (int[] dir : directions) {
            int dx = i + dir[0];
            int dy = j + dir[1];
            found = found || dfs(board, word, dx, dy, ind+1);   
        }
        board[i][j] = c;
        return found;
    }
}