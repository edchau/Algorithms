"""
697. Degree of an Array
Given a non-empty array of non-negative integers nums, 
the degree of this array is defined as the maximum frequency 
of any one of its elements.

Your task is to find the smallest possible length of a 
(contiguous) subarray of nums, that has the same degree as nums.

Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

O(n) time
O(n) space
"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        left = {}
        right = {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            
            right[num] = i
            count[num] = count.get(num, 0) + 1
            
        max_freq = max(count.values())
        min_len = len(nums)
        
        for num in nums:
            if count[num] == max_freq:
                length = right[num] - left[num] + 1
                if length < min_len:
                    min_len = length
        return min_len