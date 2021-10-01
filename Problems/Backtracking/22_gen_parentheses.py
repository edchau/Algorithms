"""
Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.dfs(0, 0, n, "", result)
        return result
    
    def dfs(self, open_p, close_p, n, path, res):
        if len(path) == n * 2:
            res.append(path)
            return
        
        if open_p < n:
            self.dfs(open_p+1, close_p, n, path+"(", res)
            
        if close_p < open_p:
            self.dfs(open_p, close_p+1, n, path+")", res)
        
        