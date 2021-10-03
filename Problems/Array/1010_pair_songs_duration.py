"""
You are given a list of songs where the ith song has a duration 
of time[i] seconds.

Return the number of pairs of songs for which their total duration 
in seconds is divisible by 60. Formally, we want the number of indices 
i, j such that i < j with (time[i] + time[j]) % 60 == 0.

"""

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        complements = [0] * 60
        count = 0
        for num in time:
            # take minus for numbers smaller than 60
            count += complements[-num % 60]
            complements[num % 60] += 1
        
        return count