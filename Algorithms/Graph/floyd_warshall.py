"""
Floyd Warshall Algorithm

Find all pairs shortest path in weighted directed graph
(Recommended for small graphs due to time)

Recurrence Relation:
dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])

dp[k-1][i][j]: best distance from i to j with values routing from 0 to k-1
(go from i to j)

dp[k-1][i][k] + dp[k-1][k][j]: best distance from i to j through node k, 
reusing best solutions from 0 to k-1 (go from i to k, then k to j)

Since we loop over k starting from 0, we compute solution for k in place,
so dimensions go down to O(V^2)

New Recurrence Relation
dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

O(V^3) Time 
O(V^2) Space
"""

# Create matrix
n = 7
m = [[float('inf') for j in range(n)] for i in range(n)]
for i in range(n):
    m[i][i] = 0
m[0][1] = 2;
m[0][2] = 5;
m[0][6] = 10;
m[1][2] = 2;
m[1][4] = 11;
m[2][6] = 2;
m[6][5] = 11;
m[4][5] = 1;
m[5][4] = -2;

"""
Setup
"""
# init dp array
dp = [[0 for j in range(n)] for i in range(n)]
next = [[float('inf') for j in range(n)] for i in range(n)]
# Copy input matrix and setup 'next' matrix for path reconstruction.
for i in range(n):
    for j in range(n):
        if (m[i][j] != float('inf')):
             next[i][j] = j;
        dp[i][j] = m[i][j];

def get_apsp_matrix():
    """
    Runs floyd warshall to compute shortest 
    distance between every pair of nodes
    """
    floyd_warshall()
    return dp

def floyd_warshall():
    # Computes all pairs shortest path
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next[i][j] = next[i][k]

    # Identify negative cycles
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] != float('inf') and dp[k][j] != float('inf') and dp[k][k] < 0:
                    dp[i][j] = float('-inf')
                    next[i][j] = -1
   
def reconstructPath(start, end):
    path = []
    # no path exists
    if dp[start][end] == float('inf'):
        return path
    
    trace = start
    while trace != end:
        # null since infinite cycle
        if trace == -1:
            return None
        path.append(trace)
        trace = next[trace][end]

    if next[trace][end] ==  -1:
        return None
    
    path.append(end)
    return path
    

dist = get_apsp_matrix();

for i in range(n):
    for j in range(n):
        print("The shortest path from ", i, " to ", j, ": ", dist[i][j])

""" 
The shortest path from node 0 to node 0 is 0.000
The shortest path from node 0 to node 1 is 2.000
The shortest path from node 0 to node 2 is 4.000
The shortest path from node 0 to node 3 is Infinity
The shortest path from node 0 to node 4 is -Infinity
The shortest path from node 0 to node 5 is -Infinity
The shortest path from node 0 to node 6 is 6.000
The shortest path from node 1 to node 0 is Infinity
The shortest path from node 1 to node 1 is 0.000
The shortest path from node 1 to node 2 is 2.000
The shortest path from node 1 to node 3 is Infinity
...
"""

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        path = reconstructPath(i, j)
        if path != None and path != []:
            print("shortest path from ", i, " to ", j, ": ", path)