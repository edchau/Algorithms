"""
Given an integer array nums with possible duplicates, randomly 
output the index of a given target number. You can assume that 
the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where 
nums[i] == target. If there are multiple valid i's, then each index 
should have an equal probability of returning.

"""

import collections
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.indices = collections.defaultdict(list)
        for i, val in enumerate(nums):
            self.indices[val].append(i)
            
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.indices.get(target, -1))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)