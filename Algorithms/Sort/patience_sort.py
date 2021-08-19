"""
Longest Increasing Subsequence using Patience Sorting

https://www.youtube.com/watch?v=K9M6g7BiBX4&ab_channel=CodersCamp
O(nlogn) Time
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = [nums[0]]
        
        for num in nums:
            for i in range(len(stack)):
                if stack[i] >= num:
                    stack[i] = num
                    break
            if num not in stack:
                stack.append(num)
        
        return len(stack)