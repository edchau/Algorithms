"""
Given two strings word1 and word2, return the minimum number 
of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

O(nm)
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        
        # Initialize array, how many edits does it take to get from
        # empty string to current substring (inserts)
        for i in range(len(word1)+1):
            dp[i][0] = i
            
        for i in range(len(word2)+1):
            dp[0][i] = i
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        
        return dp[len(word1)][len(word2)]