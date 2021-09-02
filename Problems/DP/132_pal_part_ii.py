"""
Given a string s, partition s such that every 
substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome 
partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] 
could be produced using 1 cut.
"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        
        
        dp = [[False for j in range(len(s))]  for i in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            res = s[i]
            
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
        
        min_cut = [0] * len(s)
        
        for j in range(1, len(s)):
            # s[:j] does not require cut if palindrome
            if dp[0][j]:
                min_cut[j] = 0
            else:
                min_val = float('inf')
                for i in range(j, 0, -1):
                    # go down column, if pal, check the
                    # subproblem before and add 1
                    if dp[i][j]:
                        if min_cut[i-1] < min_val:
                            min_val = min_cut[i-1]
                min_cut[j] = min_val + 1
        return min_cut[len(s)-1]
