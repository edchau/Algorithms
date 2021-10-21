"""
You are given an array prices where prices[i] is 
the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may 
complete as many transactions as you like (i.e., 
buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions 
simultaneously (i.e., you must sell the stock before 
you buy again).
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        # difference between previous will add up to max peak so we
        # dont have to traverse all the way until we find the highest
        # value
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += (prices[i] - prices[i-1])
                
        return max_profit