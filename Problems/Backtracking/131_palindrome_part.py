"""
Given a string s, partition s such that every substring of the 
partition is a palindrome. Return all possible palindrome 
partitioning of s.

A palindrome string is a string that reads the same backward as 
forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.backtrack(s, 0, [], result)
        return result
    
    def backtrack(self, s, idx, path, res):
        if idx >= len(s):
            res.append(path)
            return
        end = 1
        while idx + end <= len(s):
            cur = s[idx:(idx+end)]
            if cur == cur[::-1]:
                self.backtrack(s, idx+end, path+[cur], res)
            end += 1