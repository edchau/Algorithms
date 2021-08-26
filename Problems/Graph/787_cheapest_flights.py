"""
There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, 
toi, pricei] indicates that there is a flight from city 
fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, 
return the cheapest price from src to dst with at most 
k stops. If there is no such route, return -1.

"""

import heapq as hq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # make adj list
        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[2], flight[1]))
            
        # init priority queue
        pq = []
        hq.heappush(pq, (0, src, k+1))
        
        # init visited
        visits = [0] * n
        
        # Dijkstra (O(V+E))
        while len(pq) > 0:
            cost, node, stops = hq.heappop(pq)
            
            if node == dst:
                return cost
            if visits[node] >= stops:
                continue
            visits[node] = stops
            
            for price, neighbor in adj[node]:
                hq.heappush(pq, (cost+price, neighbor, stops-1))

        return -1
            
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Bellman Ford (O(VE))
        prev = [float('inf')] * n
        prev[src] = 0
        
        # Run again if negatives exist
        for _ in range(k+1):
            """
            Bellman Ford algorithm, keeps on updating the distance 
            array while relaxing the edges( i.e it relax the next edge 
            (u,v) based on updated distance(u) )...so it hides the 
            track of number of edges visited in between... while here 
            we hold the updated distance till we traverse all the edges 
            and then update the distance for the next iteration
            """
            curr = prev[::]
            for fro, to, price in flights:
                curr[to] = min(curr[to], prev[fro]+price)
            prev = curr
            
        return -1 if curr[dst] == float('inf') else curr[dst]