"""
Given the head of a linked list and a value x, partition 
it such that all nodes less than x come before nodes greater 
than or equal to x.

You should preserve the original relative order of the nodes 
in each of the two partitions.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        less_than = ListNode()
        less_start = less_than
        greater_than = ListNode()
        great_start = greater_than
        while head != None:
            if head.val < x:
                less_than.next = ListNode(head.val)
                less_than = less_than.next
            else:
                greater_than.next = ListNode(head.val)
                greater_than = greater_than.next
            
            head = head.next
        
        less_than.next = great_start.next
        
        return less_start.next