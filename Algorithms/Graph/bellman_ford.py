"""
Bellman Ford Algorithm

O(VE) Time (near complete graph worst)
AVG O(V+ElogV) using min priority queue

"""
class Edge:
    def __init__(self, fr, to, cost):
        self.fr = fr
        self.to = to
        self.cost = cost

n = 3 # num vertices
# (vertex, weight)
test_input1 = [Edge(0,1,1), Edge(0,2,5), Edge(1,2,1)]


# negative cycle
n2 = 4
test_input2 = [Edge(0,1,1), Edge(1,2,-4), Edge(2,0,2), Edge(2,3,1)]

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

def bellman_ford(g, n, s):
    dist = [float('inf') for i in range(n)]
    dist[s] = 0

    # For each vertex, apply relaxation for all edges
    for _ in range(n-1):
        for edge in g:
            if dist[edge.fr] + edge.cost < dist[edge.to]:
                dist[edge.to] = dist[edge.fr] + edge.cost
 
    # Run algo again to detect which nodes are part of negative cycle.
    # Negative cycle occurs if better path beyond optimal solution
    # is found.
    for _ in range(n-1):
        for edge in g:
            if dist[edge.fr] + edge.cost < dist[edge.to]:
                dist[edge.to] = float('-inf')

    return dist


print(bellman_ford(test_input1, n, 0))
print(bellman_ford(test_input2, n2, 0))