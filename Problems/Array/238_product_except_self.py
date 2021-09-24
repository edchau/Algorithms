"""
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums 
except nums[i].

The product of any prefix or suffix of nums is guaranteed to 
fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without 
using the division operation.
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        left_total = 1
        right_total = 1
        
        for i in range(1, len(nums)):
            left_total *= nums[i-1]
            left[i] *= left_total
            
        for i in range(len(nums)-2, -1, -1):
            right_total *= nums[i+1]
            right[i] *= right_total
            
        output = []
        for i in range(len(nums)):
            output.append(right[i] * left[i])
            
        return output