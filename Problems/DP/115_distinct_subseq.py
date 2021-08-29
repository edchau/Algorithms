"""
Given two strings s and t, return the number of distinct subsequences of 
s which equals t.

A string's subsequence is a new string formed from the original string by 
deleting some (can be none) of the characters without disturbing the 
remaining characters' relative positions. (i.e., "ACE" is a subsequence of 
"ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        
        for i in range(len(s)+1):
            dp[i][0] = 1
        
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]
