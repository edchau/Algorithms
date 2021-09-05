"""
Given an array of distinct integers nums and a target integer target, 
return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.


"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i + num < target+1:
                    dp[i+num] += dp[i]
        return dp[target]
        
    