class Solution(object):
    """
    Longest Palindromic Substring

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(m) >= j-i:
                    break
                elif s[i:j][::-1] == s[i:j]:
                    m = s[i:j]
        return m