/**
 * On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented 
 * by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the 
board is solved. If it is impossible for the state of the board to be solved, return -1.
 * 
 */
class Solution {
    
    private String end;
    private int minMoves;
    
    public int slidingPuzzle(int[][] board) {
        end = Arrays.deepToString(new int[][] {{1, 2, 3}, {4, 5, 0}});
        minMoves = Integer.MAX_VALUE;
        if (!dfs(board, new HashMap<>(), 0)) {
            return -1;
        }
        return this.minMoves;
    }
    
    public boolean dfs(int[][] board, HashMap<String, Integer> boards, int moves) {
        String curBoard = Arrays.deepToString(board);
        // System.out.println(curBoard);
        if (boards.containsKey(curBoard)) {
            if (moves > boards.get(curBoard)) {
                return false;
            }
        }
        if (curBoard.equals(this.end)) {
            minMoves = Math.min(minMoves, moves);
            boards.put(curBoard, moves);
            return true;
        }
        boards.put(curBoard, moves);
        
        int[][] directions = new int[][]{{1,0}, {0,1}, {-1,0}, {0,-1}};
        
        boolean solvable = false;
        
        for (int i = 0; i < board.length; ++i) {
            for (int j = 0; j < board[0].length; ++j) {
                for (int[] dir : directions) {
                    int dx = i + dir[0];
                    int dy = j + dir[1];
                    if (dx < 0 || dy < 0 || dx >= board.length || dy >= board[0].length || board[dx][dy] != 0) {
                        continue;
                    }
                    int temp = board[i][j];
                    board[i][j] = 0;
                    board[dx][dy] = temp;
                    
                    if (dfs(board, boards, moves + 1)) {
                        solvable = true;
                    }
                    
                    board[dx][dy] = 0;
                    board[i][j] = temp;
                }
            }
        }
        return solvable;
    }
}