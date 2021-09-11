"""
Given a string containing digits from 2-9 inclusive, return all 
possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        translate = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9': ['w','x','y','z']}
        combinations = []
        self.dfs(translate, 0, digits, "", combinations)
        return combinations
        
        
    def dfs(self, translate, ind, digits, path, comb):
        if len(path) == len(digits):
            comb.append(path)
            return
        
        for i in range(ind, len(digits)):
            for letter in translate[digits[i]]:
                self.dfs(translate, i+1, digits, path+letter, comb)
        