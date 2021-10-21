"""
You are given two lists of closed intervals, firstList and secondList, 
where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers 
x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are 
either empty or represented as a closed interval. For example, the intersection 
of [1, 3] and [2, 4] is [2, 3]
"""

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        first_ptr = 0
        second_ptr = 0
        output = []
        
        while first_ptr < len(firstList) and second_ptr < len(secondList):
            
            start_1, end_1 = firstList[first_ptr]
            start_2, end_2 = secondList[second_ptr]
            
            if start_1 <= end_2 and start_2 <= end_1:
                output.append([max(start_1, start_2), min(end_1, end_2)])
            
            if end_1 < end_2:
                first_ptr += 1
            else:
                second_ptr += 1
        
        
        return output