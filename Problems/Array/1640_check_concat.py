"""
You are given an array of distinct integers arr 
and an array of integer arrays pieces, where the 
integers in pieces are distinct. Your goal is to 
form arr by concatenating the arrays in pieces in 
any order. However, you are not allowed to reorder 
the integers in each array pieces[i].

Return true if it is possible to form the array arr 
from pieces. Otherwise, return false.
"""

class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        ## dictionary
        # key: head number of piece
        # value: all number of single piece
        mapping = { piece[0]: piece for piece in pieces }
        
        result = []
        
        # try to make array from pieces
        for number in arr:
            
            result += mapping.get( number, [] )
        
        # check they are the same or not
        return result == arr