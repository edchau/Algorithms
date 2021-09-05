"""
Given an integer numRows, return the first 
numRows of Pascal's triangle.
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[] for _ in range(numRows)]
        triangle[0] = [1]

        for i in range(1, numRows):
            row = triangle[i-1]
            triangle[i].append(1)
            for j in range(1, len(row)):
                triangle[i].append(row[j-1] + row[j])
            triangle[i].append(1)
            
        return triangle