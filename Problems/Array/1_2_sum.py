class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in complements:
                return [complements[comp], i]
            else: 
                complements[nums[i]] = i
        
        return []