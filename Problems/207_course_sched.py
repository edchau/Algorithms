class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = []
        
        for i in range(numCourses):
            adj.append([])
        
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
            
        
        # get in degree
        in_deg = [0 for i in range(numCourses)]
        for lst in adj:
            for i in lst:
                in_deg[i] += 1
        
        # input initial nodes with no incoming edges
        queue = [i for i in range(len(in_deg)) if in_deg[i] == 0]
        
        index = 0
        # order = [0 for i in range(numCourses)]
 
        # topological sort using kahn alg
        while len(queue) != 0:
            at = queue.pop(0)
            # order[index] = at
            index += 1
            
            for to in adj[at]:
                in_deg[to] -= 1
                if in_deg[to] == 0:
                    queue.append(to)
            
        if index != numCourses:
            return False
        
        return True
        
