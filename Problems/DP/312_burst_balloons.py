"""
You are given n balloons, indexed from 0 to n - 1. Each balloon 
is painted with a number on it represented by an array nums. You 
are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * 
nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, 
then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
"""

"""
https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations

Same problem as
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
"""

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        A = nums
        dp = [[0]*(n) for _ in range(n)]
        
        # compute tri i, j, k while adding the prev triangles from i to k and j to k
        for L in range(2, n):
            # how many triangles to compute
            for i in range(n-L):
                j = i + L
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + A[i]*A[k]*A[j])
        return dp[0][n-1]