"""
An image is represented by an m x n integer grid image where 
image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You 
should perform a flood fill on the image starting from the pixel 
image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any 
pixels connected 4-directionally to the starting pixel of the same 
color as the starting pixel, plus any pixels connected 4-directionally 
to those pixels (also with the same color), and so on. Replace the 
color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image
        
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image
        
    
    def fill(self, image, sr, sc, color, new_color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color:
            return
        image[sr][sc] = new_color
        self.fill(image, sr + 1, sc, color, new_color)
        self.fill(image, sr, sc + 1, color, new_color)
        self.fill(image, sr - 1, sc, color, new_color)
        self.fill(image, sr, sc - 1, color, new_color)