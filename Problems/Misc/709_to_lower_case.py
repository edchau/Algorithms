"""
Given a string s, return the string after replacing 
every uppercase letter with the same lowercase letter.
"""

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = []
        for ch in s:
            if ord(ch) <= 90 and ord(ch) >= 65:
                word.append(chr(ord(ch) + 32))
            else:
                word.append(ch)
            
        return "".join(word)