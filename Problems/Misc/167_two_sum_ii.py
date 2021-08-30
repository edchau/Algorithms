"""
Given an array of integers numbers that is already sorted 
in non-decreasing order, find two numbers such that they add 
up to a specific target number.

Return the indices of the two numbers (1-indexed) as an 
integer array answer of size 2, where 1 <= answer[0] < 
answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        
        return []
                