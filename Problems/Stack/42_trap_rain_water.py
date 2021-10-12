"""
Given n non-negative integers representing an elevation map where the width 
of each bar is 1, compute how much water it can trap after raining.


Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
are being trapped.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        
        for idx, h in enumerate(height):
            while len(stack) > 0 and h > height[stack[-1]]:
                prev = stack.pop()
                if len(stack) > 0:
                    peek = stack[-1]
                    width = idx - peek - 1
                    result += width * (min(h, height[peek]) - height[prev])
            stack.append(idx)
        return result