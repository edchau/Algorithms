"""
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the 
first two lists.


Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val <= l2.val:
            result = l1
            result.next = self.mergeTwoLists(l1.next, l2)
        else:
            result = l2
            result.next = self.mergeTwoLists(l1, l2.next)
        
        return result
        