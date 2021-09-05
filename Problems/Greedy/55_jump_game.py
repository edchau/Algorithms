"""
You are given an integer array nums. You are initially 
positioned at the array's first index, and each element in 
the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = len(nums)-1
        for idx in range(len(nums)-2, -1, -1):
            if idx + nums[idx] >= reach:
                reach = idx
        
        return reach == 0


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0

        for i in range(len(nums)-1):
            reach = max(reach, i+nums[i])
            if reach == i:
                return False
        return True
            