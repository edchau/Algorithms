"""
Given two equal-size strings s and t. In one step you 
can choose any character of t and replace it with 
another character.

Return the minimum number of steps to make t an anagram 
of s.

An Anagram of a string is a string that contains the 
same characters with a different (or the same) ordering.
"""

import collections
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        counts = collections.defaultdict(int)
        
        num_steps = 0
        
        for i in range(len(t)):
            # if counts of a char is negative,
            # then we have extra in t, ignore this
            # to not overcount
            # if counts of char is positive,
            # we need to change the extras to
            # match s (guaranteed to find answer)
            counts[t[i]] -= 1
            counts[s[i]] += 1
            
        for key in counts.keys():
            if counts[key] > 0:
                num_steps += counts[key]

        return num_steps