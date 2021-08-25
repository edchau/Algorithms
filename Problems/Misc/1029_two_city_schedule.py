"""
A company is planning to interview 2n people. Given 
the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, 
and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such 
that exactly n people arrive in each city.

 

Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have 
half the people interviewing in each city.

"""
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        min_cost = 0
        for cost in costs:
            min_cost += cost[0]
        
        refunds = []
        for cost_a, cost_b in costs:
            refunds.append(cost_a-cost_b)
            
        refunds.sort(reverse=True)
        
        for i in range(len(costs) // 2):
            min_cost -= refunds[i]
        
        return min_cost