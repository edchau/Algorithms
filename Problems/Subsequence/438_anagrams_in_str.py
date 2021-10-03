"""
Given two strings s and p, return an array of all the start 
indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original letters 
exactly once.
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s1 = p
        s2 = s
        if len(s1) > len(s2):
            return []
        
        count = [0] * 26
        
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
        
        # sliding window of length s1
        starts = []
        for i in range(len(s2)):
            count[ord(s2[i]) - ord('a')] -= 1
            
            if i - len(s1) >= 0:
                count[ord(s2[i - len(s1)]) - ord('a')] += 1
            if self.check_zero(count):
                starts.append(i - len(s1) + 1)
            
        return starts
    
    def check_zero(self, count):
        for val in count:
            if val != 0:
                return False
        return True