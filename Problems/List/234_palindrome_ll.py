"""
Given the head of a singly linked list, return true if it is a palindrome.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        
        head_copy = head
        
        while head_copy != None:
            stack.append(head_copy.val)
            head_copy = head_copy.next
        
        
        while head != None:
            if head.val != stack.pop():
                return False
            head = head.next
        
        return True