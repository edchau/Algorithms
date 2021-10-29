"""
Given an unsorted array of integers nums, return 
the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        
        not_visited = set(nums)
        
        for num in nums:
            if num in not_visited:
                val = num
                not_visited.remove(num)
                
                total = 1
                
                while (val+1) in not_visited:
                    not_visited.remove((val+1))
                    val += 1
                    total += 1
                
                val = num
                while (val-1) in not_visited:
                    not_visited.remove((val-1))
                    val -= 1
                    total += 1
                    
                longest = max(longest, total)
            
            
        return longest