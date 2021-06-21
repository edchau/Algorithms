"""
Given two linked lists, the task is to check whether the first 
list is present in 2nd list or not. 
O(nm)
"""

class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None
 
def find_list(first, second):
    """
    checks if first lst is in second lst
    """
    #both empty
    if not first and not second:
        return True

    # one is empty
    if not first or not second:
        return False

    ptr1 = first
    ptr2 = second

    while ptr2:
        ptr2 = second
        while ptr1:

            # ptr2 ran out but ptr1 still has elements
            if not ptr2:
                return False

            # advance
            elif ptr1.value == ptr2.value:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            
            # single mismatch
            else:
                break

        # if traversed through ptr1, then match
        if not ptr1:
            return True

        # advance second
        ptr1 = first
        second = second.next

    return False
        
            
# Init two linked lists
# node_a: 1->2->3->4
# node_b: 1->2->1->2->3->4
node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)
 
node_b = Node(1)
node_b.next = Node(2)
node_b.next.next = Node(1)
node_b.next.next.next = Node(2)
node_b.next.next.next.next = Node(3)
node_b.next.next.next.next.next = Node(4)

if find_list(node_a, node_b):
    print("LIST FOUND")
else:
    print("LIST NOT FOUND")