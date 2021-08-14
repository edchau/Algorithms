"""
647. Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

O(n^2) Time
O(n^2) Space
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False for j in range(len(s))]  for i in range(len(s))]
        count = len(s)
        
        # Length of 1 Palindrome
        for i in range(len(s)):
            dp[i][i] = True
            
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
                        count += 1
                        dp[i][j] = True
        
        return count