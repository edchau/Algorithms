"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        
        # once we get the negative number, this turns into a two
        # sum ii problem (sorted)
        
        for i, val in enumerate(nums):
            # duplicate number
            if i > 0 and val == nums[i-1]:
                continue
                
            if val > 0:
                break
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + val
                if total == 0:
                    result.append([val, nums[left], nums[right]])
                    # move one pointer
                    left += 1
                    # if that pointer is equal to prev val, keep going
                    # avoid duplicate results
                    while nums[left] == nums[left-1] and left < right:
                        left += 1     
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                
        return result