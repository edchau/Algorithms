"""
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

 
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        
        if target % 2 != 0:
            return False
        
        target //= 2
        
        dp = [False for i in range(target+1)]
        
        dp[0] = True # can sum to 0
        
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
                    
        return dp[target]