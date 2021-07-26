"""
Given an array arr, replace every element in that 
array with the greatest element among the elements 
to its right, and replace the last element with -1.

After doing so, return the array.

KEY: GO BACKWARDS IN LIST
"""

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        max_value = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        
        for i in range(len(arr)-2, -1, -1):
            current = arr[i]
            arr[i] = max_value
            max_value = max(max_value, current)
            
        return arr