"""
Given an array of integers arr, find the sum of min(b), 
where b ranges over every (contiguous) subarray of arr. 
Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], 
[3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
"""

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        
        # count values less than left
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((arr[i], count))
        
        stack = []
        # count values less than right
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))
            
        # left * right is total num of times the val is min
        total = 0
        for  i in range(n):
            total += left[i] * right[i] * arr[i]
        
        return total % (10**9 + 7)






    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        stack = []
        arr = [0] + arr + [0]
        # alternative: iterate thru to get left counts
        # and right counts
        for right, x in enumerate(arr):
            while len(stack) > 0 and arr[stack[-1]] > x:
                val = stack.pop()
                left = stack[-1]
                # currrent val * num indices greater on left 
                # * num indices greater on right
                # i.e. 3, 1, 2
                # left, val, right (need to go to right first)
                result += arr[val] * (val-left) * (right-val)
            # store indices in stack to calc left and right
            stack.append(right)
            
        return result % (10**9 + 7)