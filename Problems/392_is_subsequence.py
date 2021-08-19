# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from
# the original string by deleting some (can be none) of the 
# characters without disturbing the relative positions of the 
# remaining characters. (ie, "ace" is a subsequence of "abcde" 
# while "aec" is not).

# Input: s = "abc", t = "ahbgdc"
# Output: true

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for char in t:
            if len(s) > 0 and char == s[0]:
                s = s[1:]
            
        return len(s) == 0
            
        