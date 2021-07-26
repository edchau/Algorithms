"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the 
source node, vi is the target node, and wi is the time it takes for a signal to 
travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n 
nodes to receive the signal. If it is impossible for all the n nodes to receive the
 signal, return -1.
"""


import heapq as hq
import collections


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = collections.defaultdict(list)
        # reorder into adj list
        for time in times:
            adj[time[0]].append((time[1], time[2]))
        
        
        distances = {}
        pq = []
        
        hq.heappush(pq, (0, k))
        
        while len(pq) > 0:
            dist, node = hq.heappop(pq)
            if node not in distances:
                # add distances here (minimum since based on priority)
                distances[node] = dist
                for to, w in adj[node]:
                    if to not in distances:
                        # dont add here, cuz it may not be minimum
                        new_dist = w + dist
                        hq.heappush(pq, (new_dist, to))
        
        if len(distances) == n:
            return max(distances.values())
        return -1
            
        
        