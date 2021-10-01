"""
There are n soldiers standing in a line. Each soldier is assigned 
a unique rating value.

You have to form a team of 3 soldiers amongst them under the following 
rules:

Choose 3 soldiers with index (i, j, k) with rating 
(rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or 
(rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions.
(soldiers can be part of multiple teams).
"""

class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        """
        For each soldier, count how many soldiers on the left and right have less and greater ratings.

        This soldier can form less[left] * greater[right] + greater[left] * less[right] teams.
        """
        result = 0
        for i in range(1, len(rating)-1):
            left_greater = 0
            right_greater = 0
            left_smaller = 0
            right_smaller = 0
            
            for j  in range(len(rating)):
                if rating[i] < rating[j]:
                    # smaller
                    if i < j:
                        right_smaller += 1
                    elif i > j:
                        left_smaller += 1
                if rating[i] > rating[j]:
                    # greater
                    if i < j:
                        right_greater += 1
                    elif i > j:
                        left_greater += 1
            result += left_greater * right_smaller + left_smaller * right_greater
                    
        
        return result