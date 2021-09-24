"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        
        return [self.search_left(nums, target), self.search_right(nums, target)]
    
    def search_left(self, nums, target):
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] == target:
            return left
        else:
            return -1
            
    def search_right(self, nums, target):
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left + right) // 2 + 1
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        
        if nums[left] == target:
            return left
        else:
            return -1