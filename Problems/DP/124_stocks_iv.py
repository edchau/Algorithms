class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        K = k
        dp = [[0] * (len(prices)) for _ in range(K+1)]

        for k in range(1, K+1):
            min_price = prices[0]
            # in stocks iii, min was repeated calculation
            for i in range(1, len(prices)):
                min_price = min(min_price, prices[i] - dp[k-1][i-1])
                dp[k][i] = max(prices[i] - min_price, dp[k][i-1])

        return dp[k][len(prices)-1]