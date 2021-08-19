"""
Longest Substring Without Repeating Characters

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        start = 0
        max_len = 0
        count = 0
        
        for i, char in enumerate(s):
            if char not in letters:
                count += 1
            else:
                if letters[char] >= start:
                    start = letters[char] + 1
                    count = (i - start) + 1
                else:
                    count += 1
            
            max_len = max(max_len, count)
            letters[char] = i
            
        return max_len