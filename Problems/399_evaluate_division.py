"""
You are given an array of variable pairs equations and an array of real 
numbers values, where equations[i] = [Ai, Bi] and values[i] represent 
the equation Ai / Bi = values[i]. Each Ai or Bi is a string that 
represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents 
the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, 
return -1.0.

Note: The input is always valid. You may assume that evaluating the queries 
will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
"""
from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj = defaultdict(list)
        
        for eq, val in zip(equations, values):
            adj[eq[0]] += [(eq[1], val)]
            adj[eq[1]] += [(eq[0], 1/val)]
        
        answers = []
        for q in queries:
            answers.append(self.compute_path(adj, q[0], q[1]))
        
        return answers

        
    def compute_path(self, adj, start, end):
        queue = [(start, 1)]
        visited = {start}

        if end in adj:
            while len(queue) > 0:
                node, val = queue.pop(0)
                if node == end:
                    return val

                for to, to_val in adj[node]:
                    path_val = val * to_val
                    if to not in visited:
                        queue.append((to, path_val))
                        visited.add(to)
                
        return -1.0