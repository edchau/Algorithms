"""
Given an integer array nums, in which exactly two elements appear 
only once and all the other elements appear exactly twice. Find the 
two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity 
and uses only constant extra space.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for num in nums:
            diff ^= num
        
        print(diff)
        # 2 = 010
        # 3 = 011
        # 5 = 101
        # 6 = 110
        a = 0
        b = 0
        mask = 1
        while diff & mask == 0:
            mask = mask << 1
        
        # 3&mask and 5&mask must have different results (0011&0010 = 0010, 0101&0010 = 0000)
        for num in nums:
            if num & mask > 0:
                a ^= num
            else:
                b ^= num
            
        return [a, b]