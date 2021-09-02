"""
You have a convex n-sided polygon where each vertex has an integer 
value. You are given an integer array values where values[i] is the 
value of the ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle, 
the value of that triangle is the product of the values of its vertices, 
and the total score of the triangulation is the sum of these values over 
all n - 2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some 
triangulation of the polygon.
"""

class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        A = values
        dp = [[0]*(n) for _ in range(n)]
        
        # compute tri i, j, k while adding the prev triangles from i to k and j to k
        for L in range(2, n):
            # how many triangles to compute
            for i in range(n-L):
                j = i + L
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i]*A[k]*A[j])
        return dp[0][n-1]