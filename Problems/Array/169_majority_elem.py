"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ 
times. You may assume that the majority element always exists in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ind = 0
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[ind]:
                count += 1
            else:
                count -= 1

            if count == 0:
                ind = i
                count = 1
                
        return nums[ind]