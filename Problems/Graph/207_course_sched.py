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

O(V+E)
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]
        
        # make adj list and calc indegree
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        # topological sort to look for cycles
        queue = []
        
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        index = 0
        
        # kahn algorithm
        while len(queue) > 0:
            course = queue.pop(0)
            index += 1
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return index == numCourses