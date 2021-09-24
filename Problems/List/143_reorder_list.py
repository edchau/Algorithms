"""
You are given the head of a singly linked-list. 
The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. 
Only nodes themselves may be changed.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None:
            return []
        
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        curr = slow.next
        while curr != None:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        slow.next = None
        
        # merge lists
        head1, head2 = head, prev
        while head2:
            temp_next = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp_next
            
        