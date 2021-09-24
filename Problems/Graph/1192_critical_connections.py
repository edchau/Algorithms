"""
There are n servers numbered from 0 to n - 1 connected 
by undirected server-to-server connections forming a network 
where connections[i] = [ai, bi] represents a connection between 
servers ai and bi. Any server can reach other servers directly 
or indirectly through the network.

A critical connection is a connection that, if removed, will make 
some servers unable to reach some other server.

Return all critical connections in the network in any order.

https://www.youtube.com/watch?v=RYaakWv5m6o&ab_channel=TechRevisions
O(V+E)
"""
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = [[] for _ in range(n)]
        
        # build graph
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
    
        # lowest_rank[i] is lowest id vertex that can reach vertex i
        lowest_rank = [i for i in range(n)] 
        visited = [False for _ in range(n)] 
        result = []
        self.dfs(result, graph, lowest_rank, visited, 0, -1, 0)
        return result
    
    def dfs(self, res, graph, lowest_rank, visited, curr_rank, prev_v, curr_v):
        visited[curr_v] = True
        lowest_rank[curr_v] = curr_rank
        
        for neighbor in graph[curr_v]:
            if neighbor == prev_v:
                # do not include the the incoming path to this 
                # vertex since this is the possible ONLY bridge 
                # (critical connection) that every vertex needs
                continue
            
            if not visited[neighbor]:
                self.dfs(res, graph, lowest_rank, visited, curr_rank+1, curr_v, neighbor)
            
            # find lowest id vertex that can reach vertex i
            lowest_rank[curr_v] = min(lowest_rank[curr_v], lowest_rank[neighbor])
            
            # if gap between two nodes, then the edge is critical connection
            if lowest_rank[neighbor] - curr_rank >= 1:
                res.append([curr_v, neighbor])