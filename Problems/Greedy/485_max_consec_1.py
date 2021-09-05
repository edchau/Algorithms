"""
Given a binary array nums, return the maximum number of consecutive 
1's in the array.
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        max_len = 0
        
        for num in nums:
            if num == 1:
                current += 1
            else:
                max_len = max(current, max_len)
                current = 0
        
        return max(max_len, current)