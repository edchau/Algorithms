"""
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. 
That is, for each node, find the value of the first node that is next 
to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next 
greater node of the ith node (1-indexed). If the ith node does not have 
a next greater node, set answer[i] = 0.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # if using java, just go through list and add to arraylist
        stack = []
        result = []
        
        i = 0
        while head != None:
            while len(stack) > 0 and stack[-1][1] < head.val:
                ind, prev = stack.pop()
                result[ind] = head.val
                
            stack.append((i, head.val))
            result.append(0)
            head = head.next
            i += 1
        return result