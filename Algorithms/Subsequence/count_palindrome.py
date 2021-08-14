"""
647. Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

O(n^2) Time
O(1) Space
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        
        for i in range(len(s)):
            # palindrome is odd length
            left, right = i, i
            count += self.count_palindromes(left, right, s)
                
            # palindrome is even length:
            """
            Input: s = "cbbd"
            Output: "bb"
            """
            left, right = i, i+1
            count += self.count_palindromes(left, right, s)
                
        return count
    
    def count_palindromes(self, left, right, s):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # Start from middle and expand outward
            count += 1
            left -= 1
            right += 1
            
        return count
            