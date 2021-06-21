"""
Breadth First Search Algorithm w/ Shortest Path
Graph represented as Adjacency List

O(V+E) Time
O(V) Space
"""


n = 3 # num vertices
test_input1 = [[1,2], [2], []]
test_input2 = [[1], [2], [0]]
test_input3 = [[2], [], [1]]

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
 1  -.  2
""" 

def bfs(g, n):
    visited = [False for i in range(n)]
    start_node = 0
    queue = []

    # begin bfs with startnode
    queue.append(start_node)
    visited[start_node] = True

    prev = [None for i in range(n)]
    while len(queue) > 0:
        node = queue.pop(0)
        neighbors = g[node]

        for next in neighbors:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                prev[next] = node
    
    # can use prev to reconstruct shortest path
    # for simple bfs, omit prev and just traverse nodes
    return prev


print(bfs(test_input1, n))
print(bfs(test_input2, n))
print(bfs(test_input3, n))
