"""
Longest Palindromic Substring

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

O(n^2) Time
O(1) Space
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        for i in range(len(s)):
            
            # palindrome is odd length
            left, right = i, i
            res = self.find_longest_palindrome(left, right, s, res)
                
            # palindrome is even length:
            left, right = i, i+1
            res = self.find_longest_palindrome(left, right, s, res)
                
        return res
    
    def find_longest_palindrome(self, left, right, s, res):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # Start from middle and expand outward
            if right - left + 1 > len(res):
                res = s[left:right+1]
            left -= 1
            right += 1
            
        return res
            