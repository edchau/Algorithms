/**
 * Given a string s, determine if it is a palindrome, considering 
 * only alphanumeric characters and ignoring cases.
 */

class Solution {
    public boolean isPalindrome(String s) {
        String clean = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
        int head = 0;
        int tail = clean.length() - 1;
        
        while (head < tail) {
            if (clean.charAt(head) != clean.charAt(tail)) {
                return false;
            }
            head += 1;
            tail -= 1;
        }
        
        return true;
    }
}