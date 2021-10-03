"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        """
        Perform binary search to find the smallest
        element first
        """
        n = len(nums)
        low = 0
        high = n-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        # Now low is the index of smallest value in nums
        # and also the number of places rotated k
        k = low
        
        """
        Perform binary search mod  n to find the mid
        and rotation ind
        """
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            rotated_mid = (mid + k) % n
            if nums[rotated_mid] == target:
                return rotated_mid
            elif nums[rotated_mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                  
        
        return -1