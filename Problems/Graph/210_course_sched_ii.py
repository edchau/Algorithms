"""
There are a total of numCourses courses you have to take, labeled from 0 to 
numCourses - 1. You are given an array prerequisites where prerequisites[i] = 
[ai, bi] indicates that you must take course bi first if you want to take course 
ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first 
take course 1.
Return the ordering of courses you should take to finish all courses. If there 
are many valid answers, return any of them. If it is impossible to finish all 
courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you 
should have finished course 0. So the correct course order is [0,1].
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
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
        course_order = [0] * numCourses
        

        while len(queue) > 0:
            course = queue.pop(0)
            course_order[index] = course
            index += 1
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if index != numCourses:
            return []
        return course_order