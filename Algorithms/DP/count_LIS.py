"""
Given an integer array nums, return the number of longest 
increasing subsequences.

Notice that the sequence has to be strictly increasing.


Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences
are [1, 3, 4, 7] and [1, 3, 5, 7].
"""


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = [1] * len(nums)
        freq = [1] * len(nums)

        count = 1
        max_len = 1
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if longest[j] + 1 > longest[i]:
                        longest[i] = longest[j] + 1
                        freq[i] = freq[j]
                    elif longest[j] + 1 == longest[i]:
                        freq[i] += freq[j]
            if longest[i] > max_len:
                max_len = longest[i]
                count = freq[i]
            elif longest[i] == max_len:
                count += freq[i]
        return count