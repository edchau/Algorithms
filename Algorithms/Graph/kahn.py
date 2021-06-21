"""
Toplogical Sort Using Kahn Algorithm
Directed Acyclic Graph represented as Adjacency List

Can also be used to check for cycles

O(V+E) Time
O(V) Space (given adj list)
"""

n = 3 # num vertices
test_input1 = [[1,2], [2], []]
test_input2 = [[1], [2], [0]]
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

def kahn(g, n):
    # 1. Get in degree of all vertices
    in_deg = [0 for i in range(n)]

    for out in g:
        for v in out:
            in_deg[v] += 1
    
    # 2. Init queue with vertices that have no incoming edges
    queue = [i for i in range(len(in_deg)) if in_deg[i] == 0]

    index = 0
    order = [0 for i in range(n)]

    # 3. While the queue is not empty, traverse through graph
    #    and update in degrees of removed nodes
    while len(queue) != 0:
        at = queue.pop(0)

        # insert current vertex into order
        order[index] = at
        index += 1

        for out in g[at]:
            # update in degree of cur nodes
            in_deg[out] -= 1

            # if updated node has 0 in deg, enqueue
            if in_deg[out] == 0:
                queue.append(out)
            
    if index != n:
        return "graph is cyclic"
    
    return order


print(kahn(test_input1, n))
print(kahn(test_input2, n))