"""
You are given an array of integers stones where stones[i] is the weight 
of the ith stone.

We are playing a game with the stones. On each turn, we choose the 
heaviest two stones and smash them together. Suppose the heaviest two 
stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight
y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no 
stones left, return 0.


"""

import heapq as hq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        pq = []
        for s in stones:
            hq.heappush(pq, -1*s)
        
        while len(pq) > 1:
            y = -1*hq.heappop(pq)
            x = -1*hq.heappop(pq)
            
            if x != y:
                hq.heappush(pq, x-y)
        
        if len(pq) == 1:
            return -1*hq.heappop(pq)
        return 0