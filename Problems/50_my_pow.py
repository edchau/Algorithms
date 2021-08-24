"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

O(logn) Time
O(logn) Space
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1/x, -1*n)
        
        p = 0
        if n % 2 == 0:
            p = self.myPow(x*x, n//2)
        else:
            p = self.myPow(x*x, n//2) * x
        
        return p