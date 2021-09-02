"""
Given an integer array nums and an integer k, return the kth 
largest element in the array.

Note that it is the kth largest element in the sorted order, 
not the kth distinct element.
"""

# Heap

import heapq as hq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        pq = []
        
        for num in nums:
            hq.heappush(pq, num)
        
        while len(pq) > 0:
            val = hq.heappop(pq)
            if k == 0:
                return val
            k -= 1

# Quick Select
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k=len(nums)-k
        return self.quick_select(nums, 0, len(nums)-1, k)
    
    def quick_select(self, nums, l, r, k):
        part = l
        for i in range(l, r):
            if nums[i] <= nums[r]:
                nums[i], nums[part] = nums[part], nums[i]
                part += 1
        nums[part], nums[r] = nums[r], nums[part]
        
        if part > k:
            return self.quick_select(nums, l, part-1, k)
        elif part < k:
            return self.quick_select(nums, part+1, r, k)
        else:
            return nums[part]
