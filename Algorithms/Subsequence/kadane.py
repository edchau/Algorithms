"""
Kadane's Algorithm

Used to find largest contiguous subarray sum

O(N) Time
O(1) Space
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        max_sum = nums[0]
        current = nums[0]
        
        for i in range(1, len(nums)):
            current = max(nums[i], nums[i] + current)
            max_sum = max(max_sum, current)
        
        return max_sum