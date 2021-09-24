"""
Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect. If the two 
linked lists have no intersection at all, return null.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # slow method: concatenate list and check for cycle
        # fast method: use two pointers and switch
        # headA and headB pointers at the point where 
        # either one is None
        if headA == None or headB == None:
            return None
        
        a = headA
        b = headB
        
        while a != b:
            # eventually, after one pass if the list is not 
            # same length, the pointers will meet since we
            # switch the heads
            if not a:
                a = headB
            elif not b:
                b = headA
            else:
                a = a.next
                b = b.next
        
        return a