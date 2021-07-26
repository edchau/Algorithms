"""
Dijkstra's Shortest Path Algorithm

O((V+E)logV) Time (near complete graph worst)
O(V) using min priority queue

O(ELogE) time for heap implementation

"""

from queue import PriorityQueue

n = 3 # num vertices
# (vertex, weight)
test_input1 = [[(1,1),(2,5)], [(2,1)], []]

n2 = 4
test_input2 = [[(1,1),(2,5)], [(2,1)], [(3,2)],  []]
"""
test input 1 (acyclic):
     0
   /  \
  .    .
 1  -.  2

test input 2 (cyclic):
     0
   /  .
  .    \
 1  -.  2 -. 3
 -----------.
"""

def dijkstra(g, n, s):
    visited = [False for i in range(n)]
    dist = [float('inf') for i in range(n)]

    # used to reconstruct path
    prev = [None for i in range(n)]
    pq = PriorityQueue()
    pq.put((s, 0))
    dist[s] = 0 # starting node

    while pq.qsize() > 0:
        index, minValue = pq.get()
        visited[index] = True

        # # early cutoff
        # if dist[index] < minValue:
        #     continue

        for node in g[index]:
            to, w = node
            if visited[to]:
                continue
            newDist = dist[index] + w
            if newDist < dist[to]:
                prev[to] = index
                dist[to] = newDist
                pq.put((to, w))
    
    return dist, prev

def find_shortest_path(g, n, s, e):
    dist, prev = dijkstra(g, n, s)
    path = []

    # end node is not reachable
    if dist[e] == float('inf'):
        return path
    
    # start from n node and trace backwards
    trace = e
    while trace != None:
        path.insert(0, trace)
        trace = prev[trace]
    
    return path
    

print(dijkstra(test_input1, n, 0))
print(dijkstra(test_input2, n2, 0))

print(find_shortest_path(test_input1, n, 0, 2))
print(find_shortest_path(test_input2, n2, 0, 3))
