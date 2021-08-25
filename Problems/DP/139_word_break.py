"""
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused 
multiple times in the segmentation.

 
Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be 
segmented as "leet code".
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        
        for i in range(len(s)+1):
            if dp[i]:
                for word in wordDict:
                    if s[i:].find(word) == 0:
                        dp[i+len(word)] = True
                        
        return dp[len(s)]