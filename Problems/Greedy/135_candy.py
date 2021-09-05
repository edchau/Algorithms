"""
There are n children standing in a line. Each child is 
assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the 
following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their 
neighbors.
Return the minimum number of candies you need to have to 
distribute the candies to the children.
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # if 0 or 1 children
        if len(ratings) < 2:
            return len(ratings)
        
        candy = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                candy[i] = max(candy[i+1] + 1, candy[i])
                
        return sum(candy)
                
        