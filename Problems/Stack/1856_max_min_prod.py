"""
The min-product of an array is equal to the minimum value 
in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a 
min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product 
of any non-empty subarray of nums. Since the answer may be large, 
return it modulo 109 + 7.

Note that the min-product should be maximized before performing 
the modulo operation. Testcases are generated such that the maximum 
min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray 
[2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
"""

"""
The min-product of an array is equal to the minimum value 
in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a 
min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product 
of any non-empty subarray of nums. Since the answer may be large, 
return it modulo 109 + 7.

Note that the min-product should be maximized before performing 
the modulo operation. Testcases are generated such that the maximum 
min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray 
[2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
"""

class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # get running sums
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)
        
        # use increasing stack
        # Intuition: consider each val if
        # it was the min of a subarray
        
        # find max subsequence given that the current val
        # is min value
        max_min_prod = 0
        stack = []
        for i, val in enumerate(nums):
            start = i
            while stack and stack[-1][1] > val:
                idx, top = stack.pop()
                total = sums[i] - sums[idx]
                max_min_prod = max(max_min_prod, top * total)
                # if prev val is larger, then the subarray
                # can expand to the left and still maintain
                # its status as min value
                start = idx
            stack.append((start, val))
        print(stack)
        
        # compute max min prod from start to end
        # longest subarray possible given current
        # min val
        for start, val in stack:
            total = sums[len(nums)] - sums[start]
            max_min_prod = max(max_min_prod, val * total)
        
        return max_min_prod % (10**9 + 7)