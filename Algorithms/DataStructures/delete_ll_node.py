class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

def delete_node(node_a, val):
    head = node_a
    prev = None
    while node_a != None:
        if node_a.value == val:
            if prev == None:
                head = node_a.next
            else:
                prev.next = node_a.next
        prev = node_a
        node_a = node_a.next
    
    return head


# node_a: 1->2->3->4
node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)

node_a = delete_node(node_a, 3)

while node_a != None:
    print(node_a.value)
    node_a = node_a.next