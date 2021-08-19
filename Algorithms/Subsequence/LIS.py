"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly 
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting 
some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


i.e.
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], 
therefore the length is 4.

O(nlogn) Time

Use Patience Sorting
https://www.youtube.com/watch?v=K9M6g7BiBX4&ab_channel=CodersCamp
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