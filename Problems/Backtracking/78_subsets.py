"""
Given an integer array nums of unique elements, 
return all possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for k in range(len(nums)+1):
            self.backtrack(nums, 0, [], res, k)
        return res
    
    
    def backtrack(self, nums, idx, path, res, k):
        if len(path) == k:
            res.append(path)
            return
        
        for i in range(idx, len(nums)):
            self.backtrack(nums, i+1, path + [nums[i]], res, k)