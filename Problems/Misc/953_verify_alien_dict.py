"""
In an alien language, surprisingly, they also use English lowercase 
letters, but possibly in a different order. The order of the alphabet 
is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the 
order of the alphabet, return true if and only if the given words 
are sorted lexicographically in this alien language.
"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        translate = {}
        
        # map to normal alphabet
        for i in range(26):
            translate[order[i]] = i
        
        
        for i in range(1, len(words)):
            prev = words[i-1]
            curr = words[i]
            if (self.bigger(prev, curr, translate)):
                return False
                
        return True

    def bigger(self, w1, w2, translate):
        for ch1, ch2 in zip(w1, w2):
            if translate[ch1] != translate[ch2]:
                return translate[ch1] > translate[ch2]
        
        return len(w1) > len(w2)
