"""
Given the head of a linked list and an integer val, remove 
all the nodes of the linked list that has Node.val == val, 
and return the new head.

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = ListNode()
        prev_ptr = prev
        
        while head != None:
            if head.val != val:
                prev.next = head
                prev = prev.next
            else:
                prev.next = None
                
            head = head.next
        
        return prev_ptr.next
            