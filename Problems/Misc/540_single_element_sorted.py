"""
You are given a sorted array consisting of only integers where 
every element appears exactly twice, except for one element which 
appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = left + (right-left) // 2
            
            if mid % 2 == 0:
                # if even, should be first index so 
                # we check to right
                if nums[mid] == nums[mid+1]:
                    left = mid + 2
                else:
                    # otherwise, we know the single digit
                    # is in the first half
                    right = mid
            elif mid % 2 == 1:
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                else:
                    right = mid
        
        return nums[left]
            