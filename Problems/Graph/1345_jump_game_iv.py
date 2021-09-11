"""
Given an array of integers arr, you are initially positioned at the first index 
of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is 
the last index of the array.
"""

import collections

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # create graph
        adj_list = collections.defaultdict(list)
        for i, val in enumerate(arr):
            adj_list[val].append(i)
        
        # node, ind
        queue = [(arr[0], 0, 0)]
        # min_jumps = 0
        # visited set is mainly for i+1 and i-1
        visited = set()
        visited.add(0)
        
        # BFS to find path to last index
        while len(queue) > 0:
            node, i, jumps = queue.pop(0)   
            
            if i == len(arr) - 1:
                return jumps
            
            if i+1 < len(arr) and i+1 not in visited:
                queue.append((arr[i+1], i+1, jumps+1))
                visited.add(i+1)
            if i-1 >= 0 and i-1 not in visited:
                queue.append((arr[i-1], i-1, jumps+1))
                visited.add(i-1)
            
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append((arr[neighbor], neighbor, jumps+1))
                    visited.add(neighbor)
            #clear adj list to prevent looking repeat nodes again
            adj_list[node] = {}

        return 0
                