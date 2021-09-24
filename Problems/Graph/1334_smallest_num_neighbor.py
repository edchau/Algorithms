"""
There are n cities numbered from 0 to n-1. Given the array edges where 
edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted 
edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable
 through some path and whose distance is at most distanceThreshold, If 
 there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the 
sum of the edges' weights along that path.
"""

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dis = [[float('inf')] * n for _ in range(n)]

        # init distances
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
            
        # distances to self is 0
        for i in range(n):
            dis[i][i] = 0
        
        # Floyd Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        
        result = {}
        # Find smallest number of cities given a certain threshold
        for i in range(n):
            total = 0
            for d in dis[i]:
                if d <= distanceThreshold:
                    total += 1
            result[total] = i
        
        return result[min(result)]
                