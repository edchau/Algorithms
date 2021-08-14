"""
Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest 
common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original 
string with some characters (can be none) deleted without changing the 
relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to 
both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.


Idea:
If the characters match, remove both from the string
If don't match, check for the max between removing one chracter (j-1)
or the other (i-1)
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else: 
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[len(text1)][len(text2)]

    def LCS_memo(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        return self.LCS(text1, text2, len(text1), len(text2), {})

    def LCS(self, text1, text2, i, j, memo):
        key = (i, j)
        if (key in memo):
            return memo[key]
        if i == 0 or j == 0:
            return 0
        elif text1[i-1] == text2[j-1]:
            memo[key] = 1 + self.LCS(text1, text2, i-1, j-1, memo)
            return memo[key]
        else:
            memo[key] = max(self.LCS(text1, text2, i-1, j, memo), self.LCS(text1, text2, i, j-1, memo))
            return memo[key]