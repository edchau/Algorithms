"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one 
of the symbols '+' and '-' before each integer in nums and 
then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and 
a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, 
which evaluates to target.
"""

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = len(nums)-1
        curr_sum = 0
        self.memo = {}
        return self.knapsack(nums, target, index, curr_sum)
    
    def knapsack(self, nums, target, ind, curr_sum):
        key = (ind, curr_sum)
        if key in self.memo:
            return self.memo[key]
        if ind < 0 and curr_sum == target:
            return 1
        if ind < 0:
            return 0
        positive = self.knapsack(nums, target, ind-1, curr_sum + nums[ind])
        negative = self.knapsack(nums, target, ind-1, curr_sum - nums[ind])
        self.memo[key] = positive + negative
        return self.memo[key]