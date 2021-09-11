"""
You are a professional robber planning to rob houses along a 
street. Each house has a certain amount of money stashed. All 
houses at this place are arranged in a circle. That means the 
first house is the neighbor of the last one. Meanwhile, adjacent 
houses have a security system connected, and it will automatically 
contact the police if two adjacent houses were broken into on the
 same night.

Given an integer array nums representing the amount of money of each 
house, return the maximum amount of money you can rob tonight without 
alerting the police.



"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[n-1]
        return max(self.find_max(nums, 0, n-2), self.find_max(nums, 1, n-1))
        
    def find_max(self, nums, start, end):
        rob = 0
        dont_rob = 0
        for i in range(start, end+1):
            r = rob
            dr = dont_rob
            # curr val + prev house no rob
            rob = nums[i] + dr
            # update to best prev subproblem
            dont_rob = max(r, dr)
        return max(rob, dont_rob)

