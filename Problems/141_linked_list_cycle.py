"""
Given a linked list, check if there exists a cycle
O(N)
"""

class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None


def tortoise_hare(head):
    if head == None:
        return
    
    ptr1 = head
    ptr2 = head

    while ptr1.next != None and ptr2.next.next != None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
        if (ptr1 == ptr2):
            return True
        
    return False
        

# Init two linked lists
# node_a: 1->2->3->4
# node_b: 1->2->3->4->1
node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)
 
node_b = Node(1)
node_b.next = Node(2)
node_b.next.next = Node(3)
node_b.next.next.next = Node(4)
node_b.next.next.next.next = node_b

print(tortoise_hare(node_a)) # false
print(tortoise_hare(node_b)) # true