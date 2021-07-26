"""
1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane,
where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between 
them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there 
is exactly one simple path between any two points.
"""


import heapq

class Solution(object):

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 2:
            return 0
        mst_cost = 0
        points = [(pt[0], pt[1]) for pt in points] 
        
        g = self.create_adj_list(points)
        visited = {}
        edge_count = 0
        
        pq = []
        self.add_edges(g, points[0], pq, visited)
        while len(pq) > 0:
            if edge_count == len(points) - 1:
                break
            cost, edge = heapq.heappop(pq)
            
            if edge in visited:
                continue
            edge_count += 1
            mst_cost += cost
            
            self.add_edges(g, edge, pq, visited)
            
        return mst_cost if edge_count == len(points)-1 else 0
        
    def create_adj_list(self, points):
        adj = {}
        for cur in points:
            for pt in points:
                if pt == cur:
                    continue

                cost = self.man_dist(cur, pt)
                if cur not in adj:
                    adj[cur] = []
                adj[cur].append((cost, pt))
        return adj

    def add_edges(self, g, node, pq, visited):
        visited[node] = True
        for edge in g[node]:
            if edge[1] not in visited:
                heapq.heappush(pq, edge)
    
    def man_dist(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    