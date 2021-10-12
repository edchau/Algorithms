"""
Given an integer n, return how many distinct phone numbers 
of length n we can dial.

You are allowed to place the knight on any numeric cell 
initially and then you should perform n - 1 jumps to dial a 
number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 10^9 + 7.
"""
class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        # possible moves at each space
        adj = {0: [4, 6], 1: [8, 6], 2: [7, 9], 3: [4, 8],
                   4: [3, 9, 0], 5: [], 6: [0, 7, 1], 7: [2, 6],
                   8: [1, 3], 9: [4, 2]}
        memo = {}
        
        # subproblems: how many digits can we store starting at
        # each number (prevent recalculations)
        result = 0
        
        # start at each digit
        for i in range(10):
            result += self.dfs(i, n, adj, memo)
            
        return result % (10**9+7)
        
    def dfs(self, start, n, adj, memo):
        if n == 1:
            return 1
        key = (n, start)
        
        if key in memo:
            return memo[key]
        
        memo[key] = 0
        for nxt in adj[start]:
            memo[key] += self.dfs(nxt, n-1, adj, memo)
            
        return memo[key]