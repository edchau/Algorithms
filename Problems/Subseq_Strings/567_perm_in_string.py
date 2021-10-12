"""
Given two strings s1 and s2, return true if s2 contains a 
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is 
the substring of s2.

"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        count = [0] * 26
        
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
        
        # sliding window of length s1
        for i in range(len(s2)):
            count[ord(s2[i]) - ord('a')] -= 1
            
            if i - len(s1) >= 0:
                count[ord(s2[i - len(s1)]) - ord('a')] += 1
            if self.check_zero(count):
                return True
            
        return False
    
    def check_zero(self, count):
        for val in count:
            if val != 0:
                return False
        return True