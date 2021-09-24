"""
Given the head of a linked list, rotate the list to the right 
by k places.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if k == 0:
            return head
        
        # deque = []
        head_ptr = head
        length = 1
        
        while head_ptr.next != None:
            head_ptr = head_ptr.next
            length += 1
        
        # set end to front of list
        head_ptr.next = head
        
        # Use modulo to compute k greater than len of head
        # instead of deque
        k = k % length
        
        # shift entire k block at the end
        temp_head = head
        # -1 to get the the number of iterations to get to length - k block
        for _ in range(length-k-1): 
            temp_head = temp_head.next
            k -= 1
        
        start = temp_head.next
        temp_head.next = None
        
        return start
    
        # while k > -1:
        #     front = deque.pop()
        #     if k == 0:
        #         front.next = None
        #     else:
        #         front.next = head
        #         head = front
        #         deque.insert(0, front)
        #     k -= 1