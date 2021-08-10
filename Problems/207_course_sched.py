"""
There are a total of numCourses courses you have to take, labeled 
from 0 to numCourses - 1. You are given an array prerequisites 
where prerequisites[i] = [ai, bi] indicates that you must take 
course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 
you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
"""


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
        
