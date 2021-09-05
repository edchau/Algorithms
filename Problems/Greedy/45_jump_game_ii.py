"""
Given an array of non-negative integers nums, you are 
initially positioned at the first index of the array.

Each element in the array represents your maximum jump 
length at that position.

Your goal is to reach the last index in the minimum 
number of jumps.

You can assume that you can always reach the last index.

"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # can model as target sum, but n^2 time
        num_jumps = 0
        reach = 0
        cur_end = 0
        for i in range(len(nums)-1):
            reach = max(reach, i + nums[i])
            if cur_end == i:
                num_jumps += 1
                cur_end = reach
        return num_jumps