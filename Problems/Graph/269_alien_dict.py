"""
https://www.youtube.com/watch?v=6kTZYvNNyps&ab_channel=NeetCode

Alien Dictionary

Topological Sort DAG
"""

from collections import defaultdict
def alien_order(words):
    # Create DAG
    adj = defaultdict(set)
    
    for i in range(1, len(words)):
        w1, w2 = words[i-1], words[i]
        min_len = min(len(w1), len(w2))

        # Invalid Order
        if w1[:min_len] == w2[:min_len] and len(w2) > len(w1):
            return ""

        # Else, create the adj list
        for j in range(min_len):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    """
    i.e.  w -> e -> r -> t -> f
    """
    # Kahn Algorithm for topological sort

    in_deg = defaultdict(int)

    # init in degree
    for key in adj.keys():
        in_deg[key] = 0

    for key in adj.keys():
        for neighbor in adj[key]:
            in_deg[neighbor] += 1

    queue = []

    # init queue with in degree 0
    for key in in_deg.keys():
        if in_deg[key] == 0:
            queue.append(key)

    order = []
    k = 0
    # BFS
    while len(queue) > 0:
        node = queue.pop(0)
        if k > len(in_deg):
            return ""
        k += 1
        order.append(node)
        for neighbor in adj[node]:
            in_deg[neighbor] -= 1
            if in_deg[neighbor] == 0:
                queue.append(neighbor)
    
    if k != len(in_deg):
        return ""
    
    return "".join(order)


test_input1 = ["wrt", "wrf", "er", "ett", "rftt"]
print(alien_order(test_input1)) # wertf


test_input2 = ["wrt", "wrf", "wrt", "ett", "rftt"]
print(alien_order(test_input2)) # ""