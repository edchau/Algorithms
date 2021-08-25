"""
Given an array nums with n objects colored red, white, or 
blue, sort them in-place so that objects of the same color 
are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color 
red, white, and blue, respectively.

You must solve this problem without using the library's 
sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 4
        output = [0] * len(nums)
        for num in nums:
            counts[num] += 1
        
        for i in range(1, len(counts)):
            counts[i] += counts[i-1]
        
        for i in range(len(nums)):
            output[counts[nums[i]]-1] = nums[i]
            counts[nums[i]] -= 1
        
        for i in range(len(nums)):
            nums[i] = output[i]