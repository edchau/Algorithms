/**
 * Given a string columnTitle that represents the column title as appear in 
 * an Excel sheet, return its corresponding column number.
 */
class Solution {
    public int titleToNumber(String columnTitle) {
        if (columnTitle == null) {
            return 0;
        }
        int total = 0;
        for (char c : columnTitle.toUpperCase().toCharArray()) {
            // think of 26 as base 10
            total *= 26;
            total += (c - 'A') + 1;
        }
        return total;
    }
}