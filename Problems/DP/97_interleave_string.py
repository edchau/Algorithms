"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving 
of s1 and s2.

An interleaving of two strings s and t is a configuration where they are 
divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        m = len(s1)
        n = len(s2)
        
        return self.dp(0, 0, m, n, s1, s2, s3, {})
        
    
    def dp(self, i, j, m, n, s1, s2, s3, memo):
        key = (i, j)
        if i == m and j == n:
            return True
        if key in memo:
            return memo[key]
        
        found = False
        if i < m and s1[i] == s3[i+j]:
            found |= self.dp(i+1, j, m, n, s1, s2, s3, memo)
        
        if j < n and s2[j] == s3[i+j]:
            found |= self.dp(i, j+1, m, n, s1, s2, s3, memo)
        
        memo[key] = found
        
        return memo[key]
        