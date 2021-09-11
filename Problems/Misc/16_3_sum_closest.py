"""
Given an integer array nums of length n and an integer 
target, find three integers in nums such that the sum is 
closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = float('inf')
        
        for i, val in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[left] + nums[right] + val
                
                if total <= target:
                    left += 1
                elif total > target:
                    right -= 1
                    
                if abs(total-target) < abs(result-target):
                    result = total
        
        return result