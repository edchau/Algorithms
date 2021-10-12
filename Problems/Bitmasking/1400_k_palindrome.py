"""
Given a string s and an integer k. You should construct 
k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to 
construct k palindrome strings or False otherwise.

"""


class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        counts = defaultdict(int)
        for ch in s:
            counts[ch] += 1
        
        num_odd = 0
        for c in counts.values():
            if c % 2 != 0:
                num_odd += 1
        return num_odd <= k and k <= len(s)


# Note: Use Bit Manipulation to get Constant Space
# Number & 1 to check odd