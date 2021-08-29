"""
Given a collection of candidate numbers (candidates) and a 
target number (target), find all unique combinations in candidates 
where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result
    
    def backtrack(self, cand, target, idx, path, res):
        # idx is starting value from which we take numbers
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(idx, len(cand)):
            # prevent duplicates (sorted list)
            if i > idx and cand[i] == cand[i-1]:
                continue
            self.backtrack(cand, target-cand[i], i+1, path+[cand[i]], res)
            