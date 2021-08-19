"""
Given a m * n matrix seats  that represent seats distributions in a 
classroom. If a seat is broken, it is denoted by '#' character otherwise
it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, 
upper left and upper right, but he cannot see the answers of the student 
sitting directly in front or behind him. Return the maximum number of 
students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.
"""


class Solution(object):
    """
    https://leetcode.com/problems/maximum-students-taking-exam/discuss/988450/max-flow-ford-fulkerson-and-edmonds-karp-algorithm-solution-in-javascript
    """
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        seat_count, graph, source, sink = self.build_graph(seats)
        flow = self.max_flow(graph, source, sink)
        # seats available - max num of students cheating
        return seat_count - flow
    
    def build_graph(self, seats):
        m, n = len(seats), len(seats[0])
        source = m*n
        sink = m*n+1
        
        seat_count = 0
        # directions for cheating or where people could cheat from
        directions = [[0,-1],[-1,-1],[1,-1],[0,1],[-1,1],[1,1]]
        
        # adj matrix size m*n + 2
        graph = [[0] * (m*n + 2) for _ in range(m*n + 2)]
        
        # divide graph into Bipartite graph and then add source/sink to left/right
        # - Place alternate column nodes to two different bipartite graph
        # - i.e. j = 0, 2, 4, 6,....n will be in group A
        # - j = 1, 3, 5 ......n will be in group B
        for i in range(m):
            for j in range(n):
                
                # if seat is broken, skip
                if seats[i][j] == '#':
                    continue
                
                seat_count += 1
                node = i * n + j
                
                if j % 2 == 0:
                    # bipartite group A
                    graph[source][node] = 1
                    
                    for r, c in directions:
                        x = i + r
                        y = j + c
                        
                        # invalid seat
                        if x < 0 or x >= m or y < 0 or y >= n or seats[x][y] == '#':
                            continue
                    
                        neighbor = x * n + y
                        graph[node][neighbor] = 1
                    
                else:
                    # bipartite group B
                    graph[node][sink] = 1
        
        return seat_count, graph, source, sink
        
    def bfs(self, g, source, sink):
        n = len(g)
        visited = [False for _ in range(n)]
        parent = [None for _ in range(n)]
        
        queue = []
        
        # init queue with source
        queue.append(source)
        visited[source] = True
        parent[source] = None
        
        while len(queue) > 0:
            
            node = queue.pop(0)
            
            if node == sink:
                return parent
            
            for neighbor in range(n):
                if not visited[neighbor] and g[node][neighbor] >= 1:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    queue.append(neighbor)
        return parent
    
    def max_flow(self, g, source, sink):
        flow = 0
        
        while True:
            parent = self.bfs(g, source, sink)
            
            if parent[sink] == None:
                break
            
            v = sink
            while v != source:
                u = parent[v]
                g[u][v] -= 1
                g[v][u] += 1
                v = u
                
            flow += 1
            
        return flow
            
            