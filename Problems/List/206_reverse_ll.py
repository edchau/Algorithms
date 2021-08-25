"""
Given the head of a singly linked list, reverse the list, 
and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        
        while head != None:
            next_node = head.next
            head.next = prev
            
            prev = head
            head = next_node
        
        return prev