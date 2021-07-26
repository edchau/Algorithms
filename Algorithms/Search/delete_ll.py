class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

def delete_node(node_a, val):
    pass


# node_a: 1->2->3->4
node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)

node_a = delete_node(node_a, 3)

while node_a != None:
    print(node_a.value)
    node_a = node_a.next