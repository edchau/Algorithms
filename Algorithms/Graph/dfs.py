"""
Depth First Search Algorithm
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

def dfs(g, n):
    visited = [False for i in range(n)]
    start_node = 0
    # assumes connected
    dfs_helper(g, start_node, visited)
    print("DFS Complete...")

def dfs_helper(g, node, visited):
    if visited[node]:
        return
    visited[node] = True
    print("Visited Node: ", node)

    neighbors = g[node]
    for next in neighbors:
        dfs_helper(g, next, visited)


def dfs_iterative(g, n):
    visited = [False for i in range(n)]
    start_node = 0
    stack = []

    stack.append(start_node)
    while len(stack) > 0:
        node = stack.pop()
        
        if visited[node]:
            continue

        visited[node] = True
        print("Visited Node: ", node)
        for adj in g[node]:
            if not visited[adj]:
                stack.append(adj)

    print("DFS COMPLETE")

    

dfs(test_input1, n)
dfs(test_input2, n)
dfs(test_input3, n)
print("ITERATIVE")
dfs_iterative(test_input1, n)
dfs_iterative(test_input2, n)
dfs_iterative(test_input3, n)
