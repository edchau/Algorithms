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


"""
You are given an integer array coins representing coins 
of different denominations and an integer amount representing 
a total amount of money.

Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination 
of the coins, return 0.

You may assume that you have an infinite number of each kind 
of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        
        # need to cycle thru all coins first before
        # able to use previous count
        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin >= 0:
                    dp[i] += dp[i-coin]
        return dp[amount]