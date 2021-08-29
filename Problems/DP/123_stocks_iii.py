"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        K = 2
        dp = [[0] * (len(prices)) for _ in range(K+1)]

        for k in range(1, K+1):
            for i in range(1, len(prices)):
                min_price = prices[0]
                for j in range(1, i+1):
                    # prices[i] - prices[j] + dp[k-1][j-1]
                    # reference dp to get max profit from
                    # prior to minimum price (must sell
                    # before buying another)
                    min_price = min(min_price, prices[j] - dp[k-1][j-1])
                dp[k][i] = max(prices[i] - min_price, dp[k][i-1])

        return dp[k][len(prices)-1]