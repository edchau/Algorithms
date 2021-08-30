"""
Given two strings s and t of lengths m and n respectively, return 
the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. If there is no 
such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 
'C' from string t.
"""



import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        right = 0
        
        min_window = ""
        min_len = float('inf')
        count = 0
        
        counter = collections.Counter(t)
        counter_search = collections.defaultdict(int)
        
        while right < len(s):
            counter_search[s[right]] += 1
            if s[right] in counter:
                if counter_search[s[right]] <= counter[s[right]]:
                    count += 1
            
            while left <= right and count == len(t):
                # check if this would be min window
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    min_window = s[left: right+1]
                
                # move left pointer, if no longer satisfies, remove 1 from count
                counter_search[s[left]] -= 1
                if s[left] in counter and counter_search[s[left]] < counter[s[left]]:
                    count -= 1
                
                left += 1
        
            right += 1
            
        return min_window