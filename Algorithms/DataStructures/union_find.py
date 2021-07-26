def find(node, root):
    if node == root[node]:
        return node
    else:
        return find(root[node], root)

def union(node0, node1, root):
    node0 = find(node0, root)
    node1 = find(node1, root)
    
    root[node1] = node0
    return

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0
        edges = []
        for i in range(1, len(points)):
            for j in range(i):
                dist = abs(points[i][0]-points[j][0]) \
                    + abs(points[i][1] - points[j][1])
                edges.append([i, j, dist])
        
        edges.sort(key=lambda x: x[2])
        
        root = [_ for _ in range(len(points))]
        n_edge = 0
        ret = 0
        while n_edge < len(points) - 1:
            (i, j, dist) = edges.pop(0)
            if find(i, root) != find(j, root):
                ret += dist
                n_edge += 1
                union(i, j, root)
        
        return ret