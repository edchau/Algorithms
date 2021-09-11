"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values 
of the kth node from the beginning and the kth node from the 
end (the list is 1-indexed).

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head_ptr = head
        kth_from_front = None
        stack = []
        count = 0
        while head != None:
            count += 1
            if count == k:
                kth_from_front = head
            stack.append(head)
            head = head.next
    
        
        kth_from_back = None
        
        while len(stack) > 0:
            k -= 1
            node = stack.pop()
            if k == 0:
                kth_from_back = node
                break
        
        kth_from_front.val, kth_from_back.val = kth_from_back.val, kth_from_front.val
        
        return head_ptr
        