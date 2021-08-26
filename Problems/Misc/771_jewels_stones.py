"""
You're given strings jewels representing the types of stones that are 
jewels, and stones representing the stones you have. Each character 
in stones is a type of stone you have. You want to know how many of 
the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type 
of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

O(n+m) Time
"""

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels = set(jewels)
        return sum([1 for s in stones if s in jewels])