"""
You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty 
substrings such that the numerical values of the substrings 
are in descending order and the difference between numerical 
values of every two adjacent substrings is equal to 1.

For example, the string s = "0090089" can be split into 
["0090", "089"] with numerical values [90,89]. The values are 
in descending order and adjacent values differ by 1, so this way is valid.
Another example, the string s = "001" can be split into 
["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are 
invalid because they have numerical values [0,1], [0,1], and [0,0,1] 
respectively, all of which are not in descending order.
Return true if it is possible to split s​​​​​​ as described above, or false 
otherwise.

A substring is a contiguous sequence of characters in a string.
"""

class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.dfs(s, 0, [])
        
        
    def dfs(self, s, idx, path):
        if idx == len(s) and len(path) >= 2:
            return True
            
        res = False
        for i in range(idx, len(s)):
            if s[idx:i+1] == "":
                continue
            num = int(s[idx:i+1])
            # skip 0's in the middle of a number
            if num == 0 and i < len(s)-1:
                continue
            
            if len(path) == 0 or path[-1] - num == 1:
                res = res or self.dfs(s, i+1, path+[num])
        
        return res