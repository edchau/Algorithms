"""
There are n gas stations along a circular route, where the amount of 
gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas 
to travel from the ith station to its next (i + 1)th station. You begin 
the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's 
index if you can travel around the circuit once in the clockwise direction, 
otherwise return -1. If there exists a solution, it is guaranteed to be 
unique
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) - sum(cost) < 0:
            return -1

        # otherwise, a solution exists
        # if the current gas tank turns negative,
        # we reset the start to the position after
        # since if the running total is negative, we
        # cannot start from any position prior to the
        # current one
        
        start = 0
        gas_tank = 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start = i+1
                gas_tank = 0
            
        return start
        