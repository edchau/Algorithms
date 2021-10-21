"""
Given an integer array nums and an integer k, return the 
k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # bucket sort
        freq = defaultdict(int)
        
        for n in nums:
            freq[n] += 1
            
        
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for key in freq.keys():
            bucket[freq[key]].append(key)
        
        result = []
        for i in range(len(bucket)-1, -1, -1):
            if len(bucket[i]) > 0:
                result += bucket[i][:k]
                k -= len(bucket[i])
            if k <= 0:
                break
        return result