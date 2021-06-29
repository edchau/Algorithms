class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None




# Init two linked lists
# node_a: 1->2->3->4
# node_b: 1->2->3->4->1
node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)