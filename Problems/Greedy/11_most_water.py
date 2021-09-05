"""
Given n non-negative integers a1, a2, ..., an , where each represents 
a point at coordinate (i, ai). n vertical lines are drawn such that 
the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, 
which, together with the x-axis forms a container, such that the container 
contains the most water.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_water = 0

        while left < right:
            distance = right - left
            water = 0
            if height[left] < height[right]:
                water = distance * height[left]
                left += 1
            else:
                water = distance * height[right]
                right -= 1

            max_water = max(max_water, water)

        return max_water
