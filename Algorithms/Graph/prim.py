"""
Prim's MST Algorithm

MST is complete when # of edges 1 less than the # of nodes

O(ELogE) Time (Lazy)
O(ELogV) Time (Eager) -> Uses Index Priority Queue instead of Queue
Update destination node with most promising incoming edge instead of 
adding edges to PQ
"""
from queue import PriorityQueue

class Edge:
    def __init__(self, fr, to, cost):
        self.fr = fr
        self.to = to
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

# negative cycle
n = 4
test_input = [[Edge(0,1,1), Edge(0, 3, 5)], [Edge(1,2,4)], [Edge(2,0,2), Edge(2,3,6)], []]

"""
test input (cyclic):
     0 ------
   /  .      |
  .    \     .
 1  -.  2 -. 3
 -----------.
"""

def lazy_prim(g, n, s):
    visited = [False for i in range(n)]
    m = n-1 # number of edges in MST
    edge_count, mst_cost = 0, 0
    mst_edges = [None for i in range(m)]
    pq = PriorityQueue()
    add_edges(g, s, pq, visited)

    while pq.qsize() > 0 and edge_count != m:
        edge = pq.get()
        node_index = edge.to

        if visited[node_index]:
            continue

        mst_edges[edge_count] = (edge.fr, node_index)
        edge_count += 1
        mst_cost += edge.cost

        add_edges(g, node_index, pq, visited)
        
    if edge_count != m:
        return None, None # No MST Exists
    
    return mst_cost, mst_edges


def add_edges(g, s, pq, visited):
    visited[s] = True
    for edge in g[s]:
        if not visited[edge.to]:
            pq.put(edge, edge.cost)
    
print(lazy_prim(test_input, n, 0))