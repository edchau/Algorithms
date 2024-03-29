"""
Given an integer n, return the least number of perfect
square numbers that sum to n.

A perfect square is an integer that is the square of an 
integer; in other words, it is the product of some integer 
with itself. For example, 1, 4, 9, and 16 are perfect squares 
while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
"""

import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        dp[0] = 1
        
        coins = [i*i for i in range((int)(math.sqrt(n))+1)]
        for coin in coins:
            for i in range(coin, n+1):
                if i == coin:
                    dp[i] = 1
                    continue
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[n]

"""
class Solution {
    public int numSquares(int n) {
        ArrayList<Integer> squares = new ArrayList<>();
        int num = 1;
        while (num * num <= n) {
            squares.add(num*num);
            num += 1;
        }
        
        int[] dp = new int[n+1];
        Arrays.fill(dp, n+1);
        dp[0] = 1;
        for (int coin : squares) {
            for(int i = 0; i < n+1; ++i) {
                if (i == coin) {
                    dp[i] = 1;
                }
                else if (i - coin >= 0) {
                    dp[i] = Math.min(dp[i], dp[i-coin] + 1);
                }
            }
        }
        return dp[n];
    }
}
"""