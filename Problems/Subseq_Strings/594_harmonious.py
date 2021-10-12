"""
We define a harmonious array as an array where the difference 
between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest 
harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from 
the array by deleting some or no elements without changing the 
order of the remaining elements.
"""
import collections

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        
        max_length = 0
        for num in nums:
            if num+1 in counts:
                max_length = max(max_length, counts[num] + counts[num+1])
            
            if num-1 in counts:
                max_length = max(max_length, counts[num] + counts[num-1])
                
        return max_length