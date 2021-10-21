"""
You have a long flowerbed in which some of the plots are 
planted, and some are not. However, flowers cannot be planted 
in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return if n new flowers can be planted in the flowerbed without 
violating the no-adjacent-flowers rule.
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == len(flowerbed)-1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        count += 1
                        flowerbed[i] = 1
                elif i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        count += 1
                        flowerbed[i] = 1
                elif flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    count += 1
        
        return count >= n