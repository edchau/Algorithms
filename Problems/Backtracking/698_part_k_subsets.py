"""
Given an integer array nums and an integer k, return 
true if it is possible to divide this array into k 
non-empty subsets whose sums are all equal.

O(k*(2^n))
"""

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        visited = [False] * len(nums)
        return self.dfs(nums, 0, k, target, 0, visited)
        
        
    def dfs(self, nums, idx, k, target, total, visited):
        if k == 1:
            return True
        
        if total == target:
            # because some previous elements may not be part of 
            # current path leading to curSum == targetSum. so you 
            # have to start over for next k - 1 recursion
            # key: must have visited list to do this
            return self.dfs(nums, 0, k-1, target, 0, visited)
        
        for i in range(idx, len(nums)):
            if not visited[i] and total + nums[i] <= target:
                visited[i] = True
                if self.dfs(nums, i+1, k, target, total + nums[i], visited):
                    return True
                visited[i] = False
        return False