"""
You are given an integer array nums consisting of n elements, 
and an integer k.

Find a contiguous subarray whose length is equal to k that 
has the maximum average value and return this value. Any 
answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_k = 0
        for i in range(k):
            sum_k += nums[i]
        
        max_sum = sum_k
        
        for i in range(k, len(nums)):
            sum_k += nums[i] - nums[i-k]
            if sum_k > max_sum:
                max_sum = sum_k

        return max_sum / float(k)