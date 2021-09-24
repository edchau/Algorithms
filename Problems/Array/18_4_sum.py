"""
Given an array nums of n integers, return an array of all 
the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            three_sum = self.threeSum(nums[i+1:], target-val)
            if len(three_sum) > 0:
                for lst in three_sum:
                    result.append([val] + lst)
            
        return result
        

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        # once we get the negative number, this turns into a two
        # sum ii problem (sorted)
        
        for i, val in enumerate(nums):
            # duplicate negative number
            if i > 0 and val == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + val
                if total == target:
                    result.append([val, nums[left], nums[right]])
                    # move one pointer
                    left += 1
                    # if that pointer is equal to prev val, keep going
                    # avoid duplicate results
                    while nums[left] == nums[left-1] and left < right:
                        left += 1     
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1
                
        return result