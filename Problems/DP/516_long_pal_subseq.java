/**
 * Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by 
deleting some or no elements without changing the order of the remaining elements.
 * 
 */

class Solution {
    
    private HashMap<String, Integer> memo;
    
    public int longestPalindromeSubseq(String s) {
        memo = new HashMap<>();
        int i = 0;
        int j = s.length()-1;
        return findLPS(s, i, j);
    }
    
    public int findLPS(String s, int i, int j) {
        String key = s.substring(i, j+1);
        
        // base case
        if (i == j) {
            return 1;
        }
        if (i > j) {
            return 0;
        }
        
        // memo
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        
        int longest = 0;
        if (s.charAt(i) == s.charAt(j)) {
            longest = findLPS(s, i+1, j-1) + 2;
        } else {
            longest = Math.max(findLPS(s, i+1, j), findLPS(s, i, j-1));
        }
        
        memo.put(key, longest);
        return memo.get(key);
    }
}