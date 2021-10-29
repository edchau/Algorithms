"""
A frog is crossing a river. The river is divided into some 
number of units, and at each unit, there may or may not exist 
a stone. The frog can jump on a stone, but it must not jump 
into the water.

Given a list of stones' positions (in units) in sorted ascending 
order, determine if the frog can cross the river by landing on 
the last stone. Initially, the frog is on the first stone and 
assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either 
k - 1, k, or k + 1 units. The frog can only jump in the forward 
direction.
"""

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) == 0:
            return True
        
        # store possible k values for next move
        positions = {}
        
        for stone in stones:
            positions[stone] = set()
            
        # initial val only has k value of 1
        positions[0].add(1)
        
        for i in range(len(stones)-1):
            stone = stones[i]
            for step in positions[stone]:
                reach = step + stone
                
                # end condition
                if reach == stones[len(stones) - 1]:
                    return True
                
                # get the next set of all steps the
                # current one can reach
                next_jump = positions.get(reach, None)
                
                # add all possible moves for next reach
                # k, k+1, k-1
                if next_jump != None:
                    next_jump.add(step)
                    if (step - 1 > 0):
                        next_jump.add(step - 1);
                    next_jump.add(step + 1)
        		
        return False
        
        