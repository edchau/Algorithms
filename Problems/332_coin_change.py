"""
You are given an integer array coins representing coins of 
different denominations and an integer amount representing 
a total amount of money.

Return the fewest number of coins that you need to make up 
that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1.

You may assume that you have an infinite number of each 
kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            if dp[i] > -1:
                for coin in coins:
                    if i + coin < amount + 1:
                        if dp[i+coin] == -1 or dp[i] + 1 < dp[i+coin]:
                            dp[i+coin] = dp[i] + 1

        return dp[amount]