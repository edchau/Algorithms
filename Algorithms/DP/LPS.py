"""
Longest Palindromic Substring

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

O(n^2) Time
O(n^2) Space
"""

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