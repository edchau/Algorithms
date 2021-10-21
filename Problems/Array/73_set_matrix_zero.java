/**
 * Given an m x n integer matrix matrix, if an element is 0, 
 * set its entire row and column to 0's, and return the matrix.
You must do it in place.
 * 
 */

class Solution {
    public void setZeroes(int[][] matrix) {
        // use first cell in row/column to indicate if we need to change to 0
        int row = matrix.length;
        int col = matrix[0].length;
        
        // keep track if whether or not first row and column need to be set to 0
        // since we're using the first row and col itself as a flag
        boolean firstCol = false;
        boolean firstRow = false;
        
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (matrix[i][j] == 0) {
                    if (i == 0) {
                        firstRow = true;
                    }
                    if (j == 0) {
                        firstCol = true;
                    }
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        
        // handle rows and columns separately
        for (int i = 1; i < row; ++i) {
            for (int j = 1; j < col; ++j) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
        }
        
        for (int i = 1; i < col; ++i) {
            if (matrix[0][i] == 0) {
                for (int j = 0; j < row; ++j) {
                    matrix[j][i] = 0;
                }
            }
        }
        
        // update first row and first column
        if (firstCol) {
            for (int i = 0; i < row; ++i) {
                matrix[i][0] = 0;
            }
        }
        if (firstRow) {
            for (int i = 0; i < col; ++i) {
                matrix[0][i] = 0;
            }
        }
        
        
    }
}