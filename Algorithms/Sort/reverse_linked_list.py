class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

def invert_ll(head):
    prev = None
    cur = head
    while cur != None:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next

    # not pass by reference
    head = prev

    return head


# node_a: 1->2->3->4
node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)

node_a = invert_ll(node_a)

while node_a != None:
    print(node_a.value)
    node_a = node_a.next