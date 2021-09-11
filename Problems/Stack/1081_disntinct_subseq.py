"""
Return the lexicographically smallest subsequence of s that 
contains all the distinct characters of s exactly once.

Note: This question is the same as 316: 
https://leetcode.com/problems/remove-duplicate-letters/
"""
class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # monotonic increasing stack
        stack = []
        
        # right most index, no need to remove
        # value if it is already right most index
        # since we want all distinct values
        ind = {}
        
        # track current window
        curr = set()
        # right most ind
        for i, ch in enumerate(s):
            ind[ch] = i

        for i, ch in enumerate(s):
            if ch in curr:
                continue
            while stack and stack[-1] > ch and i < ind[stack[-1]]:
                top = stack.pop()
                curr.remove(top)
            stack.append(ch)
            curr.add(ch)

        return "".join(stack)