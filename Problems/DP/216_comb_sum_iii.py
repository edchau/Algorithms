"""
Find all valid combinations of k numbers that sum up to n such that
the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not 
contain the same combination twice, and the combinations may be returned 
in any order.
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        dp = [[] for i in range(n+1)]
        candidates = [i for i in range(1, 10)]
        result = []
        self.backtrack(candidates, n, 0, [], result, k)
        return result
    
    def backtrack(self, cand, target, idx, path, res, k):
        # idx is starting value from which we take numbers
        if target == 0:
            if len(path) == k:
                res.append(path)
            return
        if target < 0:
            return
        for i in range(idx, len(cand)):
            # prevent duplicates (sorted list)
            if i > idx and cand[i] == cand[i-1]:
                continue
            self.backtrack(cand, target-cand[i], i+1, path+[cand[i]], res, k)