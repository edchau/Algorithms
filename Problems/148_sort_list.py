"""
Given the head of a linked list, return the list after sorting it 
in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1)
memory (i.e. constant space)?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        mid = self.find_mid(head)
        upper_head = mid.next
        
        # splits up left and right
        mid.next = None
        
        left = self.sortList(head)
        right = self.sortList(upper_head)
        
        sorted_list = self.merge(left, right)
        return sorted_list
    
    def merge(self, a, b):
        result = None
        
        if a == None:
            return b
        if b == None:
            return a
        
        if a.val <= b.val:
            result = a
            result.next = self.merge(a.next, b)
        else:
            result = b
            result.next = self.merge(a, b.next)
            
        return result
        
    def find_mid(self, head):
        if head == None:
            return None
        
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow