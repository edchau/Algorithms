"""
Longest Palindromic Substring

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

O(n^2) Time
O(1) Space
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        for i in range(len(s)):
            
            # palindrome is odd length
            left, right = i, i
            res = self.find_longest_palindrome(left, right, s, res)
                
            # palindrome is even length:
            left, right = i, i+1
            res = self.find_longest_palindrome(left, right, s, res)
                
        return res
    
    def find_longest_palindrome(self, left, right, s, res):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # Start from middle and expand outward
            if right - left + 1 > len(res):
                res = s[left:right+1]
            left -= 1
            right += 1
            
        return res



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        
        dp = [[False for j in range(len(s))]  for i in range(len(s))]
        res = ""
        
        # Length of 1 Palindrome
        for i in range(len(s)):
            dp[i][i] = True
            res = s[i]
            
        # if we start from end, we can build table from
        # simplest case and build up since the ind at
        # i, j depends on i+1, j-1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                # compare start and end
                if s[i] == s[j]:
                    # if chars in between is 1 or the
                    # calculated substr in between
                    # is already a palindrome
                    if j - i == 1 or dp[i+1][j-1]:
                        if j - i + 1 > len(res):
                            res = s[i:j+1]
                        dp[i][j] = True
        
        
        return res


"""
class Solution {
    public String longestPalindrome(String s) {
        String result = "";
        
        for (int i = 0; i < s.length(); ++i) {
            String longest = findPalindrome(s, i);
            
            if (longest.length() > result.length()) {
                result = longest;
            }
            
        }
        
        return result;
    }
    
    public String findPalindrome(String s, int ind) {
        
        // even
        int left = ind;
        int right = ind;
        
        String odd = "";
        while (left >= 0 && right < s.length()) {
            if (s.charAt(left) != s.charAt(right)) {
                break;
            }
            odd = s.substring(left, right+1);
            left -= 1;
            right += 1;
        }
        
        
        // odd
        left = ind;
        right = ind+1;
        
        String even = "";
        while (left >= 0 && right < s.length()) {
            if (s.charAt(left) != s.charAt(right)) {
                break;
            }
            even = s.substring(left, right+1);
            left -= 1;
            right += 1;
        }
        
        if (even.length() > odd.length()) {
            return even;
        }
        
        return odd;
    }
}

"""