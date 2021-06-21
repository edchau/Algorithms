"""
Finding Connected Components using DFS
Graph represented as Adjacency List

O(V+E) Time
O(V) Space
"""

n = 7 # num vertices
test_input1 = [[1], [2], [0], [4] ,[3] ,[6] ,[5]]

def findComponents(g, n):
    visited = [False for i in range(n)]
    count = 0
    components = [0 for i in range(n)]
    # loop bc disconnnectivity
    for node in range(n):
        if not visited[node]:
            # counter for components
            count += 1
            dfs(g, node, visited, components, count)
    return (count, components)


def dfs(g, node, visited, components, count):
    visited[node] = True
    components[node] = count
    for next in g[node]:
        if not visited[next]:
            dfs(g, next, visited, components, count)


print(findComponents(test_input1, n))