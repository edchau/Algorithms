"""
Given a string s and a dictionary of strings wordDict, add 
spaces in s to construct a sentence where each word is a valid 
dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple 
times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [[] for _ in range(len(s)+1)]
        dp[0] = [""]
        
        for i in range(len(s)+1):
            for word in wordDict:
                if s[i:].find(word) == 0:
                    dp[i+len(word)] += [c + " " + word if len(c) > 0 else word for c in dp[i]]
        return dp[len(s)]


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.word_break_help(s, wordDict, {})
        
    def word_break_help(self, target, words, memo):
        if target in memo:
            return memo[target]
        
        if target == '':
            return [""]
        
        result = []
        
        for word in words:
            if target.find(word) == 0:
                suffix = target[len(word):]
                combinations = self.word_break_help(suffix, words, memo)
                target_comb = [word + " " + c if len(c) > 0 else word for c in combinations]
                result += target_comb
        
        memo[target] = result
        return result