"""
Given a string s, find two disjoint palindromic subsequences 
of s such that the product of their lengths is maximized. The 
two subsequences are disjoint if they do not both pick a character 
at the same index.

Return the maximum possible product of the lengths of the two 
palindromic subsequences.

A subsequence is a string that can be derived from another string 
by deleting some or no characters without changing the order of 
the remaining characters. A string is palindromic if it reads the 
same forward and backward.
"""
class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        palindrome = {} # bitmask -> length
        
        # 1 << n more efficient way to calculate 2 ** n
        # no need to convert pow to this operation
        for mask in range(1, 1 << n):
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    # if true, include char
                    subseq += s[i]
            # calc lengths of bitmasks
            if subseq == subseq[::-1]:
                palindrome[mask] = len(subseq)
        
        # find longest pair of disjoint subseq
        # go thru every pair of bitmasks
        result = 0
        for m1 in palindrome:
            for m2 in palindrome:
                if m1 & m2 == 0:
                    result = max(result, palindrome[m1] * palindrome[m2])
        
        return result