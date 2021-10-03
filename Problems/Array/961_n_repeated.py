"""
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

 

Example 1:

Input: nums = [1,2,3,3]
Output: 3
"""

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        if one element is repeated n times,
        than any order of nums will contain that
        element s.t. nums[i] = nums[i-1] or
        nums[i] = nums[i-1]
        Otherwise, it will be the first element
        """
        
        for i in range(2, len(nums)):
            if nums[i] == nums[i-1] or nums[i] == nums[i-2]:
                return nums[i]
        
        return nums[0]